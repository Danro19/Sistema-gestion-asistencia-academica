from colorama import Fore,  init
from datetime import datetime
init(autoreset=True)

def registroAsistencia(asistencia, estudiantes):
    while True:
        try:
            codigo_estudiante = int(input("Ingrese el código del estudiante: "))
            if codigo_estudiante not in estudiantes:
                print(Fore.RED+">>> Error. El código ingresado no está registrado como estudiante.")
                continue
            
            # Obtener la fecha actual
            fecha_actual = datetime.now().strftime("%Y-%m-%d")
            
            # Inicializar el registro de asistencia para la fecha
            if fecha_actual not in asistencia:
                asistencia[fecha_actual] = {}
            
            # Marcar hora de llegada
            hora_llegada = datetime.now().strftime("%H:%M:%S")
            print(f"La hora de llegada del estudiante {estudiantes[codigo_estudiante]['Nombre']} ({codigo_estudiante}) es: {hora_llegada}")

            # Registrar la entrada
            asistencia[fecha_actual][codigo_estudiante] = {
                "Nombre": estudiantes[codigo_estudiante]["Nombre"],
                "Hora de llegada": hora_llegada,
                "Hora de salida": None  # Aún no se ha registrado la salida
            }
            
            input("Presione cualquier tecla para registrar la salida del estudiante...")

            # Marcar hora de salida
            hora_salida = datetime.now().strftime("%H:%M:%S")
            print(f"La hora de salida del estudiante {estudiantes[codigo_estudiante]['Nombre']} ({codigo_estudiante}) es: {hora_salida}")

            # Actualizar el registro de salida
            asistencia[fecha_actual][codigo_estudiante]["Hora de salida"] = hora_salida
            
            

            print("Asistencia registrada correctamente.")
            break  # Salir del bucle si todo va bien
            
        except ValueError:
            print(Fore.RED+">>> Error. Código inválido.")

        except Exception as e:
            print(Fore.RED+f">>> Error: {e}")

    input(Fore.RED+"Presione cualquier tecla para volver al menú...")
    return asistencia
