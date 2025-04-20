import json
import os

def guardar(datos, nombre):
    # Corregir la ruta para que sea relativa al directorio del proyecto
    ruta_archivo = f'Proyecto_ACME/utils/{nombre}.json'
    
    # Verificar si el directorio existe, si no, crearlo
    os.makedirs(os.path.dirname(ruta_archivo), exist_ok=True)
    
    try:
        # Intentar cargar el archivo existente
        try:
            with open(ruta_archivo, 'r') as fd:
                contenido = json.load(fd)
                if not isinstance(contenido, dict):
                    print(f"El archivo {nombre}.json no contiene un diccionario. Se creará uno nuevo.")
                    contenido = {}
        except FileNotFoundError:
            contenido = {}
        except json.JSONDecodeError:
            print(f"Error al decodificar el archivo {nombre}.json. Se creará uno nuevo.")
            contenido = {}
        
        # Actualizar el contenido con los nuevos datos
        if datos:
            if isinstance(datos, dict):
                contenido.update(datos)
            else:
                print(f"Advertencia: Los datos para {nombre} no son un diccionario.")
                # Si no es un diccionario, intentar guardar directamente
                contenido = datos
        
        # Guardar los datos actualizados
        with open(ruta_archivo, 'w') as fd:
            json.dump(contenido, fd, indent=4)
        
        print(f"Datos guardados correctamente en {nombre}.json")
        
    except Exception as e:
        print(f"Error al guardar datos en {nombre}.json: {str(e)}")
import json
import os

def guardar(datos, nombre):
    # Corregir la ruta para que sea relativa al directorio del proyecto
    ruta_archivo = f'Proyecto_ACME/utils/{nombre}.json'
    
    # Verificar si el directorio existe, si no, crearlo
    os.makedirs(os.path.dirname(ruta_archivo), exist_ok=True)
    
    try:
        # Intentar cargar el archivo existente
        try:
            with open(ruta_archivo, 'r') as fd:
                contenido = json.load(fd)
                if not isinstance(contenido, dict):
                    print(f"El archivo {nombre}.json no contiene un diccionario. Se creará uno nuevo.")
                    contenido = {}
        except FileNotFoundError:
            contenido = {}
        except json.JSONDecodeError:
            print(f"Error al decodificar el archivo {nombre}.json. Se creará uno nuevo.")
            contenido = {}
        
        # Actualizar el contenido con los nuevos datos
        if datos:
            if isinstance(datos, dict):
                contenido.update(datos)
            else:
                print(f"Advertencia: Los datos para {nombre} no son un diccionario.")
                # Si no es un diccionario, intentar guardar directamente
                contenido = datos
        
        # Guardar los datos actualizados
        with open(ruta_archivo, 'w') as fd:
            json.dump(contenido, fd, indent=4)
        
        print(f"Datos guardados correctamente en {nombre}.json")
        
    except Exception as e:
        print(f"Error al guardar datos en {nombre}.json: {str(e)}")
