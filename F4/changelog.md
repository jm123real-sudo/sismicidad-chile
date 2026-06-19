Changelog — Proyecto Sismicidad Chile
Todos los cambios relevantes del proyecto están documentados aquí.
Formato basado en Keep a Changelog.
---
[F4] — 2026-06-15
Added
`F4/F4_Integracion.ipynb`: notebook integrador que reutiliza el pipeline F1–F3
y presenta 3 visualizaciones analíticas con storytelling
`F4/changelog.md`: trazabilidad de mejoras por fase
Visualización 1: mapa geográfico de sismos coloreado por magnitud
Visualización 2: boxplot distribución de magnitud por profundidad focal
Visualización 3: serie temporal de sismos ≥ 6.0 (2014–2024) con eje dual
Secciones de resultados, discusión, limitaciones y conclusiones en el notebook
Changed
`figures/`: gráficos de F4 exportados a esta carpeta compartida
`README.md`: actualizado con estado F4 completado e instrucciones de F4
---
[F3] — 2026-06-14
Added
`F3/src/orquestador.py`: clase `Pipeline` orquestadora (composición + polimorfismo)
`F3/src/transformadores.py`: clase abstracta `Transformador` con subclases
`ClasificadorMagnitudAlta`, `ClasificadorProfundidad`, `NormalizadorMinMax`
`F3/src/pipeline.py`: clases `AnalizadorSismicoBase` y `AnalizadorSismicoAvanzado`
con encapsulamiento (`_df`), herencia y polimorfismo en `resumen()`
`F3/README_F3.md`: documentación técnica de la arquitectura de F3
`F3/resultados/metricas_eficiencia.csv`: benchmarks timeit exportados
Fixed
Encapsulamiento corregido: `self.df` → `self._df` con `@property datos`
Clases duplicadas eliminadas del notebook (celdas 22–26 obsoletas)
Celda `!pip install pandas` con output local eliminada
Celda 27 convertida de Markdown a código (generación del CSV de métricas)
Error de indentación en `resumen()` de `AnalizadorSismicoAvanzado`
Conflictos de merge resueltos via Git Bash (no editor web)
---
[F2] — 2026-06-10
Added
`F2/F2_limpieza.ipynb`: pipeline completo de limpieza con funciones modulares
`data/processed/seismic_data_clean.csv`: dataset limpio con 14 columnas
Clase `DatasetInspector` para diagnóstico de calidad
Funciones: `cargar_datos`, `eliminar_duplicados`, `convertir_fecha`,
`clasificar_profundidad`, `clasificar_magnitud`, `normalizar_minmax`, `exportar_datos`
Variables derivadas: `Year`, `Month`, `Day`, `Hour`, `DayOfWeek`,
`Depth_Category`, `Magnitude_Category`, `Depth_norm`, `Magnitude_norm`
Validaciones con `assert` (8 comprobaciones)
Fixed
Ruta del CSV corregida de `../seismic_data.csv` a `../../data/raw/seismic_data.csv`
Rango de latitud ajustado a -63° (el dataset tiene registros en -62.35°)
Error de indentación en función `validar_dataset`
---
[F1] — 2026-06-05
Added
Estructura modular del repositorio: `F1/`, `F2/`, `F3/`, `F4/`,
`data/raw/`, `data/processed/`, `src/`, `figures/`
`F1/F1_Definicion.ipynb`: definición del problema, exploración inicial
y clase `DatasetInspector`
`.venv` y `requirements.txt` con versiones exactas (`pip freeze`)
`.gitignore` configurado (excluye `.venv/`, checkpoints, dataset)
`README.md` con instrucciones de reproducibilidad
Flujo de trabajo Git: ramas por integrante + PR → revisión → merge a main
Changed
Estructura de carpetas mejorada respecto al mapa conceptual original:
se adoptó separación por fase (F1–F4) en vez de `notebooks/` único
para facilitar trabajo paralelo y trazabilidad individual
---
Tabla comparativa de mejoras F1–F4
Aspecto	F1	F2	F3	F4
Estructura del repo	Carpetas F1–F4 creadas	F2 con notebook	F3 con src/ modular	F4 con visualizaciones
Dataset	Carga inicial	Limpieza completa	Transformaciones POO	Dataset listo para graficar
Código	Funciones básicas	Pipeline modular	POO: herencia + polimorfismo	Funciones de visualización
Validaciones	`DatasetInspector`	8 `assert`	Casos normal/límite/excepción	Validación integrada
Documentación	README + docstrings	Markdown en celdas	Docstrings en clases	Storytelling en markdown
Visualizaciones	Dispersión geográfica básica	Distribución de profundidades	—	3 gráficos analíticos con hallazgos
Git	Ramas por integrante	PRs con revisión	Merge conflicts resueltos	Changelog + README final
