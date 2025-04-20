

def leerCodigoEstudiante():
    while True:
        try:    
            cod = int(input("Ingrese el codigo del estudiante: "))
            return cod
        except ValueError:
            print("Error al ingresar el codigo.\n")

def nombreEstudiante():
    while True:
        strNombreEstudiante = input("Ingrese el nombre del estudiante: ").strip()
        if strNombreEstudiante:
            return strNombreEstudiante
        print(">>>Error. Nombre inválido")

def edadEstudiante():
    while True:
        try:
            edad = int(input("Ingrese la edad del estudiante (años): "))
            if edad >= 6:
                return edad 
            print(">>> Error. Edad Inválida.")
        except ValueError:
            print(">>>Error. Edad inválida.") 

def sexoEstudiante():
    while True:
        sexo = input("Ingrese el sexo del estudiante (M/F): ").strip().upper()
        if sexo in {"M", "F"}:
            return sexo
        print(">>> Error. Sexo Inválido.")

def registroEstudiante(estudiante):
    codigo = leerCodigoEstudiante()
    if codigo not in estudiante: 
        nombre = nombreEstudiante()
        edad = edadEstudiante()
        sexo = sexoEstudiante()
        estudiante[codigo] = {"Nombre": nombre, "Edad": edad, "Sexo": sexo}
        print(f"{codigo} registrado correctamente.")
    else:
        print("El codigo de estudiante ya existe.")    

    input("Presione cualquier tecla para volver al menu...")
    return estudiante


