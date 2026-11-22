"""TF-LUK LAB: educational EOD research engine, not Martin Luk's original code.

Provider: Massive.com REST OHLC API. All signals are generated after close t,
executed at NEXT session open t+1; when both target and stop touch a bar,
stop is assumed to trigger first. Fixed present-day universe introduces
survivorship bias; no intraday execution or spread orderbook modeled.
"""
from __future__ import annotations
import argparse, datetime as dt, io, json, os, pathlib, time
from collections import Counter, defaultdict
import numpy as np
import pandas as pd
import requests

ROOT=pathlib.Path(__file__).resolve().parents[1]
BASE='https://api.massive.com'
ETF_SYMBOLS=['SPY','QQQ','IWM','SMH','IGV','XBI','XLE','XLF']
SECTOR_ETF={
    'Semiconductores':'SMH','Software y ciberseguridad':'IGV',
    'IA e infraestructura':'QQQ','Cuántica':'IWM','Cripto':'QQQ',
    'Fintech':'XLF','Energía y solar':'XLE','Biotecnología':'XBI',
    'Consumo y tecnología':'QQQ'
}
SETUPS={
 'L1':('LONG','Pullback a EMA 9 ascendente'),
 'L2':('LONG','Undercut & reclaim'),
 'S1':('SHORT','Rechazo de EMA 9 descendente'),
 'S2':('SHORT','Failed breakout / upthrust')
}

def fetch_bars(session,ticker,start,end,api_key,cache):
    cache.mkdir(parents=True,exist_ok=True)
    path=cache/f'{ticker}_{start}_{end}.json'
    if path.exists():
        payload=json.loads(path.read_text(encoding='utf-8'))
    else:
        url=f'{BASE}/v2/aggs/ticker/{ticker}/range/1/day/{start}/{end}'
        params={'adjusted':'true','sort':'asc','limit':50000,'apiKey':api_key}
        for attempt in range(6):
            try:
                r=session.get(url,params=params,timeout=35)
                if r.status_code==429 or r.status_code>=500:
                    time.sleep(min(60,4*2**attempt)); continue
                if r.status_code in (401,403):
                    raise RuntimeError(f'{ticker}: acceso denegado ({r.status_code}). Revisa tu clave y cobertura Massive.')
                r.raise_for_status()
                payload=r.json()
                if payload.get('status')=='ERROR':
                    raise RuntimeError(f'{ticker}: {payload.get("error",payload)}')
                path.write_text(json.dumps(payload),encoding='utf-8')
                break
            except requests.RequestException:
                if attempt==5: raise
                time.sleep(min(30,2**attempt))
        else: raise RuntimeError(f'{ticker}: límite de intentos API')
    bars=payload.get('results') or []
    if not bars: return pd.DataFrame()
    df=pd.DataFrame(bars)
    for k in ['o','h','l','c','v','t']:
        if k not in df: return pd.DataFrame()
    dates=pd.to_datetime(df['t'],unit='ms',utc=True).dt.tz_convert('America/New_York').dt.tz_localize(None).dt.normalize()
    out=pd.DataFrame({'date':dates,'open':pd.to_numeric(df.o,errors='coerce'),
        'high':pd.to_numeric(df.h,errors='coerce'),'low':pd.to_numeric(df.l,errors='coerce'),
        'close':pd.to_numeric(df.c,errors='coerce'),'volume':pd.to_numeric(df.v,errors='coerce')})
    out=out.dropna().drop_duplicates('date').sort_values('date').set_index('date')
    out=out[out[['open','high','low','close']].gt(0).all(axis=1)]
    return out

def features(df):
    x=df.copy()
    for n in [9,21,50,150]: x[f'ema{n}']=x.close.ewm(span=n,adjust=False,min_periods=n).mean()
    x['ret20']=x.close.pct_change(20,fill_method=None)
    x['ret5']=x.close.pct_change(5,fill_method=None)
    x['ret60']=x.close.pct_change(60,fill_method=None)
    x['dollarvol20']=(x.close*x.volume).rolling(20,min_periods=20).mean()
    x['prev_low']=x.low.shift(1)
    x['prev_high20']=x.high.shift(1).rolling(20,min_periods=20).max()
    wk=x.close.resample('W-FRI').last().dropna()
    wk9=wk.ewm(span=9,adjust=False,min_periods=9).mean()
    # Only completed Fridays may appear at daily timestamps. No partial-week lookahead.
    x['weekly_ema9']=wk9.reindex(x.index,method='ffill')
    x['leading']=(x.close>x.ema9)&(x.ema9>x.ema21)&(x.ema21>x.ema50)
    x['lagging']=(x.close<x.ema9)&(x.ema9<x.ema21)&(x.ema21<x.ema50)
    return x

def load_universe(path,limit=None):
    u=pd.read_csv(path).fillna('')
    required={'ticker','sector'}
    if not required.issubset(u.columns): raise ValueError('universe.csv requiere ticker,sector')
    u.ticker=u.ticker.str.strip().str.upper()
    u.sector=u.sector.str.strip()
    u=u[(u.ticker!='')&(u.sector!='')].drop_duplicates('ticker')
    if limit and limit>0: u=u.head(limit)
    return dict(zip(u.ticker,u.sector))

def derive_signals(x, market, sector_history, sector, stock, min_dollarvol=1e7):
    # All observations are fully known at signal-day CLOSE; entry is next-day OPEN.
    s=x.copy()
    spy=market['SPY'].reindex(s.index)
    qqq=market['QQQ'].reindex(s.index)
    iwm=market['IWM'].reindex(s.index)
    sector_df=sector_history[sector].reindex(s.index)
    s['rs20']=s.ret20-spy.ret20
    s['sector_rs20']=sector_df['ret20']-spy.ret20
    s['market_long']=(spy.close>spy.ema21)&(qqq.close>qqq.ema21)&(iwm.close>iwm.ema50)
    s['market_short']=(spy.close<spy.ema21)|(qqq.close<qqq.ema21)|(iwm.close<iwm.ema9)
    liquid=s.dollarvol20>=min_dollarvol
    sector_long=s.sector_rs20>0
    sector_short=s.sector_rs20<0
    ma_up=(s.ema9>s.ema21)&(s.ema21>s.ema50)&(s.ema9>s.ema9.shift(5))
    ma_down=(s.ema9<s.ema21)&(s.ema21<s.ema50)&(s.ema9<s.ema9.shift(5))
    s['L1']=liquid&s.market_long&sector_long&(s.rs20>0)&ma_up&(s.low<=s.ema9*1.012)&(s.close>=s.ema9)&(s.close>s.open)
    s['L2']=liquid&s.market_long&sector_long&(s.rs20>0)&(s.close>s.ema21)&(s.low<s.prev_low)&(s.close>s.prev_low)&(s.close>s.open)
    s['S1']=liquid&s.market_short&sector_short&(s.rs20<0)&ma_down&(s.high>=s.ema9*.988)&(s.close<s.ema9)&(s.close<s.open)
    s['S2']=liquid&s.market_short&sector_short&(s.rs20<0)&(s.high>s.prev_high20)&(s.close<s.prev_high20)&(s.close<s.open)&(s.close<s.ema9)
    return s

def resolve_trade(x,signal_index,setup,max_hold=10,rr_target=3.0,slippage_bps=5.0):
    direction,description=SETUPS[setup]
    if signal_index+1>=len(x): return None
    row=x.iloc[signal_index]
    entry_date=x.index[signal_index+1]
    first=x.iloc[signal_index+1]
    slip=slippage_bps/10000.0
    entry=float(first.open)*(1+slip if direction=='LONG' else 1-slip)
    stop=float(row.low)*.995 if direction=='LONG' else float(row.high)*1.005
    risk=entry-stop if direction=='LONG' else stop-entry
    if not np.isfinite(risk) or risk<=0 or risk/entry>.10 or risk/entry<.002: return None
    target=entry+(rr_target*risk if direction=='LONG' else -rr_target*risk)
    final_i=min(len(x)-1,signal_index+max_hold)
    mfe=0.0; mae=0.0
    exit_price=None; outcome='TIEMPO'; exit_date=None
    for j in range(signal_index+1,final_i+1):
        bar=x.iloc[j]
        if direction=='LONG':
            mfe=max(mfe,(float(bar.high)-entry)/risk)
            mae=max(mae,(entry-float(bar.low))/risk)
            # Stops take precedence when both touched. Gaps fill at OPEN, not the stop.
            if bar.open<=stop: exit_price=float(bar.open); outcome='GAP_STOP'
            elif bar.low<=stop: exit_price=stop; outcome='STOP'
            elif bar.open>=target: exit_price=float(bar.open); outcome='GAP_TARGET'
            elif bar.high>=target: exit_price=target; outcome='TARGET'
        else:
            mfe=max(mfe,(entry-float(bar.low))/risk)
            mae=max(mae,(float(bar.high)-entry)/risk)
            if bar.open>=stop: exit_price=float(bar.open); outcome='GAP_STOP'
            elif bar.high>=stop: exit_price=stop; outcome='STOP'
            elif bar.open<=target: exit_price=float(bar.open); outcome='GAP_TARGET'
            elif bar.low<=target: exit_price=target; outcome='TARGET'
        if exit_price is not None:
            exit_date=x.index[j]; break
    if exit_price is None:
        exit_price=float(x.iloc[final_i].close); exit_date=x.index[final_i]
    exit_price*=1-slip if direction=='LONG' else 1+slip
    r=(exit_price-entry)/risk if direction=='LONG' else (entry-exit_price)/risk
    return dict(ticker=x.attrs.get('ticker',''),setup=setup,direction=direction,
        signal_date=x.index[signal_index].strftime('%Y-%m-%d'),
        entry_date=entry_date.strftime('%Y-%m-%d'),exit_date=exit_date.strftime('%Y-%m-%d'),
        entry=round(entry,4),stop=round(stop,4),target=round(target,4),
        exit=round(exit_price,4),r=round(float(r),4),mfe_r=round(mfe,4),mae_r=round(mae,4),reason=outcome)

def summarize(trades):
    if not trades: return {'n':0,'win_rate':None,'avg_r':None,'profit_factor':None,'total_r':None,'max_drawdown_r':None}
    a=np.array([t['r'] for t in trades],float)
    gains=float(a[a>0].sum()); losses=float(-a[a<0].sum())
    eq=np.cumsum(a)
    dd=eq-np.maximum.accumulate(np.r_[0.0,eq])[1:]
    return {'n':len(a),'win_rate':round(float((a>0).mean()*100),2),
      'avg_r':round(float(a.mean()),3),
      'profit_factor':round(gains/losses,2) if losses>0 else None,
      'total_r':round(float(a.sum()),2),'max_drawdown_r':round(float(dd.min()),2),
      'avg_mfe_r':round(float(np.mean([t['mfe_r'] for t in trades])),2),
      'avg_mae_r':round(float(np.mean([t['mae_r'] for t in trades])),2)}

def run_engine(api_key,universe_file=ROOT/'universe.csv',out=ROOT/'data/report.json',
               start='2026-01-01',end=None,max_symbols=30,delay=.25,
               min_dollarvol=10_000_000,hold=10,slippage_bps=5.0, cache=ROOT/'cache'):
    end=end or dt.datetime.now(dt.timezone.utc).date().isoformat()
    u=load_universe(universe_file,max_symbols)
    wanted=list(dict.fromkeys(list(u)+ETF_SYMBOLS))
    session=requests.Session()
    prices={}; failed={}
    print(f'Buscando históricos de {len(wanted)} tickers: {start} → {end}')
    for i,t in enumerate(wanted,1):
        try:
            x=fetch_bars(session,t,start,end,api_key,pathlib.Path(cache))
            if len(x)<80: failed[t]=f'solo {len(x)} velas'; continue
            prices[t]=features(x)
            print(f'  [{i}/{len(wanted)}] {t}: {len(x)} velas')
        except Exception as ex:
            if 'acceso denegado' in str(ex): raise
            failed[t]=str(ex)
            print(f'  [{i}/{len(wanted)}] {t}: ERROR {str(ex)[:100]}')
        if delay: time.sleep(delay)
    if not all(t in prices for t in ['SPY','QQQ','IWM']):
        raise RuntimeError('Faltan datos de SPY/QQQ/IWM: no se puede calcular el régimen de mercado. '+str(failed))
    actual={t:s for t,s in u.items() if t in prices}
    if not actual: raise RuntimeError('No hay acciones con datos suficientes. Revisar clave, plan y fechas.')
    sector_symbols=defaultdict(list)
    for t,sec in actual.items(): sector_symbols[sec].append(t)
    # Historical equal-weight sector return (fixed-current-universe approximation).
    sec_history={}
    for sec,ts in sector_symbols.items():
        returns=pd.concat({t:prices[t]['ret20'] for t in ts},axis=1)
        sec_history[sec]=pd.DataFrame({'ret20':returns.mean(axis=1,skipna=True)})
    indices={t:prices[t] for t in ['SPY','QQQ','IWM']}
    all_dates=sorted(set(prices['SPY'].index))
    latest_date=max(all_dates)
    stock_features={}
    for t,sec in actual.items():
        x=derive_signals(prices[t],indices,sec_history,sec,t,min_dollarvol=min_dollarvol)
        x.attrs['ticker']=t
        stock_features[t]=x
    # Select all signal candidates for testing; no possible intraday same-bar hindsight.
    trades=[]; signals=[]
    for t,x in stock_features.items():
        sec=actual[t]
        for i in range(80,len(x)):
            d=x.index[i]
            if d>latest_date: continue
            for setup in SETUPS:
                if not bool(x.iloc[i][setup]): continue
                if d==latest_date:
                    r=x.iloc[i]; stop=float(r.low)*.995 if setup.startswith('L') else float(r.high)*1.005
                    signals.append(dict(ticker=t,sector=sec,setup=setup,direction=SETUPS[setup][0],
                        description=SETUPS[setup][1],signal_date=d.strftime('%Y-%m-%d'),
                        last_close=round(float(r.close),4),stop_reference=round(stop,4),
                        ret20=round(float(r.ret20)*100,2),sector_rs20=round(float(r.sector_rs20)*100,2),
                        dollarvol20=round(float(r.dollarvol20),0),
                        distance_to_stop_pct=round(abs(r.close-stop)/r.close*100,2),
                        trend='Líder' if r.leading else 'Rezagada' if r.lagging else 'Intermedia',
                        chart=[round(float(c),3) for c in x.close.tail(36)]))
                trade=resolve_trade(x,i,setup,max_hold=hold,slippage_bps=slippage_bps)
                if trade and trade['exit_date']<=latest_date.strftime('%Y-%m-%d'):
                    trade['sector']=sec
                    trades.append(trade)
    trades=sorted(trades,key=lambda x:(x['entry_date'],x['ticker'],x['setup']))
    # Dedup same ticker same entry date when 2 setups coincide; keep both only as research if selected flag.
    trades_unique=[]; seen=set()
    for t in trades:
        key=(t['ticker'],t['entry_date'],t['direction'])
        if key not in seen: trades_unique.append(t);seen.add(key)
    trades=trades_unique
    asof=latest_date.strftime('%Y-%m-%d')
    sectors=[]
    for sec,ts in sector_symbols.items():
        recs=[]
        for t in ts:
            x=stock_features[t]; x=x.loc[:latest_date]
            if x.empty: continue
            r=x.iloc[-1]
            if (latest_date-x.index[-1]).days>5: continue
            if np.isfinite(r.ret20): recs.append((t,r))
        if not recs: continue
        avg20=float(np.mean([float(r.ret20) for _,r in recs]))
        avg5=float(np.mean([float(r.ret5) for _,r in recs if np.isfinite(r.ret5)]))
        avg60=float(np.mean([float(r.ret60) for _,r in recs if np.isfinite(r.ret60)])) if any(np.isfinite(r.ret60) for _,r in recs) else 0
        leaders=sum(bool(r.leading) for _,r in recs); laggards=sum(bool(r.lagging) for _,r in recs)
        spyret=prices['SPY'].loc[:latest_date].iloc[-1].ret20
        sectors.append(dict(sector=sec,etf_proxy=SECTOR_ETF.get(sec,'SPY'),
          ret5=round(avg5*100,2),ret20=round(avg20*100,2),ret60=round(avg60*100,2),
          rs20=round((avg20-float(spyret))*100,2),leading=leaders,lagging=laggards,
          stocks=len(recs),tickers=', '.join(t for t,_ in recs)))
    sectors.sort(key=lambda s:s['rs20'],reverse=True)
    breadth={'leading':sum(bool(x.loc[:latest_date].iloc[-1].leading) for x in stock_features.values()),
      'lagging':sum(bool(x.loc[:latest_date].iloc[-1].lagging) for x in stock_features.values()),
      'total':len(stock_features)}
    breadth['intermediate']=breadth['total']-breadth['leading']-breadth['lagging']
    benchmarks=[]
    for t in ['SPY','QQQ','IWM']:
        r=prices[t].loc[:latest_date].iloc[-1]
        benchmarks.append(dict(ticker=t,close=round(float(r.close),2),ret20=round(float(r.ret20)*100,2),
           over_ema9=bool(r.close>r.ema9),over_ema21=bool(r.close>r.ema21),over_ema50=bool(r.close>r.ema50),
           chart=[round(float(c),2) for c in prices[t].close.tail(42)]))
    by_setup={k:summarize([t for t in trades if t['setup']==k]) for k in SETUPS}
    by_month={m:summarize([t for t in trades if t['entry_date'].startswith(m)])
              for m in sorted(set(t['entry_date'][:7] for t in trades))}
    equity=[];cum=0
    for t in trades:
        cum+=t['r'];equity.append({'date':t['entry_date'],'cum_r':round(cum,2)})
    latest_stocks=[]
    for t,x in stock_features.items():
        x=x.loc[:latest_date];r=x.iloc[-1]
        if (latest_date-x.index[-1]).days>5: continue
        latest_stocks.append(dict(ticker=t,sector=actual[t],close=round(float(r.close),2),
           ret5=round(float(r.ret5)*100,2) if pd.notna(r.ret5) else None,
           ret20=round(float(r.ret20)*100,2) if pd.notna(r.ret20) else None,
           rs20=round(float(r.rs20)*100,2) if pd.notna(r.rs20) else None,
           trend='Líder' if r.leading else 'Rezagada' if r.lagging else 'Intermedia',
           dollarvol20=round(float(r.dollarvol20),0) if pd.notna(r.dollarvol20) else 0,
           ema9=round(float(r.ema9),2) if pd.notna(r.ema9) else None,
           ema21=round(float(r.ema21),2) if pd.notna(r.ema21) else None,
           ema50=round(float(r.ema50),2) if pd.notna(r.ema50) else None,
           chart=[round(float(c),2) for c in x.close.tail(42)]))
    latest_stocks.sort(key=lambda r:r['rs20'] if r['rs20'] is not None else -999,reverse=True)
    signals.sort(key=lambda r:(r['direction']!='LONG',-abs(r['sector_rs20'])))
    report={
        'meta':{'app':'TF-LUK LAB','version':'1.0','mode':'real','provider':'Massive API',
         'asof':asof,'start':start,'requested_end':end,'universe_count':len(actual),
         'generated_utc':dt.datetime.now(dt.timezone.utc).isoformat(),
         'data_note':'Datos ajustados de Massive; no incluyen tape, bid/ask ni avisos de earnings.',
         'bias_note':'Universo definido hoy, sin tickers deslistados: sesgo de supervivencia. Sector por lista manual. Backtest señales al cierre/entrada siguiente apertura. Sin simultaneidad de cartera.',
         'cost_note':f'{slippage_bps} bps de deslizamiento por lado; comisiones, borrow fees, borrow availability, impuestos y financiación no incluidos.'},
        'market':{'benchmarks':benchmarks,'breadth':breadth},
        'sectors':sectors,'stocks':latest_stocks,'candidates':signals,
        'backtest':{'overall':summarize(trades),'by_setup':by_setup,'by_month':by_month,'trades':trades[-800:],
          'equity_r':equity[-800:],'parameters':{'max_hold_sessions':hold,'target_r':3.0,
               'slippage_bps_each_side':slippage_bps,'min_dollarvol20':min_dollarvol,
               'entry':'siguiente apertura','intrabar_collision':'stop primero',
               'note':'R acumulado NO es retorno de cartera. Operaciones independientes pueden solaparse.'}},
        'failed':failed,
        'methodology':{'sources':'Transcripciones de Martin Luk, junio–noviembre 2026. Reglas exactas no publicadas.',
            'long':['L1: pullback a EMA 9 ascendiendo en acción y sector fuerte','L2: undercut & reclaim sobre soporte'],
            'short':['S1: rechazo de EMA 9 descendente en sector débil','S2: failed breakout + vela bajista'],
            'disclaimer':'Hipótesis investigables inspiradas en observaciones. No señales del trader.'}}
    out=pathlib.Path(out);out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(report,ensure_ascii=False,allow_nan=False,indent=2),encoding='utf-8')
    print(f'✅ {out} | {len(actual)} símbolos | {len(signals)} setups activos | {len(trades)} operaciones históricas')
    return report

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--start',default='2026-01-01')
    p.add_argument('--end',default=None)
    p.add_argument('--max-symbols',type=int,default=30)
    p.add_argument('--delay',type=float,default=.25)
    p.add_argument('--min-dollarvol',type=float,default=10000000)
    p.add_argument('--hold',type=int,default=10)
    p.add_argument('--slippage-bps',type=float,default=5)
    p.add_argument('--output',default=str(ROOT/'data/report.json'))
    p.add_argument('--universe',default=str(ROOT/'universe.csv'))
    args=p.parse_args()
    key=os.getenv('MASSIVE_API_KEY','').strip()
    if not key: raise SystemExit('Falta MASSIVE_API_KEY. En Colab se pide por getpass; en GitHub Actions crea un Secret.')
    run_engine(key,args.universe,args.output,args.start,args.end,args.max_symbols,args.delay,args.min_dollarvol,args.hold,args.slippage_bps)

if __name__=='__main__': main()
