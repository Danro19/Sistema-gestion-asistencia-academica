from colorama import Fore, Style, init
from Modulos.limpieza import limpiarPantalla
def menu():
    limpiarPantalla()
    while True:
       
        init(autoreset=True)
        
        
            
        print(Fore.RED +"╔╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╗")
        print(Fore.RED +"╠╬╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╬╣")
        print(Fore.RED +"╠╣                                                         ╠╣")
        print(Fore.RED +"╠╣                                                         ╠╣")
        print(Fore.RED +"╠╣      ▄▄▄▄███▄▄▄▄      ▄████████ ███▄▄▄▄   ███    █▄     ╠╣")
        print(Fore.RED +"╠╣    ▄██▀▀▀███▀▀▀██▄   ███    ███ ███▀▀▀██▄ ███    ███    ╠╣")
        print(Fore.RED +"╠╣    ███   ███   ███   ███    █▀  ███   ███ ███    ███    ╠╣")
        print(Fore.RED +"╠╣    ███   ███   ███  ▄███▄▄▄     ███   ███ ███    ███    ╠╣")
        print(Fore.RED +"╠╣    ███   ███   ███ ▀▀███▀▀▀     ███   ███ ███    ███    ╠╣")
        print(Fore.RED +"╠╣    ███   ███   ███   ███    █▄  ███   ███ ███    ███    ╠╣")
        print(Fore.RED +"╠╣    ███   ███   ███   ███    ███ ███   ███ ███    ███    ╠╣")
        print(Fore.RED +"╠╣     ▀█   ███   █▀    ██████████  ▀█   █▀  ████████▀     ╠╣")
        print(Fore.RED +"╠╣                                                         ╠╣")
        print(Fore.RED +"╠╣                                                         ╠╣")
        print(Fore.RED +"╠╬╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╬╣")
        print(Fore.RED +"╚╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╝")
        
        print(""*10)   
        print("="*40)
        print("a. Registro de grupos.")
        print("b. Registro de módulos.")
        print("c. Registro de estudiantes.")
        print("d. Relacionar.")
        print("e. Registro de docentes.")
        print("f. Registro de asistencia.")
        print("g. Consultas de información.")
        print("h. Informe asistencia.")
        print("i. Cambio de contraseña.")
        print("j. Salida del sistema.")
        print("="*40)
        print("")
        print(">> Ingresar a opcion: ", end="")
        try:
            opciones = ["a", "b", "c","d","e","f", "g", "h", "i"]
            opc = input().lower()
            if opc not in opciones:
                print(Fore.RED+"Error opcion invalida")
                print("presione cualquier tecla para volver al menu. \n")
            return opc
        
        except ValueError:
            print(Fore.RED+"ingreso una opcion incorrecta")
            print("presione cualquier tecla para volver al menu. \n")
         

            