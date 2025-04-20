# python/Proyecto_ACME/Modulo/informes.py

from datetime import datetime, timedelta

def generarInformeAsistencia(asistencia, modulos, estudiantes):
    print("\n=== Informe de Asistencia ===")
    
    # Parámetros de tiempo
    retraso_tolerancia = timedelta(minutes=15)
    salida_anticipada_tolerancia = timedelta(minutes=15)

    for cod_modulo, datos_modulo in modulos.items():
        print(f"\nMódulo: {datos_modulo['Nombre']} (Código: {cod_modulo})")
        
        for cod_estudiante, registros in asistencia.items():
            for registro in registros:
                # Obtener la hora de llegada y salida
                hora_llegada = datetime.strptime(registro['horallegada'], "%Y-%m-%d %H:%M:%S")
                hora_salida = datetime.strptime(registro['horasalida'], "%Y-%m-%d %H:%M:%S")
                
                # Obtener horas de inicio y fin del módulo
                hora_inicio = datetime.strptime(datos_modulo['Hora_Inicio'], "%H:%M")
                hora_fin = datetime.strptime(datos_modulo['Hora_Fin'], "%H:%M")
                
                # Verificar si el estudiante llegó tarde
                if hora_llegada > hora_inicio + retraso_tolerancia:
                    print(f"Estudiante: {estudiantes[cod_estudiante]['Nombre']} llegó tarde.")
                
                # Verificar si el estudiante salió temprano
                if hora_salida < hora_fin - salida_anticipada_tolerancia:
                    print(f"Estudiante: {estudiantes[cod_estudiante]['Nombre']} salió antes de terminar la clase.")
                
                # Adicionalmente, podrías agregar otros criterios de consulta

    input("\nPresione cualquier tecla para volver al menú...")
