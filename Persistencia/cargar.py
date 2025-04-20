import json
import os

def cargar_archivo_json(nombre_archivo):
    # Corregir la ruta para que sea relativa al directorio del proyecto
    ruta = f'Proyecto_ACME/utils/{nombre_archivo}.json'
    
    # Verificar si el directorio existe, si no, crearlo
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    
    try:
        with open(ruta, 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print(f"Archivo {nombre_archivo}.json no encontrado. Se creará uno nuevo.")
        return {}
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo {nombre_archivo}.json. Posible formato incorrecto.")
        return {}
