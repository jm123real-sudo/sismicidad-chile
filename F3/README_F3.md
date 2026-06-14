# Fase 3 – Núcleo Algorítmico, Eficiencia Computacional y Programación Orientada a Objetos

## Proyecto

**Análisis de Sismicidad en Chile**

Este entregable corresponde a la Fase 3 del proyecto desarrollado en el Magíster en Ciencia de Datos e Inteligencia Artificial, enfocado en el análisis de eventos sísmicos registrados en Chile.

Durante esta fase se implementa un núcleo algorítmico modular que permite procesar información sísmica utilizando técnicas de programación estructurada, algoritmos recursivos, programación orientada a objetos (POO) y análisis de eficiencia computacional.

El objetivo es construir componentes reutilizables, mantenibles y escalables que sirvan como base para futuras etapas de modelamiento y análisis avanzado.

---

## Objetivos de la Fase 3

### Objetivo General

Desarrollar una solución modular para el análisis de eventos sísmicos mediante la implementación de algoritmos, estructuras orientadas a objetos y mecanismos de evaluación de eficiencia computacional.

### Objetivos Específicos

- Implementar algoritmos de procesamiento de datos utilizando programación estructurada.
- Aplicar recursividad mediante algoritmos de ordenamiento.
- Diseñar clases reutilizables utilizando Programación Orientada a Objetos.
- Incorporar mecanismos de herencia y polimorfismo.
- Implementar transformadores especializados para enriquecer la información sísmica.
- Comparar enfoques de procesamiento para evaluar rendimiento computacional.
- Generar métricas objetivas de eficiencia para apoyar decisiones de diseño.

---

## Dataset Utilizado

Para esta fase se utiliza el conjunto de datos limpio generado en la Fase 2:

```text
data/processed/seismic_data_clean.csv
```

El dataset contiene registros históricos de eventos sísmicos ocurridos en Chile e incluye variables relevantes para el análisis, tales como:

- Fecha del evento
- Latitud
- Longitud
- Profundidad (Depth)
- Magnitud (Magnitude)
- Región asociada
- Otras variables derivadas obtenidas durante la limpieza de datos

El conjunto utilizado contiene aproximadamente 4.015 registros válidos listos para procesamiento analítico.

---

## Estructura de la Fase 3

```text
F3/
│
├── F3_Nucleo_Algoritmico.ipynb
├── README_F3.md
│
├── resultados/
│   └── metricas_eficiencia.csv
│
└── src/
    ├── algoritmos.py
    ├── pipeline.py
    ├── preprocesador.py
    └── transformadores.py
```

### Descripción de Componentes

| Archivo | Descripción |
|----------|-------------|
| algoritmos.py | Implementa algoritmos recursivos para procesamiento y ordenamiento de datos. |
| preprocesador.py | Contiene funciones de carga, exploración y filtrado de eventos sísmicos. |
| pipeline.py | Implementa clases orientadas a objetos utilizando herencia y polimorfismo. |
| transformadores.py | Define transformadores para clasificación de magnitudes y profundidades. |
| metricas_eficiencia.csv | Almacena resultados obtenidos en las pruebas de rendimiento computacional. |
| F3_Nucleo_Algoritmico.ipynb
---

## Algoritmos Implementados

### Merge Sort Recursivo

Dentro del módulo `algoritmos.py` se implementa el algoritmo Merge Sort, un método de ordenamiento basado en la estrategia Divide y Vencerás.

El algoritmo divide recursivamente una lista en dos mitades hasta obtener sublistas de un elemento. Posteriormente, dichas sublistas son combinadas manteniendo el orden de los elementos.

### Justificación

Se seleccionó Merge Sort debido a que:

- Utiliza recursividad de forma natural.
- Presenta un rendimiento estable.
- Es ampliamente utilizado como referencia académica para estudiar complejidad computacional.
- Permite demostrar conceptos fundamentales de diseño algorítmico.

### Complejidad Temporal

| Caso | Complejidad |
|--------|------------|
| Mejor caso | O(n log n) |
| Caso promedio | O(n log n) |
| Peor caso | O(n log n) |

### Complejidad Espacial

```text
O(n)
```

debido al almacenamiento temporal utilizado durante la etapa de combinación.

---

## Programación Orientada a Objetos

La solución incorpora Programación Orientada a Objetos (POO) para encapsular la lógica de análisis sísmico y favorecer la reutilización de código.

### Clase Base

```text
AnalizadorSismicoBase
```

Responsabilidades:

- Almacenar el DataFrame.
- Entregar métricas generales.
- Calcular cantidad de registros.
- Obtener magnitud máxima observada.

### Clase Derivada

```text
AnalizadorSismicoAvanzado
```

Extiende la funcionalidad de la clase base incorporando:

- Profundidad promedio.
- Magnitud promedio.
- Cantidad de sismos ---

## Eficiencia Computacional

Uno de los objetivos de esta fase consiste en evaluar el rendimiento de distintas estrategias de procesamiento de datos. Para ello se realizaron pruebas de ejecución utilizando estructuras de programación tradicionales y algoritmos recursivos.

### Algoritmo de Ordenamiento Implementado

Se implementó el algoritmo **Merge Sort**, el cual utiliza una estrategia de división y conquista para ordenar listas de magnitudes sísmicas.

Características principales:

- Implementación recursiva.
- Divide el problema en subproblemas más pequeños.
- Combina resultados parciales ordenados.
- Mantiene un rendimiento estable para grandes volúmenes de datos.

### Complejidad Temporal

| Caso | Complejidad |
|--------|------------|
| Mejor caso | O(n log n) |
| Caso promedio | O(n log n) |
| Peor caso | O(n log n) |

### Complejidad Espacial

| Recurso | Complejidad |
|----------|------------|
| Memoria adicional | O(n) |

### Resultados Obtenidos

Las mediciones fueron almacenadas en:

```text
F3/resultados/metricas_eficiencia.csv
---

## Transformadores Especializados

Para enriquecer el análisis sísmico se implementó una arquitectura basada en transformadores reutilizables. Estos componentes permiten modificar o complementar la información contenida en el dataset sin alterar la estructura original de los datos.

### Clase Base: TransformadorMagnitud

La clase base define una interfaz común para todos los transformadores del proyecto mediante el método:

```python
aplicar(df)
```

Este método debe ser implementado por cualquier clase derivada, asegurando consistencia y extensibilidad en la arquitectura.

### ClasificadorMagnitudAlta

Este transformador identifica eventos sísmicos considerados fuertes utilizando un umbral configurable.

Parámetros:

- Umbral por defecto: 6.0
- Variable utilizada: Magnitude

Resultado:

Genera una nueva columna llamada:

```text
sismo_fuerte
```

donde:

- True → magnitud igual o superior al umbral.
- False → magnitud inferior al umbral.

### ClasificadorProfundidad

Este transformador clasifica automáticamente cada evento sísmico según su profundidad.

Categorías implementadas:

| Profundidad | Categoría |
|------------|------------|
| Menor a 70 km | Superficial |
| Entre 70 y 300 km | Intermedio |
| Mayor a 300 km | Profundo |

Resultado:

Se genera la variable:

```text
Categoria_Profundidad
```

que permite realizar análisis segmentados según el comportamiento geológico de los eventos sísmicos.

### Beneficios del Diseño Implementado

- Reutilización de código.
- Separación de responsabilidades.
- Fácil mantenimiento.
- Escalabilidad para futuras fases.
- Compatibilidad con nuevos transformadores.

---

## Conclusiones

Durante la Fase 3 se logró desarrollar un núcleo algorítmico modular para el análisis de eventos sísmicos en Chile, incorporando conceptos fundamentales de programación estructurada, algoritmos recursivos, Programación Orientada a Objetos (POO) y evaluación de eficiencia computacional.

Los resultados obtenidos demuestran que la arquitectura propuesta permite organizar el código en componentes reutilizables y escalables, facilitando el mantenimiento y la incorporación de nuevas funcionalidades en etapas posteriores del proyecto.

La implementación de Merge Sort permitió aplicar recursividad y analizar complejidad algorítmica, mientras que el uso de herencia y polimorfismo favoreció una estructura orientada a objetos más flexible y extensible.

Por otra parte, los transformadores especializados permitieron enriquecer el conjunto de datos mediante nuevas variables derivadas asociadas a magnitud y profundidad, aportando valor analítico para futuras etapas de modelado.

Finalmente, esta fase establece una base técnica sólida para la Fase 4, donde se abordarán técnicas de modelado y evaluación predictiva utilizando los datos procesados y las estructuras desarrolladas en esta etapa.fuertes.
- Métricas complementarias para análisis exploratorio.
 | Notebook principal que integra y valida todos los componentes desarrollados. |