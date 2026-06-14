import pandas as pd


def cargar_datos(ruta):
    """
    Carga un archivo CSV y devuelve un DataFrame.
    """
    try:
        df = pd.read_csv(ruta)
        return df

    except FileNotFoundError:
        print("Error: archivo no encontrado")
        return None


def analizar_dataset(df):
    """
    Retorna un resumen básico del dataset.
    """
    resumen = {
        "filas": df.shape[0],
        "columnas": df.shape[1],
        "nombres_columnas": df.columns.tolist(),
        "valores_nulos": df.isnull().sum().to_dict()
    }

    return resumen


def buscar_sismos_fuertes(df, magnitud_minima):
    """
    Retorna los sismos cuya magnitud sea mayor o igual
    al valor indicado.
    """
    return df[df["Magnitude"] >= magnitud_minima]