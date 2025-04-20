from colorama import Fore, Style, init
from datetime import datetime
init(autoreset=True)


def leerCodigoModulo():
    while True:
        try:
            cod = int(input("Ingrese el código del módulo: "))
            if cod:
                return cod
            
            print(Fore.RED+">>> Error. Código inválido")
        except ValueError:
            print(Fore.RED+">>Error. Codigo invalido")    

def nombreModulo():
    while True:
        try:
            strNombreModulo = input("Ingrese nombre del módulo: ").strip()
            if strNombreModulo:
                return strNombreModulo
            print(Fore.RED+">>> Error. Nombre inválido")
        except Exception as e:
            print(Fore.RED+">>Error al iniciar el nombre. ")

def duracionModulo():
    while True:
        try:
            dModulo1 = int(input("Ingrese la duración del módulo (semanas): "))
            if dModulo1 > 0:
                return dModulo1
            print(Fore.RED+">>> Error. Duración inválida.")
        except ValueError:
            print(Fore.RED+">>> Error. Duración inválida.")

def horaInicio():
    while True:
        try:
            hora = input("Ingrese la hora de inicio de la clase (HH:MM): ")
            datetime.strptime(hora, "%H:%M")  # Validar formato de hora
            return hora
        except ValueError:
            print(Fore.RED+">>> Error. Formato de hora inválido. Debe ser HH:MM.")

def horaFin():
    while True:
        try:
            hora = input("Ingrese la hora de fin de la clase (HH:MM): ")
            datetime.strptime(hora, "%H:%M")  # Validar formato de hora
            return hora
        except ValueError:
            print(Fore.RED+">>> Error. Formato de hora inválido. Debe ser HH:MM.")

def registroModulo(modulo):
    codigo = leerCodigoModulo()
    if codigo not in modulo: 
        nombre = nombreModulo()
        duracion = duracionModulo()
        inicio = horaInicio()
        fin = horaFin()
        modulo2 = {
            "Nombre": nombre,
            "Duracion": duracion,
            "Hora_Inicio": inicio,
            "Hora_Fin": fin
        }
        modulo[codigo]=modulo2
        print("Módulo registrado correctamente.")
    else:
        print("El código del módulo ya existe.")    

    input("Presione cualquier tecla para volver al menú...")
    return modulo



