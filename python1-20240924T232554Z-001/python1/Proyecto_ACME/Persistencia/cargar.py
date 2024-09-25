#cargar archivos
import json


def cargar_archivo_json(nombre_archivo):
    ruta = f'python1/Proyecto_ACME/utils/{nombre_archivo}.json'
    try:
        with open(ruta, 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print(f"")
        return {}


