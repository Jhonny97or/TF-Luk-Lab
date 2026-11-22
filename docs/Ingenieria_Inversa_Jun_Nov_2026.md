# MARTIN LUK — INGENIERÍA INVERSA DEL MÉTODO DE TRADING
## Junio–noviembre 2026 | Dossier de estudio de las fuentes compartidas

> Alcance: 51 archivos TXT suministrados en tres lotes + 5 transcripciones adicionales pegadas en el chat, de las cuales una se repitió literalmente. No se realizaron inferencias de fecha exacta no presente en las fuentes.
> Esta investigación busca sistematizar lo narrado por el operador; no acredita su rentabilidad ni prueba estadísticamente sus estrategias.

## 1. Resumen ejecutivo

La hipótesis central que explica el método no es una EMA individual sino la interacción **régimen de mercado × liderazgo sectorial × acción relativa × confluencia técnica × punto de invalidación × tamaño**. Los mismos patrones se pueden comprar o vender según el entorno; una señal se rechaza si llega tarde o exige un stop demasiado amplio.

## 2. Proceso decisorio que debe reconstruirse

1. **Contexto de índices.** Identificar si QQQ, SPY e IWM están en tendencia alcista, corrección, distribución o rebote dentro de bajada; observar EMA 9, 21, 50 y soportes semanales.
2. **Breadth de sus watchlists.** Contar líderes, mediocres y rezagadas. Revisar si el deterioro se concentra en un solo sector o se extiende a múltiples industrias/capitalizaciones.
3. **Tema y rotación sectorial.** Comparar semiconductores, software/ciberseguridad, memoria, quantum, solar, infraestructura, cripto, biotecnología y otros grupos por fuerza relativa.
4. **Selección transversal.** Preferir acciones líquidas y con tendencia semanal clara; mirar cercanía a máximos/mínimos de rangos, gaps históricos y Anchored VWAP.
5. **Entrada asimétrica.** Buscar pullback + reclaim, undercut & rally, VCP/inside day, EP, failed breakout o rebote hacia EMA bajista; el trigger puede bajar a 1, 5, 15 o 60 minutos.
6. **Invalidez primero.** Definir el precio que invalida el setup antes de ingresar; convertirlo en acciones/posición; considerar slippage y gap de apertura.
7. **Administración de cartera.** Sumar exposición bruta y neta; medir riesgos sectoriales comunes y disponibilidad de buying power; no copiar su apalancamiento.
8. **Gestión posterior.** Permitir que el ganador se desarrolle si la tendencia no se deteriora; tomar parciales en extensiones o al alcanzar soporte contrario; no mover sistemáticamente al breakeven.
9. **Retroalimentación.** Registrar si el precio respeta el nivel inmediatamente, si aparece follow-through, si se producen stop-outs en cadena y si el régimen de mercado cambia.
10. **Auditoría semanal.** Clasificar errores de anticipación, FOMO, reentradas sin trigger, excesos de tamaño, trades omitidos y decisiones de venta prematura.

## 3. Clasificación de setups (inferencia a partir de las sesiones)

| Código | Entrada que estudiar | Invalidez / stop | Fallo que evitar |
|---|---|---|---|
| L1 — Pullback en líder | Mercado general constructivo y sector fuerte. Acción con estructura semanal alcista, retroceso hacia EMA diaria ascendente, soporte estructural, reclaim de 1/5/15min. | Mínimo del patrón o vela trigger; no colocar stop solamente por porcentaje arbitrario. | Stop-out al perder soporte; si rebota y recaptura, considerar reentrada nueva. |
| L2 — Undercut & rally | Acción o índice pierde soporte, recupera EMA/previo mínimo y aparecen líderes acompañando; buscar relación entrada-invalidación estrecha. | Mínimo de barrida o nivel que anula recuperación. | Diferenciar sweep real de tendencia bajista sostenida. |
| L3 — EP / gap + pullback | Catalizador y gap sobre resistencia; evita perseguir exceso; busca respuesta en niveles de 5/15/60min. | Mínimo intradía relevante, dependiendo de liquidez. | Volatilidad de earnings/gap puede saltar stop. |
| L4 — Base antes de breakout | Inside day, VCP, EMA comprimidas, higher lows y tema fuerte; puede anticiparse dentro de la base cuando el stop es cercano. | Base low, vela señal u otra estructura. | Alerta de oportunidad perdida si se espera siempre ruptura visible. |
| S1 — Rechazo EMA descendente | Mercado/selectivo bajista y sector débil, precio rebota hasta EMA 9/21/50/150 descendente o gap-fill/AVWAP. | Máximo de rechazo o swing high. | No vender tarde un gap bajista extendido. |
| S2 — Failed breakout / inverse EP | Estructura alcista previa falla con vela amplia, gran volumen, mecha superior, cierre bajo soporte; rebote posterior es vendido. | Máximo del fracaso o rebote de 5/15min. | Puede convertirse en verdadera recuperación; respetar stop. |
| S3 — Debilidad de líder anterior | Tema líder pierde medias y amplitud; antiguos ganadores pueden romper después de distribución. | Máximo local, EMA relevante o nivel de invalidación. | Líderes muy líquidos pueden tener squeezes violentos. |

## 4. Gestión del riesgo observada

- Diferenciar **posición nominal (% de cuenta)** de **riesgo de stop (% de cuenta)**. En los textos se mencionan posiciones individuales del orden del 20–25% y ejemplos de riesgo del orden 0,15–0,30% por trade, con excepciones, no una regla estable universal.
- Dimensionar: número de acciones = (equity × riesgo por trade)/(distancia de entrada a stop). Ejemplo: US$50.000 × 0,2% /(US$40 - US$39,20) = 125 acciones.
- Algunas sesiones describen exposición apalancada superior al 100%, incluso más de 250–300%; estos son hechos de su estilo, **no parámetros recomendados para copiar**. El riesgo de gaps e instrumentos correlacionados puede exceder los stops individuales.
- Martin afirma que rara vez pasa stops mecánicamente a breakeven; en ocasiones los mueve por estructura. También toma beneficios parciales en extensión, caídas fuertes o resistencias, y puede reentrar.
- La baja liquidez, pequeñas capitalizaciones, ADR, earnings y anuncios FOMC requieren una simulación de gaps y slippage; un stop no garantiza un precio de ejecución.

## 5. Construcción de scanners — versión investigable, NO reglas textuales exactas del operador

- Universo NASDAQ/NYSE con históricos ajustados y exclusiones de instrumentos inapropiados según el experimento.
- Indicadores diarios y semanales: EMA 9, 21, 50 y 150; máximos previos; gaps; Anchored VWAP bien definido por fecha de evento.
- Rotación sectorial: ranking de fuerza relativa del sector en 5/20/60 sesiones, dispersión y número de líderes.
- Estado de universo: categorías líderes/mediocres/rezagadas según alineación de medias y fuerza relativa; mantener historiales point-in-time para evitar survivorship bias.
- Filtros de liquidez: experimentar con >US$10M, >US$50M, >US$100M y >US$500M negociados por día; **los umbrales 100M y 500M aparecen en su organización posterior de watchlists, no como mínimos universales de toda operación**.
- Señales LONG: confluencia soporte + first pullback + reclaim intradía, y alternativas EP e inside days.
- Señales SHORT: sector débil + rally a EMA descendente/gap fill/AVWAP + rechazo + stop sobre high.
- Ranking experimental: no premia el patrón sin relación riesgo/beneficio. Penaliza distancia grande al stop, entrada demasiado extendida, bajo volumen monetario y señales contradictorias del sector.

## 6. Experimentos recomendados

1. Long con sector líder versus long idéntico en sector mediocre, manteniendo idéntico trigger y stop.
2. Short en rebote a EMA 9/21/50/150 versus short inmediatamente tras gran gap bajista.
3. Triggers de 1, 5 y 15 min con datos intradía y spread/slippage realistas.
4. Comparar stop estructural versus stop a breakeven a 1R versus salida por EMA.
5. Backtest por estados líderes/rezagados para aislar efectividad de market breadth.
6. Reingreso tras stop con confirmación versus prohibir reingresos; añadir comisiones y slippage.
7. Ganadores mantenidos hasta señal estructural versus venta de 1/3 en extensión; calcular R media y cola derecha.
8. Simulador de riesgo de cartera: gaps simultáneos, shocks sectoriales, gross exposure y margin call.

## 7. Fichas cronológicas de las 51 transcripciones adjuntas

**Convención:** J-01..J-11, JA-01..JA-20, SN-01..SN-20 siguen el orden en que los archivos fueron entregados. No implican una fecha de mercado específica. Las marcas del video son relativas al stream.

### JUNIO (11 archivos)

#### J-01 — Gap bajista y liderazgo sobreextendido
**Hallazgo:** IWM cerca de EMA 9 diaria; investiga qué sucede durante un pullback general, identifica software y ciberseguridad como líderes, y advierte sobre persecución de movimientos tardíos.
**Qué aprender:** Contexto antes de señal.
**Fuente:** `Texto pegado(20261122-030754).txt`. **Capítulos:** Cap. 2: Market outlook and strategy; Cap. 3: Identifying leading sectors; Cap. 4: Position management.

#### J-02 — Watchlist de candidatos operables
**Hallazgo:** Reduce la lista a acciones donde realmente contemplaría entrar; considera pullback hacia medias y mínimo del día como nivel de invalidación.
**Qué aprender:** Separar líder de entrada.
**Fuente:** `Texto pegado (2)(20261122-030824).txt`. **Capítulos:** Cap. 1: Market outlook and approach; Cap. 2: Trading current watchlists; Cap. 3: Managing order execution.

#### J-03 — Distribución y señales técnicas de advertencia
**Hallazgo:** Analiza NVDA y otras acciones tras reversiones, pérdida de medias y velas rojas; reflexiona sobre cómo detener el sobretrading.
**Qué aprender:** Vigilar distribución colectiva.
**Fuente:** `Texto pegado (3)(20261122-030841).txt`. **Capítulos:** Cap. 1: Market downturn analysis; Cap. 2: Technical warning signs; Cap. 3: Trading psychology advice.

#### J-04 — Mercado dividido y cortos potenciales
**Hallazgo:** Combina análisis de indicadores, sectores y grandes acciones; observa rebotes hacia resistencias sin declarar necesariamente acabado el mercado alcista.
**Qué aprender:** Evitar sesgos rígidos.
**Fuente:** `Texto pegado (4)(4).txt`. **Capítulos:** Cap. 1: Market introduction; Cap. 2: Market sentiment and strategy; Cap. 3: Individual stock analysis.

#### J-05 — Parciales en shorts y prudencia con nuevos largos
**Hallazgo:** Comenta cierres de SQQQ/QBTS y mantiene vigilancia sobre soportes importantes, pese a rebotes en algunas acciones.
**Qué aprender:** Exigir confirmación de vuelta.
**Fuente:** `Texto pegado (5)(1).txt`. **Capítulos:** Cap. 1: Market outlook and strategy; Cap. 2: Stock watchlist and analysis; Cap. 3: Trade performance review.

#### J-06 — Giro agresivo tras recuperación y falsas rupturas
**Hallazgo:** Aumenta exposición con un failed breakdown de índices, entradas dentro de rangos y stops ajustados; explica su tolerancia a múltiples intentos.
**Qué aprender:** Confluencia índice + acción + stop.
**Fuente:** `Texto pegado (6).txt`. **Capítulos:** Cap. 1: Market analysis and setups; Cap. 2: IPO and market trends; Cap. 3: Trading execution and strategy.

#### J-07 — Preparación, ejecución y restricciones de liquidez
**Hallazgo:** Reflexiona sobre su proceso de aprendizaje y trades; la calidad del punto de entrada depende de temporalidad, movimiento sectorial y liquidez.
**Qué aprender:** Registrar condiciones de ejecución.
**Fuente:** `Texto pegado (7).txt`. **Capítulos:** Cap. 1: Introduction and background; Cap. 2: Reviewing past trades; Cap. 3: Trading lifestyle.

#### J-08 — Oportunidades en días bajistas
**Hallazgo:** Busca compras de retroceso sobre EMA y máximos anteriores, estudia triggers intradía y la diferencia entre tendencia semanal sana y ruido de apertura.
**Qué aprender:** Comprar soporte confirmado, no caída ciega.
**Fuente:** `Texto pegado (8).txt`. **Capítulos:** Cap. 1: Market introduction; Cap. 2: Analyzing the morning gap; Cap. 3: Trading stance on gaps.

#### J-09 — Fortaleza de IWM y respuesta de líderes
**Hallazgo:** Discute amplitud, grado de recuperación y posibilidades de lockout rally; contrasta el miedo del mercado con la tendencia aún ascendente.
**Qué aprender:** Evaluar amplitud real.
**Fuente:** `Texto pegado (9).txt`. **Capítulos:** Cap. 1: Market outlook and analysis; Cap. 2: Trading strategy and planning; Cap. 3: Sector review and stock picks.

#### J-10 — Gestión y análisis de oportunidad
**Hallazgo:** Distingue acción fuerte de acción operable, y reconoce que la volatilidad y timing intradía condicionan el precio que se puede pagar.
**Qué aprender:** Reproducir criterios de exclusión.
**Fuente:** `Texto pegado (10).txt`. **Capítulos:** Cap. 1: Market context and review; Cap. 2: Current market opportunities; Cap. 3: Navigating market volatility.

#### J-11 — Deterioro de mercado y disciplina
**Hallazgo:** Examinar debilidad debajo de medias, stop-outs y necesidad de ajustar agresividad y exposición a las señales que entregan las operaciones.
**Qué aprender:** La pérdida también informa.
**Fuente:** `Texto pegado (11).txt`. **Capítulos:** Cap. 1: Market introduction; Cap. 2: Analyzing market weakness; Cap. 3: Trading discipline and stops.

### JULIO–AGOSTO (20 archivos)

#### JA-01 — Corning pierde calidad; salida de semiconductores
**Hallazgo:** Vende posiciones en MU/INTC/GLW al observar que Corning no rebota con energía en EMA 9; reevalúa semis y reintenta QBTS short.
**Qué aprender:** Respuesta al nivel > simple toque de EMA.
**Fuente:** `Texto pegado(20261122-033158).txt`. **Capítulos:** Cap. 1: Introduction and trading; Cap. 2: Selling semiconductor stakes; Cap. 3: Market rotation and outlook.

#### JA-02 — Regreso de viaje y transición hacia cortos
**Hallazgo:** Cierra varias posiciones largas y toma cortos al observar debilidad; comenta cansancio y necesidad de desconectar del mercado.
**Qué aprender:** No operar por obligación.
**Fuente:** `Texto pegado (2)(20261122-033211).txt`. **Capítulos:** Cap. 1: Market update introduction; Cap. 2: Holiday and trading shift; Cap. 3: Reasons for closing longs.

#### JA-03 — Rally contra resistencias bajistas
**Hallazgo:** Evalúa gaps al alza hacia EMA descendentes; desarrolla disciplina de tamaño de posición, riesgo overnight y stops.
**Qué aprender:** Short en rebote, no por caída pasada.
**Fuente:** `Texto pegado (3)(20261122-033227).txt`. **Capítulos:** Cap. 1: Market outlook; Cap. 2: Short-side trading strategy; Cap. 3: Sector analysis and trades.

#### JA-04 — Estudio técnico y watchlist tier 2
**Hallazgo:** Investiga AOI y otros sectores en EMA 150 o zonas semanales; describe universo de pequeñas empresas y el trabajo de revisar patrones anteriores.
**Qué aprender:** Distinguir soportes mayores de rebotes temporales.
**Fuente:** `Texto pegado (4)(5).txt`. **Capítulos:** Cap. 1: Market outlook; Cap. 2: Analyzing trade setups; Cap. 3: Historical context.

#### JA-05 — Selección de líderes y temas
**Hallazgo:** Revisa AMD, líderes de memoria, cripto y otros grupos; estudia si cambios de volumen y de estructura anticipan una rotación del mercado.
**Qué aprender:** Comparar fuerza relativa dentro del sector.
**Fuente:** `Texto pegado (5)(2).txt`. **Capítulos:** Cap. 1: Market scan and outlook; Cap. 2: Leading themes and analysis; Cap. 3: Crypto and tech trade setup.

#### JA-06 — Breakdowns generalizados y cierre de longs
**Hallazgo:** Cierra largos tras ver deterioro en software, fintech y nombres relacionados; incursiona en cortos y reporta stop-outs repetidos.
**Qué aprender:** Criterio de cambio de régimen.
**Fuente:** `Texto pegado (6)(1).txt`. **Capítulos:** Cap. 1: Market context and setup; Cap. 2: Analyzing market breakdowns; Cap. 3: Trading index volatility.

#### JA-07 — Reentrada SNDK y control de revenge trading
**Hallazgo:** Tras un stop vuelve a SNDK cerca de EMA diaria y EMA 150 horaria con trigger de 15 minutos; analiza cómo evitar subir el tamaño para recuperar pérdidas.
**Qué aprender:** Reentrar por nueva señal, no por frustración.
**Fuente:** `Texto pegado (7)(1).txt`. **Capítulos:** Cap. 1: Market context and morning; Cap. 2: Risk management strategies; Cap. 3: Trading current opportunities.

#### JA-08 — Preparación semanal por listas líderes/rezagadas
**Hallazgo:** Compara número de acciones líderes y rezagadas, prepara candidatos durante el fin de semana y analiza divergencias entre índices y acciones.
**Qué aprender:** La amplitud se puede contar.
**Fuente:** `Texto pegado (8)(1).txt`. **Capítulos:** Cap. 1: Market context; Cap. 2: Watchlist and strategy; Cap. 3: Market outlook and psychology.

#### JA-09 — Cobertura parcial al llegar a soportes
**Hallazgo:** Considera tomar beneficios en shorts cuando semiconductores alcanzan EMA semanales y muestra cómo el gap y la volatilidad afectan las salidas.
**Qué aprender:** No extrapolar indefinidamente una caída.
**Fuente:** `Texto pegado (9)(1).txt`. **Capítulos:** Cap. 1: Morning market analysis; Cap. 2: Short selling strategies; Cap. 3: Market decline and pressure.

#### JA-10 — Ciberseguridad y cripto como alternativas
**Hallazgo:** Tras debilidad del mercado estudia undercuts y recuperación en ciberseguridad y Ethereum; algunas partes de la transcripción están corruptas.
**Qué aprender:** Marcar evidencia incompleta.
**Fuente:** `Texto pegado (10)(1).txt`. **Capítulos:** .

#### JA-11 — Recuperación de CRWD/NET
**Hallazgo:** Explica posiciones en software, weekly EMA 9 y recuperación de medias; observa cómo la primera reacción sobre soporte puede cambiar un sesgo.
**Qué aprender:** Primeras señales de nuevo liderazgo.
**Fuente:** `Texto pegado (11)(1).txt`. **Capítulos:** Cap. 1: Market context and intro; Cap. 2: Review of current positions; Cap. 3: Cryptocurrency market outlook.

#### JA-12 — Gaps alcistas: paciencia en lugar de persecución
**Hallazgo:** No compra simplemente porque SPY hace gap o varios títulos suben; prefiere una retirada que permita un stop más definido.
**Qué aprender:** Precio de entrada importa.
**Fuente:** `Texto pegado (12).txt`. **Capítulos:** Cap. 1: Market context introduction; Cap. 2: Pre-market stock analysis; Cap. 3: Current market leadership.

#### JA-13 — Varios gaps consecutivos; evaluación de EP
**Hallazgo:** Analiza Episodic Pivots y aperturas fuertes tras una sucesión de gaps del índice; reconoce riesgos de comprar al final de una aceleración.
**Qué aprender:** Separar catalizador de precio pagado.
**Fuente:** `Texto pegado (13).txt`. **Capítulos:** Cap. 1: Market overview and stocks; Cap. 2: Trading reflection; Cap. 3: Analyzing stock setups.

#### JA-14 — Earnings bajistas, semis y centros de datos
**Hallazgo:** Detecta acciones rebotando hacia resistencias semanales o EMA descendentes, y estudia fallos de rupturas para posibles shorts.
**Qué aprender:** Rebote hacia oferta.
**Fuente:** `Texto pegado (14).txt`. **Capítulos:** Cap. 1: Market outlook analysis; Cap. 2: Trading strategy and focus; Cap. 3: Technical setups and trades.

#### JA-15 — Rutina de scanning completa y jerarquías
**Hallazgo:** Muestra cómo revisa primero su lista existente, después screeners; separa pequeñas capitalizaciones y liquidez diaria, y explica por qué algunas compras se hacen sobre pullback.
**Qué aprender:** Convertir watchlist en proceso reproducible.
**Fuente:** `Texto pegado (15).txt`. **Capítulos:** Cap. 1: Watchlist management; Cap. 2: Market tiers and strategy; Cap. 3: Identifying trade setups.

#### JA-16 — Reaceleración y exceso de exposición
**Hallazgo:** Más de treinta acciones subiendo en premarket; algunos índices consolidan sin alcanzar EMA 9, pero reconoce restricciones de buying power.
**Qué aprender:** Fuerza no elimina riesgo de cartera.
**Fuente:** `Texto pegado (16).txt`. **Capítulos:** Cap. 1: Market introduction; Cap. 2: Stock analysis and outlook; Cap. 3: Market strength assessment.

#### JA-17 — Gap adverso y stops en intradía
**Hallazgo:** Discute un gap grande en CPRS, condiciones de liquidez y selección del mínimo de vela como stop en algunas operaciones.
**Qué aprender:** Modelar gap risk.
**Fuente:** `Texto pegado (17).txt`. **Capítulos:** Cap. 1: Market outlook and analysis; Cap. 2: Trading specific stocks; Cap. 3: Pullback trading strategies.

#### JA-18 — Cripto y primer rango de apertura
**Hallazgo:** Estudia reclaims semanales de quantum y realiza compras de ruptura en temporalidad de 1 minuto; evalúa stops y capital disponible.
**Qué aprender:** Trigger intradía en tesis semanal.
**Fuente:** `Texto pegado (18).txt`. **Capítulos:** Cap. 1: Market overview and intro; Cap. 2: Crypto and market analysis; Cap. 3: Trading strategy and focus.

#### JA-19 — Mercado mezclado y costo de estar mirando
**Hallazgo:** Reflexiona sobre ausencias por compromisos y la conveniencia de no operar cuando señales son poco claras; estudia reacción sectorial.
**Qué aprender:** Estar fuera es una decisión.
**Fuente:** `Texto pegado (19).txt`. **Capítulos:** Cap. 1: Market outlook and sentiment; Cap. 2: Trading absence and lessons; Cap. 3: Crypto trading review.

#### JA-20 — Software resistente frente a semis débiles
**Hallazgo:** Un gap de semiconductores hacia resistencia contrasta con fortaleza de otras áreas; revisa su escaneo de sectores y operaciones de biotecnología.
**Qué aprender:** Hacer pares sectoriales, no generalizar.
**Fuente:** `Texto pegado (20).txt`. **Capítulos:** Cap. 1: Market introduction; Cap. 2: Market gap analysis; Cap. 3: Sector sentiment.

### SEPTIEMBRE–NOVIEMBRE (20 archivos)

#### SN-01 — Gestión short y escenarios de rebote
**Hallazgo:** Planifica cubrir parcialmente en debilidad o vender el rebote en resistencia; no agrega shorts por inercia después de una caída.
**Qué aprender:** Plan de dos escenarios antes de apertura.
**Fuente:** `Texto pegado(20261122-034401).txt`. **Capítulos:** Cap. 1: Market outlook and strategy; Cap. 2: Analyzing market conditions; Cap. 3: Trade selection and execution.

#### SN-02 — Revisión de SNDK y tamaño por stop
**Hallazgo:** Observa apertura fuerte en índices con semis selectivamente débiles; discute precálculo de posiciones y por qué el contexto convierte a SNDK en short.
**Qué aprender:** La operación nace del contexto.
**Fuente:** `Texto pegado (2)(20261122-034427).txt`. **Capítulos:** Cap. 1: Market opening overview; Cap. 2: Sector and stock analysis; Cap. 3: Trading strategy and outlook.

#### SN-03 — Descanso obligatorio por exceso de agresividad
**Hallazgo:** Se impone un día sin operar tras notar estrés, impulsividad y operaciones de calidad decreciente; observa el mercado sin ejecutar.
**Qué aprender:** Regla psicológica de bloqueo.
**Fuente:** `Texto pegado (3)(20261122-034453).txt`. **Capítulos:** Cap. 1: Introduction; Cap. 2: Rest day discipline; Cap. 3: Market observation.

#### SN-04 — Costes ADR y entradas demasiado anticipadas
**Hallazgo:** Detecta prima aparente de ADR de SK Hynix, analiza stops, metales y operaciones que había anticipado antes de obtener confirmación.
**Qué aprender:** Considerar instrumentos, spreads y timing.
**Fuente:** `Texto pegado (4)(6).txt`. **Capítulos:** Cap. 1: Market context and intro; Cap. 2: ADR premiums and early entry; Cap. 3: Precious metals and learning.

#### SN-05 — Software y ciberseguridad muestran fuerza relativa
**Hallazgo:** Compara fortaleza del software con ventas en semis; revisa shorts y el riesgo de permanecer sesgado pese a señales contrarias.
**Qué aprender:** Distinguir liderazgo y debilidad coexistentes.
**Fuente:** `Texto pegado (5)(3).txt`. **Capítulos:** Cap. 1: Market outlook and analysis; Cap. 2: Shorting strategy; Cap. 3: Sector strength analysis.

#### SN-06 — FOMC y episodio 100
**Hallazgo:** Opera con decisiones de tasas a punto de conocerse; discute riesgos de velas súbitas y exposición al anunciarse noticias macro.
**Qué aprender:** Añadir régimen de eventos a la simulación.
**Fuente:** `Texto pegado (6)(2).txt`. **Capítulos:** Cap. 1: Market context and Fed news; Cap. 2: Analyzing market index trends; Cap. 3: Sector strength and laggards.

#### SN-07 — Gap violento contra los cortos
**Hallazgo:** Sufre reacción alcista adversa en cortos, comenta reducción de riesgo por trade respecto de años anteriores y riesgo de stops ajustados.
**Qué aprender:** No confundir stop ajustado con control del gap.
**Fuente:** `Texto pegado (7)(2).txt`. **Capítulos:** .

#### SN-08 — Reorganización de watchlists por liquidez
**Hallazgo:** Elimina tier 2 como lista separada; reordena líderes, mediocres y rezagadas por dos segmentos de volumen monetario y explica entradas de 1 minuto.
**Qué aprender:** Clasificación dinámica reproducible.
**Fuente:** `Texto pegado (8)(2).txt`. **Capítulos:** Cap. 1: Market context and strategy; Cap. 2: Market outlook and setup; Cap. 3: Trade management insights.

#### SN-09 — Cierra largos demasiado pronto y reabre cortos
**Hallazgo:** Tras un período sin streams reconoce haber vendido PLTR prematuramente porque le cuesta gestionar simultáneamente posiciones largas y cortas con margen.
**Qué aprender:** Hedge de cartera también requiere capacidad.
**Fuente:** `Texto pegado (9)(2).txt`. **Capítulos:** Cap. 1: Trading update and strategy; Cap. 2: Transitioning to short positions; Cap. 3: Diving trip and focus.

#### SN-10 — Cerrar shorts al alcanzar soporte
**Hallazgo:** Reduce cortos que llegan a gaps históricos, soportes y extensión bajista; considera reshort si hay un rebote nuevo.
**Qué aprender:** Tomar beneficio no exige cambiar la tesis.
**Fuente:** `Texto pegado (10)(2).txt`. **Capítulos:** Cap. 1: Market introduction; Cap. 2: Short position strategy; Cap. 3: USOIL and market analysis.

#### SN-11 — Riesgo overnight y menor tamaño en pequeñas empresas
**Hallazgo:** Explica que un stop no puede eliminar el riesgo de apertura y que ajusta a la baja la posición en small caps poco líquidas.
**Qué aprender:** Agregar riesgo de gap/liquidez.
**Fuente:** `Texto pegado (11)(2).txt`. **Capítulos:** Cap. 1: Introduction; Cap. 2: Overnight risk management; Cap. 3: Market context and streaming.

#### SN-12 — Short en metales, petróleo y mercado mixto
**Hallazgo:** Estudia debilidad de índices, movimientos de plata/oro y exposición cruzada, reconociendo incertidumbre de corto plazo.
**Qué aprender:** Correlaciones entre activos.
**Fuente:** `Texto pegado (12)(1).txt`. **Capítulos:** Cap. 1: Market overview and sentiment; Cap. 2: Trading silver and oil; Cap. 3: Risk management and strategy.

#### SN-13 — Volatilidad y reentradas bajo presión
**Hallazgo:** En mercado muy volátil evalúa haber entrado demasiado pronto y el daño potencial de un gap contra la cartera short.
**Qué aprender:** La calidad del trade empeora con el apuro.
**Fuente:** `Texto pegado (13)(1).txt`. **Capítulos:** Cap. 1: Market outlook and analysis; Cap. 2: Crypto and sector overview; Cap. 3: Trading strategy and risk.

#### SN-14 — Ejemplos de gap overnight extremo
**Hallazgo:** Revisa shocks en acciones fuera de horario y una experiencia histórica con stop no colocado físicamente.
**Qué aprender:** El riesgo exógeno no cabe en el stop teórico.
**Fuente:** `Texto pegado (14)(1).txt`. **Capítulos:** .

#### SN-15 — MSTR y aprendizaje del lado short
**Hallazgo:** Trata movimientos de MSTR y valores extendidos; discute cuándo intentar shorts y cómo evitar perseguir caídas desarrolladas.
**Qué aprender:** Esperar rebote de baja volatilidad.
**Fuente:** `Texto pegado (15)(1).txt`. **Capítulos:** .

#### SN-16 — No duplicar shorts por convicción
**Hallazgo:** Ante rebotes contra EMA bajistas reconoce que la exposición corta ya es suficiente y evita doblar posiciones sin mejorar relación riesgo/beneficio.
**Qué aprender:** Límites de riesgo agregado.
**Fuente:** `Texto pegado (16)(1).txt`. **Capítulos:** .

#### SN-17 — Ganancias vs. eventos de resultados
**Hallazgo:** Reduce UVXY y algunas posiciones short ante earnings relevantes; compara entrada en EMA, gap fill y criterios de volumen.
**Qué aprender:** Controlar calendario de catalizadores.
**Fuente:** `Texto pegado (17)(1).txt`. **Capítulos:** .

#### SN-18 — Leader scan mensual y nueva selección
**Hallazgo:** Ejecuta cada fin de semana ranking por rendimiento mensual; detecta software, biotecnología, energía y retail, e identifica mejores candidatos para estudiar.
**Qué aprender:** Scanner de momentum por ranking.
**Fuente:** `Texto pegado (18)(1).txt`. **Capítulos:** Cap. 1: Market overview; Cap. 2: Market leader scans; Cap. 3: Sector analysis and strategy.

#### SN-19 — Riesgo ultrapequeño en oportunidades experimentales
**Hallazgo:** Discute stops de 5/15 minutos, volatilidad de ETFs apalancados y un ejemplo de riesgo por cuenta excepcionalmente bajo.
**Qué aprender:** Riesgo variable según oportunidad.
**Fuente:** `Texto pegado (19)(1).txt`. **Capítulos:** Cap. 1: Introduction; Cap. 2: Market overview and analysis; Cap. 3: Reviewing trade positions.

#### SN-20 — Mercado todavía selectivo; longs y shorts
**Hallazgo:** Considera largos puntuales mientras conserva cortos, vende CRWD y admite que algunas reversiones podrían requerir abandonar la tesis bajista.
**Qué aprender:** Operar flexible, no sostener narrativa.
**Fuente:** `Texto pegado (20)(1).txt`. **Capítulos:** Cap. 1: Market outlook and strategy; Cap. 2: Reviewing past trades; Cap. 3: CrowdStrike trading analysis.

### Sesiones adicionales pegadas directamente en el chat

#### CHAT-JA-01 — Sesión adicional julio/agosto
Tras rebote en software, abre cuatro nuevas posiciones y espera reacción de índices en soportes. Prefiere comprar durante recuperación de EMA frente a perseguir máximos.
**Marcas útiles:** 25:40; 29:47. Fecha exacta no confirmada.

#### CHAT-JA-02 — Sesión adicional julio/agosto
Compara software alcista con semiconductores débiles; evalúa shorts en quantum y semis, stops y errores de ejecución. Explica sesgos y cambios sectoriales.
**Marcas útiles:** 1:21:29; 2:19:20; 2:54:15. Fecha exacta no confirmada.

#### CHAT-JA-03 — Sesión adicional julio/agosto
Se concentra en shorts de semis; explica watchlists por EMA, tamaño de posiciones 20–25%, diferencia entre stop en precio y riesgo de cartera, y motivos para no mover a breakeven.
**Marcas útiles:** 2:24:50; 2:30:56; 2:36:57. Fecha exacta no confirmada.

#### CHAT-JA-04 — Sesión adicional julio/agosto
Examina bajo desempeño de IWM frente a QQQ/SPY, extensión de software y dificultad de replicar con solo gráficos; enfatiza revisar cientos de gráficos y traders verificables.
**Marcas útiles:** 1:39:03; 1:47:23; 2:03:19. Fecha exacta no confirmada.

#### CHAT-SN-01 — Sesión adicional septiembre/noviembre
En gap bajista evita perseguir shorts: espera rebotes hacia EMA descendentes; identifica debilidad semis, busca confirmación sectorial y prefiere terminar temprano para evitar operar sin setup.
**Marcas útiles:** 6:52; 9:21; 17:55; 32:31. Fecha exacta no confirmada.

## 8. Matriz de evidencia y límites

| Nivel | Afirmación |
|---|---|
| Directo | Martin usa EMA y Anchored VWAP en varias temporalidades; busca concentración de fuerza relativa en sectores y entradas con stops relativamente cercanos. |
| Directo | Explica que sus listados de líderes, mediocres y rezagados evolucionan, que revisa charts de fin de semana y que estudia sus errores. |
| Reconstrucción | Los estados cuantitativos de mercado, indicadores score, filtros exactos de momentum y fórmulas de ranking son nuestras propuestas para probar, no su código exacto. |
| No confirmado | Fechas de cada stream, totales de todas las entradas y salidas, fill prices, P&L histórico, estadísticas auditadas y reproducibilidad del rendimiento. |

## 9. Ruta de entrenamiento para replicar

- Semana 1: clasificar a mano 100 gráficos de líderes y rezagados según régimen, con fechas y sin mirar lo que ocurrió después.
- Semana 2: construir scanner de volumen monetario, fuerza relativa, trend EMAs y distancia a soporte/resistencia.
- Semana 3: replay intradía de 30–50 casos LONG y 30–50 casos SHORT con observación de cambios a 1/5/15 minutos.
- Semana 4: backtesting fuera de muestra, costes de ejecución, falsos positivos, distribuciones de R y exposición sectorial.
- Semana 5: simulación sin dinero real con journal de decisiones, incluido cada trade que se omite y por qué.
- Semana 6: si hay evidencia suficiente, validar con tamaño mínimo bajo límites de pérdida diarios y semanales predeterminados.

## 10. Registro mínimo de cada operación
fecha, hora ET, símbolo, sector, régimen de índices, ranking de líderes, setup, temporalidad, señal, entrada prevista, fill real, stop, volumen negociado, spread, tamaño, riesgo inicial, riesgo overnight, exposición conjunta, salida, R realizada, MFE, MAE, comisiones/slippage, comentario y captura.

## 11. Hallazgo que merece mayor atención
La **adaptación del riesgo según la calidad y el contexto** puede explicar más de su resultado que una señal visual concreta. La comprobación requiere separar decisiones exitosas y fallidas, sin seleccionar únicamente operaciones memorables.
