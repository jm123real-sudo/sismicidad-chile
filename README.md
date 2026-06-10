# 🌎 Proyecto de Ciencia de Datos Reproducible: Sismicidad en Chile
### Magíster en Ciencia de Datos e Inteligencia Artificial · Metodología CRISP-DM

---

## 📋 Descripción

Proyecto de análisis de datos sísmicos históricos de Chile basado en registros del Centro Sismológico Nacional (CSN). Se aplica la metodología CRISP-DM para identificar patrones espacio-temporales y caracterizar zonas de riesgo sísmico a lo largo del territorio nacional.

**Dataset:** `seismic_data.csv` · Centro Sismológico Nacional / Kaggle · 2012–Presente

---

## 👥 Integrantes

| Integrante | Rama de trabajo |
|-----------|----------------|
| José Miguel Serrano | `feature/F1` |
| Jesús Fernández Urbaneja | `feature/modelado` |
| Osvaldo Rodrigo Moncada Peralta | `feature-documentacion` |
| Evelyn Andrea Andrade Cárdenas | `feature/eda` |

---

## 📁 Estructura del repositorio

```
sismicidad-chile/
│
├── data/
│   ├── raw/                          # Dataset original — NO modificar
│   │   └── seismic_data.csv
│   └── processed/                    # Datos limpios generados en F2
│       └── seismic_data_clean.csv
│
├── F1/                               # Fase 1: Definición del problema
│   └── F1_Definicion.ipynb
│
├── F2/                               # Fase 2: Limpieza de datos
│   ├── F2_limpieza.ipynb
│
├── F3/                               # Fase 3: Análisis exploratorio
│
├── F4/                               # Fase 4: Modelado
│
├── src/                              # Módulos Python reutilizables
├── figures/                          # Gráficos exportados por los notebooks
├── requirements.txt                  # Dependencias del entorno con versiones fijadas
├── .gitignore
└── README.md
```

> **Nota:** La estructura de carpetas por fase (F1/, F2/, F3/, F4/) fue adoptada como mejora respecto al mapa conceptual original que usaba una carpeta `notebooks/` única. Esta decisión técnica facilita el trabajo paralelo entre integrantes y la trazabilidad por fase.

---

## ⚙️ Cómo reproducir el entorno

### 1. Clonar el repositorio

```bash
git clone https://github.com/jm123real-sudo/sismicidad-chile.git
cd sismicidad-chile
```

### 2. Crear y activar entorno virtual

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar los notebooks

```bash
jupyter lab
```

Orden de ejecución recomendado:

| Paso | Notebook | Descripción |
|------|----------|-------------|
| 1 | `F1/F1_Definicion.ipynb` | Definición del problema y exploración inicial |
| 2 | `F2/F2_limpieza.ipynb` | Limpieza y preparación del dataset |

En cada notebook: **Kernel → Restart & Run All** para ejecutar desde cero.

### 5. Outputs generados automáticamente

- `data/processed/seismic_data_clean.csv` — dataset limpio (generado por F2)
- `figures/F2_distribucion_profundidad.png` — gráfico de profundidades (generado por F2)

---

## 🔀 Flujo de trabajo con Git

```
main
 ├── feature/eda              → F3: análisis exploratorio y visualizaciones
 ├── feature/modelado         → F4: modelado y evaluación
 └── feature-documentacion    → documentación técnica
```

```bash
# Cada integrante trabaja en su rama
git checkout -b feature/eda

# Commits descriptivos y frecuentes
git add .
git commit -m "F3: agrega visualización de distribución temporal de sismos"
git push origin feature/eda

# Pull Request → revisión grupal → merge aprobado → main
```

---

## 📊 Estado del proyecto

| Fase | Carpeta | CRISP-DM | Estado |
|------|---------|----------|--------|
| F1 | `F1/` | Comprensión del negocio + datos | ✅ Completado |
| F2 | `F2/` | Preparación de los datos | ✅ Completado |
| F3 | `F3/` | Análisis exploratorio | ⏳ Pendiente |
| F4 | `F4/` | Modelado + Evaluación | ⏳ Pendiente |

---

## 📚 Dependencias principales

Ver `requirements.txt` para la lista completa con versiones fijadas.

- Python 3.10+
- pandas 3.0.3
- numpy 2.4.6
- matplotlib 3.10.9
- seaborn 0.13+
- scikit-learn 1.4+

---

## 📖 Bibliografía

- Wirth, R., & Hipp, J. (2000). *CRISP-DM: Towards a standard process model for data mining*. Proceedings of the 4th International Conference on the Practical Applications of Knowledge Discovery and Data Mining.
- McKinney, W. (2022). *Python for Data Analysis* (3rd ed.). O'Reilly Media. https://wesmckinney.com/book/
- pandas development team. (2024). *pandas documentation*. https://pandas.pydata.org/docs/
- NumPy Developers. (2024). *NumPy documentation*. https://numpy.org/doc/
- Centro Sismológico Nacional. (2024). *Base de datos sísmica de Chile*. Universidad de Chile. https://www.csn.uchile.cl/
- Reciclador. (2021). *Chile Earthquake Dataset (1976–2021)* [Conjunto de datos]. Kaggle. https://www.kaggle.com/datasets/reciclador/chile-earthquake-dataset-1976-2021

