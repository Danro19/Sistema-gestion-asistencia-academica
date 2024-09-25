import json

def buscarGrupo(grupo):
    codGrupo = input("Ingrese el código del grupo: ")
    if codGrupo in grupo:
        return codGrupo
    else:
        print("Grupo no existe")
        return None  

def asignarModulo(modulo):
    cont = int(input("¿Cuántos módulos desea ingresar? "))
    if cont > 3:
        print("maximo de modulos son 3")
    else:
        modulos_asignados = {}  
        print(modulo)
        for i in range(1, cont + 1):
            codModulo = input(f"Ingrese el código del módulo {i}: ")
            if codModulo in modulo:
                modulos_asignados[f"m{i}"] = codModulo  
            else:
                print("Módulo no existe")

    return json.dumps(modulos_asignados)  

def buscarEstudiante(estudiantes):
    codEstudiante = input("Ingrese el código del estudiante: ")
    if codEstudiante in estudiantes:
        return codEstudiante
    else:
        print("Estudiante no existe")
         

def relacionarEstudiantes(estudiantes, modulos, grupos, datos):
    datosEstudiante = buscarEstudiante(estudiantes)
    print(datosEstudiante)
    if datosEstudiante is None:
        print("El estudiante no esta registrado")  

    if datosEstudiante not in datos:
        datosGrupo = buscarGrupo(grupos)
        print(datosGrupo)
        if datosGrupo is None:
            print("El grupo no esta registrado")
        datosAsignacion = {
            "codigo": datosEstudiante,
            "Grupo": datosGrupo,
            "modulo": json.loads(asignarModulo(modulos)) 
        }
        datos[datosEstudiante] = datosAsignacion
        print(f"Asignación completada para el estudiante {datosEstudiante}.")
    else:
        print("Estudiante ya asignado.")

    return datos  
