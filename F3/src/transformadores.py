class TransformadorMagnitud:

    def aplicar(self, df):
        raise NotImplementedError("Este método debe ser implementado por una subclase")


class ClasificadorMagnitudAlta(TransformadorMagnitud):

    def __init__(self, umbral=6.0):
        self.umbral = umbral

    def aplicar(self, df):
        df = df.copy()
        df["Sismo_Fuerte"] = df["Magnitude"] >= self.umbral
        return df


class ClasificadorProfundidad:

    def aplicar(self, df):
        df = df.copy()

        def categorizar(profundidad):
            if profundidad < 70:
                return "Superficial"
            elif profundidad <= 300:
                return "Intermedio"
            else:
                return "Profundo"

        df["Categoria_Profundidad"] = df["Depth"].apply(categorizar)
        return df