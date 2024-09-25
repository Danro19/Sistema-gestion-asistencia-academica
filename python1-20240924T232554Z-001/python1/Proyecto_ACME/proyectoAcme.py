# python/Proyecto_ACME/proyectoAcme.py
from Modulos.limpieza import limpiarPantalla
from Modulos.estudiantes import registroEstudiante
from Interfaz.menu import menu
from Modulos.grupo import registroGrupo
from Modulos.modulos import  registroModulo
from Modulos.profesores import registroDocente
from Modulos.registroasistencia import registroAsistencia
from Modulos.ingreso_contra.confIngreso import login
from Modulos.ingreso_contra.cambioContra import cambiarContrasena
from Modulos.relacion_estudiantes import relacionarEstudiantes
from Persistencia.persistencia import guardar
from Persistencia.cargar import cargar_archivo_json
from Modulos.consultas import consultarDocentesPorModulo, consultarEstudiantesPorDocente, consultarEstudiantesPorGrupo, consultarEstudiantesPorModulo, menuConsulta
from colorama import Fore, Style, init


init(autoreset=True)

login()
limpiarPantalla()
while True:
    opc = menu()
    match opc:
        case "a":
            limpiarPantalla()
            guardar(registroGrupo(cargar_archivo_json("grupos")),"grupos") 
            
        case "b":
            limpiarPantalla()
            guardar(registroModulo(cargar_archivo_json("modulos")), "modulos")
            
        case "c":
            limpiarPantalla()
            guardar(registroEstudiante(cargar_archivo_json("estudiantes")),"estudiantes"),
            
        case "d":
            guardar(relacionarEstudiantes(cargar_archivo_json("estudiantes"),cargar_archivo_json("modulo"),cargar_archivo_json("grupos"),cargar_archivo_json("asignacion")),
            "asignacion")
        case "e":
            limpiarPantalla()
            guardar(registroDocente(cargar_archivo_json("docentes"), cargar_archivo_json("modulos")), "docentes")
            
        case "f":
            limpiarPantalla()
            guardar(registroAsistencia(cargar_archivo_json("estudiantes"),cargar_archivo_json("modulo"),cargar_archivo_json("asistencia")),"asistencia")
            
        case "g":
            limpiarPantalla()
            # consultasPorCodigo(cargar_archivo_json("asignacion"),cargar_archivo_json("Estudiantes"))
            opc=menuConsulta()
            match opc:
                case"a":
                    guardar(consultarEstudiantesPorGrupo(cargar_archivo_json("estudiantes"),cargar_archivo_json("grupo")),"consultaEstudiantePorGrupo"),
                case"b":
                    guardar(consultarEstudiantesPorModulo(cargar_archivo_json("estudiantes"),cargar_archivo_json("modulo")),"consultaEstudiantePorModulo"),
                case"c":
                    guardar(consultarDocentesPorModulo(cargar_archivo_json("modulo"),cargar_archivo_json("docente")),"consultaDocentePorModulo"),
                case"d":
                    guardar(consultarEstudiantesPorDocente(cargar_archivo_json("profesor"),cargar_archivo_json("modulo"),cargar_archivo_json("estudiantes")),"ConsultaEstudiantePorDocente")
        case "h":
            pass
        
        case "i":
            cambiarContrasena() 
            
        case "j":
            print("Gracias por usar el software")
            

            print(Fore.GREEN + "*==========================================================================================*")
            print(Fore.GREEN + "88////////////////////////////////////////////////////////////////////////////////////////88")
            print(Fore.GREEN + "88////////////////////////////////////////////////////////////////////////////////////////88")
            print(Fore.GREEN + "88//////▄██████▄/////▄████████////▄████████  ▄████████//▄█/////▄████████//▄████████///////88")
            print(Fore.GREEN + "88//////███////███///███////███///███////███ ███/// ███/███////███////███/███////███//////88")
            print(Fore.GREEN + "88//////███////█▀////███////███///███////███ ███/// █▀//███▌///███////███/███////█▀///////88")
            print(Fore.GREEN + "88/////▄███/////////▄███▄▄▄▄██▀///███////███ ███////////███▌///███////███/███/////////////88")
            print(Fore.GREEN + "88////▀▀███ ████▄//▀▀███▀▀▀▀▀///▀███████████ ███////////███▌ ▀███████████/▀███████████////88")
            print(Fore.GREEN + "88//////███////███/▀███████████///███////███ ███/// █▄//███////███////███//////////███////88")
            print(Fore.GREEN + "88//////███////███///███////███///███////███ ███/// ███ ███////███////███///▄█////███/////88")
            print(Fore.GREEN + "88//////████████▀////███////███///███////█▀  ████████▀  █▀/////███////█▀///▄████████▀/////88")
            print(Fore.GREEN + "88///////////////////███////███///////////////////////////////////////////////////////////88")
            print(Fore.GREEN + "88////////////////////////////////////////////////////////////////////////////////////////88")
            print(Fore.GREEN + "88////////////////////////////////////////////////////////////////////////////////////////88")
            print(Fore.GREEN + "*==========================================================================================*")
                    
            
            
            
            break 
