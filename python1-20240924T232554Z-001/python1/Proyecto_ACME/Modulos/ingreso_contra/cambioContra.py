import json
import hashlib

def cambiarContrasena():
    nueva_contrasena = input("Ingrese la nueva contraseña: ").strip()
    if nueva_contrasena:
        with open("Proyecto_ACME/utils/Contraseña.json", "w") as fd:
            json.dump(nueva_contrasena, fd)
        print("Contraseña cambiada exitosamente.")
    else:
        print("Error. Contraseña inválida.")

