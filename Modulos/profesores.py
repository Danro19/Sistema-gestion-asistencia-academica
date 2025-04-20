import json
from colorama import Fore, Style, init
init(autoreset=True)

def leerCedulaProfesor():
    while True:
        try:    
            cedula = int(input("Ingrese la cédula del docente: "))
            return cedula
        except ValueError:
            print(Fore.RED+">>Error al ingresar la cédula.\n")

def nombreProfesor():
    while True: 
        try:
            strNombreProfesor = input("Ingrese el nombre del docente: ").strip()
            if strNombreProfesor:
                return strNombreProfesor
            print(Fore.RED+">>> Error. Nombre inválido")
        except Exception as e:
            print(Fore.RED+">>Error. Nombre Invalido")

def eleccionModuloProfesor(modulos_disponibles):
    modulos_asignados = []
    
    while len(modulos_asignados) < 3:
        print("\nMódulos Libres:")
        for codigo, modulo1 in modulos_disponibles.items():
            print(f"Código: {codigo}, Nombre: {modulo1['Nombre']}, Duración: {modulo1['Duracion']}")  

        if not modulos_disponibles:
            print(Fore.RED+"No hay módulos disponibles.")
            break

        try:
            codigo_modulo = (input("Ingrese el código del módulo a asignar (Para salir digite el número 0): "))
            if codigo_modulo == "0":
                break
            
            if codigo_modulo == modulos_disponibles():
                modulos_asignados.append(codigo_modulo)
                print(f"Módulo {modulos_disponibles[codigo_modulo]['Nombre']} asignado.")
            else:
                print(Fore.RED+">>>Código inválido o módulo ya asignado.")
        except ValueError:
            print(Fore.RED+">>> Error. Código inválido.")
    
    return modulos_asignados

def registroDocente(profesor, modulos_disponibles):
    cedula = leerCedulaProfesor()
    if cedula not in profesor: 
        nombre = nombreProfesor()
        modulos_asignados = eleccionModuloProfesor(modulos_disponibles)
        docente = {"Nombre": nombre, "Módulos": modulos_asignados}
        profesor[cedula]=docente 
    else:
        print("La cédula del docente ya existe.")    

    input("Presione cualquier tecla para volver al menú...")
    return profesor
