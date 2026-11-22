import sys, unittest, tempfile, pathlib, json
from unittest.mock import patch
import numpy as np, pandas as pd
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]/'engine'))
import luk_engine as m

class Tests(unittest.TestCase):
 def setUp(self):
  self.dates=pd.bdate_range('2026-01-02',periods=225)
 def make(self,ticker):
  rng=np.random.default_rng(sum(map(ord,ticker)))
  c=100+np.arange(225)*(.27 if ticker in ['SPY','QQQ','IWM','NVDA'] else -.13)+rng.normal(0,2,225)
  c=np.maximum(c,5)
  return pd.DataFrame({'open':c-.2,'high':c+1.4,'low':c-1.4,'close':c,'volume':np.repeat(1000000,225)},index=self.dates)
 def test_features_weekly_no_future_leak(self):
  x=m.features(self.make('NVDA'))
  self.assertTrue(pd.isna(x.weekly_ema9.iloc[0]))
  self.assertTrue(x.weekly_ema9.notna().sum()>100)
  self.assertEqual(len(x),225)
 def test_stop_collision_is_conservative(self):
  x=self.make('NVDA').iloc[:100].copy();x.attrs['ticker']='TEST'
  x.iloc[50,x.columns.get_loc('low')]=98
  x.iloc[51,x.columns.get_loc('open')]=100
  x.iloc[51,x.columns.get_loc('low')]=96
  x.iloc[51,x.columns.get_loc('high')]=115
  a=m.resolve_trade(x,50,'L1',max_hold=5)
  self.assertEqual(a['reason'],'STOP')
 def test_engine_produces_valid_json(self):
  with tempfile.TemporaryDirectory() as d:
   p=pathlib.Path(d);(p/'universe.csv').write_text('ticker,sector\nNVDA,Semiconductores\nCRWD,Software y ciberseguridad\n')
   with patch.object(m,'fetch_bars',side_effect=lambda session,ticker,start,end,key,cache:self.make(ticker)):
    r=m.run_engine('FAKE',p/'universe.csv',p/'report.json',start='2026-01-01',end='2026-11-20',max_symbols=2,delay=0,cache=p/'cache')
   self.assertEqual(r['meta']['mode'],'real')
   self.assertEqual(len(r['stocks']),2)
   self.assertIn('overall',r['backtest'])
   self.assertTrue((p/'report.json').exists())
   json.loads((p/'report.json').read_text())

if __name__=='__main__':unittest.main()
