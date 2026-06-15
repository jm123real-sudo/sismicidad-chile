Fase 3 — Núcleo Algorítmico, Eficiencia y POO
Proyecto
Análisis de sismicidad en Chile.
Objetivo
Desarrollar un núcleo algorítmico modular para analizar eventos sísmicos
utilizando programación estructurada, recursividad, programación
orientada a objetos y mediciones de eficiencia computacional.
Dataset utilizado
Se utiliza el archivo `data/processed/seismic_data_clean.csv`, generado
en la Fase 2 (`F2/F2_limpieza.ipynb`), compuesto por registros sísmicos
con las variables:
Date(UTC), Latitude, Longitude, Depth, Magnitude
Variables derivadas de F2: Year, Month, Day, Hour, DayOfWeek,
Depth_Category, Magnitude_Category, Depth_norm, Magnitude_norm
Estructura F3
```
F3/
├── F3_Nucleo_Algoritmico.ipynb
├── README_F3.md
├── resultados/
│   └── metricas_eficiencia.csv
└── src/
    ├── algoritmos.py        # merge_sort (recursividad)
    ├── pipeline.py           # AnalizadorSismicoBase / Avanzado (POO, herencia, polimorfismo)
    ├── transformadores.py    # Transformador (abstracta) y subclases (polimorfismo)
    └── orquestador.py        # Pipeline: ejecuta una lista de transformadores en orden
```
Arquitectura — componente → responsabilidad
Componente	Responsabilidad
`algoritmos.py`	Algoritmo recursivo (merge sort) para ordenar magnitudes
`pipeline.py`	Clases `AnalizadorSismicoBase` y `AnalizadorSismicoAvanzado`: encapsulan el dataset (`_df`) y exponen estadísticos mediante métodos públicos
`transformadores.py`	Clase abstracta `Transformador` y subclases `ClasificadorMagnitudAlta`, `ClasificadorProfundidad`, `NormalizadorMinMax`
`orquestador.py`	Clase `Pipeline`: recibe una lista de transformadores y los ejecuta en orden sobre el DataFrame
Cómo ejecutar
```bash
source .venv/Scripts/activate
jupyter lab
```
Abrir `F3/F3_Nucleo_Algoritmico.ipynb` y ejecutar Kernel → Restart & Run All.
El notebook importa las clases desde `src/` (no las redefine), por lo
que el código fuente y la demostración en el notebook están siempre
sincronizados.
Decisiones técnicas
Se mantiene `_df` como atributo protegido en todas las clases que
encapsulan el DataFrame, exponiendo el acceso mediante la propiedad
`datos` o métodos específicos (encapsulamiento).
`ClasificadorProfundidad` reutiliza los mismos límites (70 km, 300 km)
definidos en F2 para mantener coherencia entre fases.
El `Pipeline` no conoce el tipo concreto de cada transformador: solo
invoca `aplicar(df)`, lo que permite agregar nuevas transformaciones
sin modificar la clase orquestadora (principio abierto/cerrado).fuertes.
- Métricas complementarias para análisis exploratorio.
 | Notebook principal que integra y valida todos los componentes desarrollados. |