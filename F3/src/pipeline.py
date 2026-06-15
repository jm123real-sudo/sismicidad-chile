class AnalizadorSismicoBase:

    def __init__(self, dataframe):
        self.df = dataframe

    def resumen(self):
        return {
            "registros": len(self.df),
            "magnitud_maxima": self.df["Magnitude"].max()
        }


class AnalizadorSismicoAvanzado(AnalizadorSismicoBase):

    def resumen(self):
        resumen_base = super().resumen()

        resumen_base["profundidad_promedio"] = round(self.df["Depth"].mean(), 2)
        resumen_base["sismos_fuertes"] = len(self.df[self.df["Magnitude"] >= 6.0])
        resumen_base["magnitud_promedio"] = round(self.df["Magnitude"].mean(), 2)

        return resumen_base