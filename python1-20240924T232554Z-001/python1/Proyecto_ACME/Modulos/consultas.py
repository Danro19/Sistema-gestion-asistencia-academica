def imprimirEstudiantes(estudiantes, codigos):
    print("Estudiantes:")
    for codigo in codigos:
        if codigo in estudiantes:
            print(f"- {estudiantes[codigo]['Nombre']}")
        else:
            print(f"- Código {codigo} no encontrado.")

def imprimirDocentes(profesores, codigos):
    print("Docentes:")
    for codigo in codigos:
        if codigo in profesores:
            print(f"- {profesores[codigo]['Nombre']}")
        else:
            print(f"- Cédula {codigo} no encontrada.")

def consultarEstudiantesPorGrupo(grupo, estudiantes):
    codigo_grupo = int(input("Ingrese el código del grupo: "))
    if codigo_grupo in grupo:
        print(f"Estudiantes matriculados en el grupo {codigo_grupo}:")
        imprimirEstudiantes(estudiantes, grupo[codigo_grupo]['Estudiantes'])
    else:
        print("Código de grupo no válido.")

def consultarEstudiantesPorModulo(modulo, estudiantes):
    codigo_modulo = int(input("Ingrese el código del módulo: "))
    if codigo_modulo in modulo:
        print(f"Estudiantes inscritos en el módulo {codigo_modulo}:")
        imprimirEstudiantes(estudiantes, modulo[codigo_modulo]['Estudiantes'])
    else:
        print("Código de módulo no válido.")

def consultarDocentesPorModulo(modulo, profesores):
    codigo_modulo = int(input("Ingrese el código del módulo: "))
    if codigo_modulo in modulo:
        print(f"Docentes que imparten el módulo {codigo_modulo}:")
        imprimirDocentes(profesores, modulo[codigo_modulo]['Docentes'])
    else:
        print("Código de módulo no válido.")

def consultarEstudiantesPorDocente(profesores, modulo, estudiantes):
    cedula_docente = int(input("Ingrese la cédula del docente: "))
    if cedula_docente in profesores:
        print(f"Estudiantes a cargo del docente {profesores[cedula_docente]['Nombre']} en el módulo:")
        for codigo_modulo in profesores[cedula_docente]['Módulos']:
            imprimirEstudiantes(estudiantes, modulo[codigo_modulo]['Estudiantes'])
    else:
        print("Cédula de docente no válida.")
        
        
def menuConsulta():
    while True:
        print("** Consulta **")
        opciones = {
            "a": "Consultar estudiantes por grupo",
            "b": "Consultar estudiantes por módulo",
            "c": "Consultar docentes por módulo",
            "d": "Consultar estudiantes a cargo de un docente",
        }

        for clave, valor in opciones.items():
            print(f"{clave}. {valor}")

        opcion = input(">>> Opción: ").strip()
        if opcion in opciones:
            return opcion
        else:
            print("Error. Opción no válida.")

