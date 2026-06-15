"""
Módulo de análisis sísmico orientado a objetos.

Define una jerarquía de clases que encapsulan el estado del dataset
(atributo protegido `_df`) y exponen métodos públicos para consultarlo.
La clase avanzada extiende el comportamiento de la clase base mediante
herencia y polimorfismo (sobrescritura de `resumen()`).
"""

import pandas as pd


class AnalizadorSismicoBase:
    """
    Clase base que encapsula un DataFrame de eventos sísmicos.

    El atributo `_df` es protegido (convención de un guion bajo):
    no se accede directamente desde fuera de la clase, sino mediante
    los métodos públicos definidos aquí. Esto permite que las subclases
    cambien la implementación interna sin afectar el código que usa
    la clase (encapsulamiento).
    """

    def __init__(self, dataframe: pd.DataFrame):
        # Se trabaja sobre una copia para no modificar el DataFrame original
        self._df = dataframe.copy()

    @property
    def datos(self) -> pd.DataFrame:
        """
        Acceso de solo lectura al DataFrame interno.

        Se expone como propiedad (no como atributo público) para que,
        si en el futuro se necesita validar o transformar antes de
        entregar los datos, baste con modificar este método sin romper
        el código que ya lo usa.
        """
        return self._df

    def cantidad_registros(self) -> int:
        """Retorna el número total de registros del dataset."""
        return len(self._df)

    def magnitud_maxima(self) -> float:
        """Retorna la magnitud máxima registrada."""
        return self._df["Magnitude"].max()

    def resumen(self) -> dict:
        """
        Retorna un resumen básico del dataset.

        Este método es el punto de extensión para el polimorfismo:
        las subclases pueden sobrescribirlo para agregar más
        indicadores sin cambiar la firma del método.
        """
        return {
            "registros": self.cantidad_registros(),
            "magnitud_maxima": self.magnitud_maxima(),
        }


class AnalizadorSismicoAvanzado(AnalizadorSismicoBase):
    """
    Extiende AnalizadorSismicoBase agregando indicadores adicionales.

    Demuestra:
      - Herencia: reutiliza __init__ y los métodos de la clase base.
      - Polimorfismo: sobrescribe resumen() devolviendo un diccionario
        más completo, pero con la misma interfaz (mismo nombre y tipo
        de retorno) que la clase base.
    """

    def __init__(self, dataframe: pd.DataFrame, umbral_fuerte: float = 6.0):
        super().__init__(dataframe)
        # Atributo protegido propio de esta subclase
        self._umbral_fuerte = umbral_fuerte

    def profundidad_promedio(self) -> float:
        """Retorna la profundidad promedio en kilómetros."""
        return round(self._df["Depth"].mean(), 2)

    def magnitud_promedio(self) -> float:
        """Retorna la magnitud promedio de los eventos."""
        return round(self._df["Magnitude"].mean(), 2)

    def contar_sismos_fuertes(self, magnitud_minima: float | None = None) -> int:
        """
        Cuenta los sismos con magnitud mayor o igual al umbral indicado.

        Si no se especifica `magnitud_minima`, se usa el umbral
        configurado en el constructor (`_umbral_fuerte`), evitando
        repetir el valor mágico en cada llamada.
        """
        umbral = self._umbral_fuerte if magnitud_minima is None else magnitud_minima
        return int((self._df["Magnitude"] >= umbral).sum())

    def resumen(self) -> dict:
        """
        Sobrescribe el resumen de la clase base agregando indicadores
        adicionales (polimorfismo: misma interfaz, distinto resultado).
        """
        resumen_base = super().resumen()
        resumen_base["profundidad_promedio"] = self.profundidad_promedio()
        resumen_base["magnitud_promedio"] = self.magnitud_promedio()
        resumen_base["sismos_fuertes"] = self.contar_sismos_fuertes()
        return resumen_base
