"""
Módulo orquestador del flujo de transformaciones.

Define la clase `Pipeline`, que recibe una lista de objetos
`Transformador` (composición) y los ejecuta en orden sobre un
DataFrame. El Pipeline no necesita conocer qué hace cada
transformador: solo invoca su método `aplicar(df)` (polimorfismo).
"""

import pandas as pd

from transformadores import Transformador


class Pipeline:
    """
    Orquesta una secuencia de transformaciones sobre un DataFrame.

    Atributos:
        _etapas: lista de objetos Transformador a ejecutar en orden.
                  Es un atributo protegido porque el Pipeline controla
                  internamente cómo se recorre la lista.
    """

    def __init__(self, etapas: list[Transformador]):
        self._etapas = etapas

    def agregar_etapa(self, transformador: Transformador) -> "Pipeline":
        """
        Agrega una etapa adicional al pipeline y retorna self,
        permitiendo encadenar llamadas.
        """
        self._etapas.append(transformador)
        return self

    def ejecutar(self, df: pd.DataFrame, verbose: bool = True) -> pd.DataFrame:
        """
        Ejecuta cada etapa en orden sobre una copia del DataFrame
        de entrada y retorna el resultado final.
        """
        resultado = df.copy()
        for etapa in self._etapas:
            resultado = etapa.aplicar(resultado)
            if verbose:
                print(f"✅ Etapa ejecutada: {etapa.__class__.__name__}")
        return resultado