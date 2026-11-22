# TF-LUK LAB — Dashboard de ingeniería inversa (junio–noviembre 2026)

Una plataforma experimental **en español** para investigar ideas narradas por Martin Luk, ejecutando reglas EOD explícitas sobre históricos de Massive API. No es una copia oficial de su estrategia, no está afiliada a él y no transmite órdenes bursátiles.

## Qué incluye realmente

- Panel de **SPY, QQQ e IWM**, EMA y amplitud de líderes/intermedias/rezagadas.
- **Ranking sectorial** por retorno equiponderado del universo y fuerza relativa frente a SPY.
- **Scanner** de acciones con filtros por sector, tendencia, fuerza relativa, medias y liquidez; descarga CSV.
- **Señales EOD** de cuatro hipótesis: L1 pullback EMA, L2 undercut/reclaim, S1 rechazo EMA bajista, S2 failed breakout.
- **Backtest** EOD: señal formada al cierre, entrada en la siguiente apertura, target 3R, stop estructural, duración máxima 10 sesiones, 5 bps de slippage por lado. Cuando stop y target ocurren en la misma vela, prioriza stop (conservador). Los gaps se ejecutan a apertura, no al stop, si lo sobrepasan.
- **Playbook** separado entre observaciones de Martin Luk y reglas propuestas por este laboratorio.
- **Calculadora** de acciones por riesgo y máximo nominal. No coloca órdenes.
- **GitHub Actions** programado de lunes a viernes al final del mercado, con clave de Massive almacenada como secreto (no en el frontend).

## LO IMPORTANTE: LIMITACIONES

1. El universo (`universe.csv`) es una **lista contemporánea manual**. Por tanto hay sesgo de supervivencia: no es una prueba del mercado NASDAQ/NYSE completo ni incluye automáticamente todos los tickers deslistados.
2. Los sectores temáticos son una **taxonomía manual**, no necesariamente GICS. La media equiponderada se calcula solo con las empresas incluidas en el CSV. Los ETF indicados en la interfaz son contextuales; el motor no los usa para clasificar empresas.
3. Los setups son **hipótesis nuestras**, no señales exactas ni parámetros oficialmente atribuidos a Martin Luk.
4. Son velas **diarias**. No reconstruye entradas de 1/5/15 minutos, VWAP anclado desde eventos, libro de órdenes, SSR ni fills del trader.
5. La suma de resultados en **R no es una curva invertible de cartera**: admite operaciones simultáneas, no aplica topes de capital agregado ni costes de préstamo en shorts. El drawdown en R es secuencial por orden de entrada, no drawdown diario de equity.
6. Considera slippage configurable pero no spread bid-ask desglosado, comisiones de broker, borrow fees, impuestos ni financiación.
7. Los precios pueden estar ajustados por splits/dividendos según cobertura Massive. Un backtest histórico serio requiere universo point-in-time y revisión de ajustes corporativos.
8. Nunca pegues tu API Key en `app.js`, en `data/report.json` ni en archivos que publiques en GitHub.
9. La API requiere cobertura contratada para las fechas consultadas; si hay errores de autorización o de planes, consulta las restricciones de Massive.

## Inicio rápido con Google Colab (método recomendado)

1. Abre Google Colab: https://colab.research.google.com/
2. Sube **`TF_Luk_Lab_Colab.ipynb`** (incluido en ZIP y también disponible por separado).
3. En la celda de configuración define: `START_DATE="2026-01-01"`, `END_DATE="2026-11-20"`, `MAX_SYMBOLS=30` (ajusta según tu plan Massive), tu riesgo y la lista del archivo `universe.csv`.
4. Ejecuta todas las celdas e introduce tu API Key de Massive cuando se solicite (entrada oculta, no quedará dentro del código fuente).
5. El notebook descargará **`report.json`**. Extrae el ZIP de la web, reemplaza **`data/report.json`** con el archivo generado.
6. Sube el proyecto a GitHub y conéctalo a Vercel. La web mostrará datos reales en lugar de los ejemplos sintéticos.

## Publicar por GitHub y Vercel

1. En https://github.com/new crea el repositorio `TF-Luk-Lab`.
2. Descomprime `TF-Luk-Lab-Proyecto.zip` en tu equipo. Sube **el contenido**, no el ZIP como único archivo, manteniendo las carpetas `data`, `engine` y `.github` y los archivos de la raíz.
3. En https://vercel.com/new elige **Import Git Repository**, selecciona `TF-Luk-Lab`.
4. La app es **HTML, CSS y JavaScript estáticos**: usa Framework Preset = `Other`, Build Command vacío, Output Directory `.` (o valor predeterminado si funciona) y despliega.
5. Al actualizar `data/report.json` y hacer *commit* en GitHub, Vercel hará un nuevo despliegue.
6. Para actualizaciones automatizadas, en GitHub → Repository → Settings → Secrets and variables → Actions → New repository secret, crea `MASSIVE_API_KEY` (introduce tu clave, sin comillas).
7. GitHub → Actions → `Actualizar TF-Luk Lab (Massive)` → `Run workflow` para probar. El workflow está programado de lunes a viernes a las 23:35 UTC, después del cierre habitual; GitHub puede retrasar el cron. Se necesita habilitar las Actions y tener créditos/plan de Massive suficientes.
8. La API Key **no** se guarda en Vercel ni en la web. El workflow genera solo el reporte público JSON.

## Ejecutar localmente

Desde la carpeta del proyecto:

```bash
python -m http.server 8000
```

Abre `http://localhost:8000`. **No abras `index.html` mediante `file://`**, porque el navegador puede bloquear la lectura de `data/report.json`.

## Ejecutar el motor localmente (opcional)

```bash
pip install -r requirements.txt
# macOS / Linux
export MASSIVE_API_KEY="TU_CLAVE_PRIVADA"
# Windows PowerShell: $env:MASSIVE_API_KEY="TU_CLAVE_PRIVADA"
python engine/luk_engine.py --start 2026-01-01 --end 2026-11-20 --max-symbols 30
```

Para ampliar las empresas, edita `universe.csv`. Para analizar 2024–2026 haz `--start 2024-01-01` siempre que tu plan Massive permita esa profundidad.

## Qué construir en la Fase 2

- Universo **point-in-time** completo por sesión, con tickers deslistados y corporate actions.
- Industry mapping histórico fiable por API o dataset de referencia; ETFs como variables adicionales y no sustitutos de sector.
- Scanner intradía 1/5/15 minutos con trigger, costo real, pre/after-market y AVWAP desde un evento bien definido.
- Portfolio simulator con simultaneidad, exposición neta/bruta, topes por sector, margen, borrow fees y slippage dependiente de liquidez.
- Diario de operaciones con evidencias audiovisuales para distinguir operaciones confirmadas de hipótesis del stream.

## Fuentes para endpoints

- https://massive.com/docs/rest/stocks/aggregates/custom-bars
- https://massive.com/docs/rest/stocks/aggregates/daily-market-summary
- https://vercel.com/docs/git

Proyecto experimental independiente. No es asesoramiento financiero.
