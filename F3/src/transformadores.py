"""
Módulo de transformadores del dataset sísmico.

Define un contrato común (clase abstracta `Transformador`) y varias
implementaciones intercambiables que lo cumplen. Esto permite aplicar
una lista de transformaciones sobre un DataFrame sin que el código que
las invoca necesite conocer los detalles de cada una (polimorfismo).
"""

from abc import ABC, abstractmethod

import pandas as pd


class Transformador(ABC):
    """
    Contrato común para todas las transformaciones del dataset.

    Cualquier subclase debe implementar `aplicar(df)` y retornar un
    nuevo DataFrame con la transformación aplicada. Esto define el
    "polimorfismo" del módulo: distintas clases, misma interfaz.
    """

    @abstractmethod
    def aplicar(self, df: pd.DataFrame) -> pd.DataFrame:
        """Aplica la transformación y retorna un nuevo DataFrame."""
        raise NotImplementedError


class ClasificadorMagnitudAlta(Transformador):
    """
    Agrega una columna booleana que indica si un sismo es "fuerte"
    según un umbral configurable.

    Se separa el umbral como atributo del objeto (en vez de un valor
    fijo en el código) para que el mismo transformador pueda
    reutilizarse con distintos criterios sin modificar la clase.
    """

    def __init__(self, umbral: float = 6.0):
        self._umbral = umbral

    def aplicar(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        df["Sismo_Fuerte"] = df["Magnitude"] >= self._umbral
        return df


class ClasificadorProfundidad(Transformador):
    """
    Agrega una columna categórica con la clasificación de profundidad
    focal del sismo (Superficial, Intermedio, Profundo).

    Los límites siguen la clasificación estándar usada en F2, lo que
    mantiene coherencia entre fases del proyecto.
    """

    LIMITE_SUPERFICIAL = 70
    LIMITE_INTERMEDIO = 300

    def aplicar(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        df["Categoria_Profundidad"] = df["Depth"].apply(self._categorizar)
        return df

    def _categorizar(self, profundidad: float) -> str:
        """Método auxiliar privado: clasifica un valor de profundidad."""
        if profundidad < self.LIMITE_SUPERFICIAL:
            return "Superficial"
        elif profundidad <= self.LIMITE_INTERMEDIO:
            return "Intermedio"
        return "Profundo"


class NormalizadorMinMax(Transformador):
    """
    Normaliza una o más columnas numéricas al rango [0, 1] usando
    Min-Max scaling, agregando columnas con sufijo '_norm'.

    Esta transformación reutiliza la misma lógica aplicada en F2,
    ahora encapsulada como un transformador intercambiable.
    """

    def __init__(self, columnas: list[str]):
        self._columnas = columnas

    def aplicar(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        for col in self._columnas:
            col_min, col_max = df[col].min(), df[col].max()
            df[f"{col}_norm"] = (df[col] - col_min) / (col_max - col_min)
        return df
