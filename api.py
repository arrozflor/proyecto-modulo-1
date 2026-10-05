import pandas as pd
from sodapy import Socrata


def normalizar_departamento(nombre_departamento):

    equivalencias = {
        "VALLE DEL CAUCA": "VALLE",
        "NORTE DE SANTANDER": "NORTE SANTANDER",
        "LA GUAJIRA": "GUAJIRA",
        "SANTA MARTA": "STA MARTA D.E."
    }

    resultado = equivalencias.get(
        nombre_departamento,
        nombre_departamento
    )

    print("Antes:", nombre_departamento)
    print("Después:", resultado)

    return resultado



def consultar_casos(nombre_departamento, limite_registros):

    nombre_departamento = normalizar_departamento(nombre_departamento)

    client = Socrata("www.datos.gov.co", None)

    resultados = client.get(
        "gt2j-8ykr",
        limit=limite_registros,
        departamento_nom=nombre_departamento
    )

    if not resultados:
        return None

    datos = pd.DataFrame.from_records(resultados)

    datos_filtrados = datos[[
        "ciudad_municipio_nom",
        "departamento_nom",
        "edad",
        "fuente_tipo_contagio",
        "estado"
    ]].copy()

    datos_filtrados["País de procedencia"] = "No disponible"

    datos_filtrados.columns = [
        "Ciudad de ubicación",
        "Departamento",
        "Edad",
        "Tipo",
        "Estado",
        "País de procedencia"
    ]

    return datos_filtrados


