import json


def guardar(datos, nombre):
    ruta_archivo = f'python1/Proyecto_ACME/utils/{nombre}.json'

    
    try:
        with open(ruta_archivo, 'r') as fd:
            contenido = json.load(fd)
            if not isinstance(contenido, dict):
                contenido = {}
    except FileNotFoundError:
        contenido = {}

    
    if datos:  
        contenido.update(datos) 

   
    with open(ruta_archivo, 'w') as fd:
        json.dump(contenido, fd, indent=4)
