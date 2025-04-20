from colorama import Fore, Style, init

init(autoreset=True)


def leerCodigoGrupo():
    while True:
        try:    
            cod = int(input("Ingrese el código del grupo: "))
            return cod
        except ValueError:
            print("Error al ingresar el código.\n")

def nombreGrupo():
    while True:
        try:
            strNombreGrupo = input("Ingrese el nombre del grupo: ").strip()
            if strNombreGrupo:
                return strNombreGrupo
            print(Fore.RED+">>> Error. Nombre inválido")
        except Exception as e:
            print(Fore.RED+">> Error al introducir el nombre" + e)

def siglaGrupo():
    while True:
        try:
            sigla = input("Ingrese la sigla del grupo: ").strip().title()
            if sigla:
                return sigla
            print(Fore.RED+">>> Error. Sigla inválida.")
        except Exception as e:
            print(Fore.RED+">>> Error al ingresar la sigla")

def registroGrupo(grupo):
    codigo = leerCodigoGrupo()
    if codigo not in grupo: 
        nombre = nombreGrupo()
        sigla = siglaGrupo()
        
        Model = {
            "Nombre": nombre,  # Asegúrate de que aquí se use 'Nombre'
            "Sigla": sigla
        }
        grupo[codigo]=Model
        print(f"{codigo} registrado correctamente.")
    else:
        print("El código del grupo ya existe.")    

    input("Presione cualquier tecla para volver al menú...")
    return grupo





