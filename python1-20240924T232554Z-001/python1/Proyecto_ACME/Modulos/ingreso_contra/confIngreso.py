import json
from os import wait
from colorama import Fore, Style, init
from Modulos.limpieza import limpiarPantalla
init(autoreset=True)
import hashlib
def contrasenaIni():
    try:
        with open("Proyecto_ACME/utils/Contrasena.json", "r") as fd:
            return json.load(fd)
    except FileNotFoundError:
        return "SISGESA"  
def leerPassword(password):
    while True:
        password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        try: 
            if len(password.strip()) == 0:
                print("error en ingreso.")
            return password
        except Exception as e:
            print("Error al ingresar la contraseña" + e)



def verificar_contrasena(ingresada):
    return ingresada == contrasenaIni()

def login():
    while True:
       
        print(Fore.LIGHTRED_EX+"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(Fore.LIGHTRED_EX+"~        █████████     █████████  ██████   ██████ ██████████                                                              ~")
        print(Fore.LIGHTRED_EX+"~       ███░░░░░███   ███░░░░░███░░██████ ██████ ░░███░░░░░█                                                              ~")
        print(Fore.LIGHTRED_EX+"~      ░███    ░███  ███     ░░░  ░███░█████░███  ░███  █ ░                                                               ~")
        print(Fore.LIGHTRED_EX+"~      ░███████████ ░███          ░███░░███ ░███  ░██████                                                                 ~")
        print(Fore.LIGHTRED_EX+"~      ░███░░░░░███ ░███          ░███ ░░░  ░███  ░███░░█                                                                 ~")
        print(Fore.LIGHTRED_EX+"~      ░███    ░███ ░░███     ███ ░███      ░███  ░███ ░   █                                                              ~")
        print(Fore.LIGHTRED_EX+"~      █████   █████ ░░█████████  █████     █████ ██████████                                                              ~")
        print(Fore.LIGHTRED_EX+"~     ░░░░░   ░░░░░   ░░░░░░░░░  ░░░░░     ░░░░░ ░░░░░░░░░░                                                               ~")
        print(Fore.LIGHTRED_EX+"~      ██████████ ██████████   █████  █████   █████████    █████████   ███████████ █████    ███████    ██████   █████     ~")
        print(Fore.LIGHTRED_EX+"~     ░░███░░░░░█░░███░░░░███ ░░███  ░░███   ███░░░░░███  ███░░░░░███ ░█░░░███░░░█░░███   ███░░░░░███ ░░██████ ░░███      ~")
        print(Fore.LIGHTRED_EX+"~      ░███  █ ░  ░███   ░░███ ░███   ░███  ███     ░░░  ░███    ░███ ░   ░███  ░  ░███  ███     ░░███ ░███░███ ░███      ~")
        print(Fore.LIGHTRED_EX+"~      ░██████    ░███    ░███ ░███   ░███ ░███          ░███████████     ░███     ░███ ░███      ░███ ░███░░███░███      ~")
        print(Fore.LIGHTRED_EX+"~      ░███░░█    ░███    ░███ ░███   ░███ ░███          ░███░░░░░███     ░███     ░███ ░███      ░███ ░███ ░░██████      ~")
        print(Fore.LIGHTRED_EX+"~      ░███ ░   █ ░███    ███  ░███   ░███ ░░███     ███ ░███    ░███     ░███     ░███ ░░███     ███  ░███  ░░█████      ~")
        print(Fore.LIGHTRED_EX+"~      ██████████ ██████████   ░░████████   ░░█████████  █████   █████    █████    █████ ░░░███████░   █████  ░░█████     ~")
        print(Fore.LIGHTRED_EX+"~     ░░░░░░░░░░ ░░░░░░░░░░     ░░░░░░░░     ░░░░░░░░░  ░░░░░   ░░░░░    ░░░░░    ░░░░░    ░░░░░░░    ░░░░░    ░░░░░      ~")
        print(Fore.LIGHTRED_EX+"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        input("Precione Enter tecla para continuar...")
        limpiarPantalla
        print("BIENVENIDO")
        print(Fore.BLACK+"          ___                              _...__         ")                                               
        print(Fore.BLACK+"       .-'   '--._                       .'_     '-.      ")                                          
        print(Fore.BLACK+"     .'     .--._ '-._                 .'.' \       '.    ")                                            
        print(Fore.BLACK+"    /      /__   `'.  '.              / /    `\       \   ")                                             
        print(Fore.BLACK+"   /      /   '-.    `\ \           /'/'       \      |   ")                                             
        print(Fore.BLACK+"   |     |       '.    `\`\        / /     _.-'|      |   ")                                             
        print(Fore.BLACK+"   |     |         \     \ \      / /    .'    |      /   ")                                             
        print(Fore.BLACK+"    \    /          '.   | |,-~-,/ /   .'      \     /    ")                                            
        print(Fore.BLACK+"     '--'           __\               /__       '._.'     ")                                           
        print(Fore.BLACK+"                  ."  '.             .'  ".               ")                                 
        print(Fore.BLACK+"                  |      '.       .'      |               ")                                 
        print(Fore.BLACK+"                   \ ',    '.   .'    .' /                ")                                
        print(Fore.BLACK+"                   /'-.""-._ \ / _.-"".-'\                ")                                
        print(Fore.BLACK+"        _.=='''--,/ '/_.--._\'V'/_.--._\' \,--'''--._     ")                                           
        print(Fore.BLACK+"      .'            _'-.__0_;\ /;_0__.-' _'          '.   ")                                             
        print(Fore.BLACK+"     /     ,____..-'\'.      '''      -'/'--..____,    \  ")                                              
        print(Fore.BLACK+"    /     '          \       .=.       /          `     \ ")                                               
        print(Fore.BLACK+"    |             __  '-.   .-=-.   .-'  __             | ")                                               
        print(Fore.BLACK+"     \      _.--''  ''---'. .-=-. .'---''  ''--._      /  ")                                              
        print(Fore.BLACK+"      '----'            .-'  ___  '-.            `----'   ")                                             
        print(Fore.BLACK+"                       (    '   '    )                    ")                            
        print(Fore.BLACK+"                        '.    _    .'                     ")                           
        print(Fore.BLACK+"                          '--/ \--'                       ")                         
        print(Fore.BLACK+"                             |#|                          ")                      
        print(Fore.BLACK+"                             \_/                          ")                      
        input("Precione Enter para continuar...")
        limpiarPantalla
        
        try:

            
            print(Fore.LIGHTMAGENTA_EX+"██████████████████████████████████████████████████████████████████████████████████████████████")
            print(Fore.LIGHTMAGENTA_EX+"█▌       █████████  █████  █████████    █████████  ██████████  █████████    █████████       ▐█")
            print(Fore.LIGHTMAGENTA_EX+"█▌      ███░░░░░███░░███  ███░░░░░███  ███░░░░░███░░███░░░░░█ ███░░░░░███  ███░░░░░███      ▐█")
            print(Fore.LIGHTMAGENTA_EX+"█▌     ░███    ░░░  ░███ ░███    ░░░  ███     ░░░  ░███  █ ░ ░███    ░░░  ░███    ░███      ▐█")
            print(Fore.LIGHTMAGENTA_EX+"█▌     ░░█████████  ░███ ░░█████████ ░███          ░██████   ░░█████████  ░███████████      ▐█")
            print(Fore.LIGHTMAGENTA_EX+"█▌      ░░░░░░░░███ ░███  ░░░░░░░░███░███    █████ ░███░░█    ░░░░░░░░███ ░███░░░░░███      ▐█")
            print(Fore.LIGHTMAGENTA_EX+"█▌      ███    ░███ ░███  ███    ░███░░███  ░░███  ░███ ░   █ ███    ░███ ░███    ░███      ▐█")
            print(Fore.LIGHTMAGENTA_EX+"█▌     ░░█████████  █████░░█████████  ░░█████████  ██████████░░█████████  █████   █████     ▐█")
            print(Fore.LIGHTMAGENTA_EX+"█▌      ░░░░░░░░░  ░░░░░  ░░░░░░░░░    ░░░░░░░░░  ░░░░░░░░░░  ░░░░░░░░░  ░░░░░   ░░░░░      ▐█")
            print(Fore.LIGHTMAGENTA_EX+"██████████████████████████████████████████████████████████████████████████████████████████████")
            print("Si es tu primer ingreso la clave es SISGESA")    




            print("="*40)
            usuario = input(">>Ingrese el nombre de usuario: ")
            contrasena = input(">>Ingresa la contraseña: ")
            leerPassword(contrasena)
            print("="*40)
            if verificar_contrasena(contrasena):
                print("La contraseña indicada es correcta.")
                break
            else:
                print(Fore.RED+">>Contraseña incorrecta.")
        except Exception as e:
            print(Fore.RED+">>Error. Contraseña no valida")
