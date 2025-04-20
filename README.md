# proyecto_python_Rodriguez_Daniel### SISGESA - Sistema de Gestión de Asistencia Académica





## 📋 Descripción

SISGESA es un sistema de gestión de asistencia académica desarrollado para ACME Education, una institución educativa dedicada a la formación técnica y profesional. Este sistema permite automatizar el control de asistencia de estudiantes, facilitando la generación de informes para la mejora continua de procesos académicos y administrativos.

## ✨ Características

- ✅ Autenticación de usuarios con encriptación SHA-256
- ✅ Registro y gestión de grupos académicos
- ✅ Registro y gestión de módulos formativos
- ✅ Registro y gestión de estudiantes
- ✅ Registro y gestión de docentes
- ✅ Asignación de estudiantes a grupos y módulos
- ✅ Registro de asistencia con fecha y hora
- ✅ Consultas específicas por código
- ✅ Persistencia de datos mediante archivos JSON
- ✅ Interfaz de consola intuitiva


## 🚀 Instalación

### Requisitos previos

- Python 3.6 o superior
- Sistema operativo compatible (Windows, macOS, Linux)


### Pasos de instalación

1. Clone el repositorio o descargue el código fuente:

```shellscript
git clone https://github.com/su-usuario/sisgesa.git
cd sisgesa
```


2. Verifique la estructura de directorios:

```plaintext
Proyecto_ACME/
├── proyectoAcme.py
├── Modulos/
├── Interfaz/
├── Persistencia/
└── utils/
```


3. Ejecute el archivo principal:

```shellscript
python Proyecto_ACME/proyectoAcme.py
```




## 🔧 Configuración inicial

La primera vez que ejecute el sistema, utilice la contraseña predeterminada:

- **Contraseña**: `SISGESA`


Se recomienda cambiar esta contraseña inmediatamente después del primer inicio de sesión utilizando la opción correspondiente en el menú principal.

## 📚 Estructura del proyecto

```plaintext
Proyecto_ACME/
│
├── proyectoAcme.py          # Archivo principal
│
├── Modulos/                 # Directorio de módulos funcionales
│   ├── limpieza.py
│   ├── estudiantes.py
│   ├── grupo.py
│   ├── modulos.py
│   ├── profesores.py
│   ├── registroasistencia.py
│   ├── relacion_estudiantes.py
│   ├── consultas.py
│   └── ingreso_contra/
│       ├── confIngreso.py
│       └── cambioContra.py
│
├── Interfaz/                # Directorio de interfaz de usuario
│   └── menu.py
│
├── Persistencia/            # Directorio de persistencia de datos
│   ├── persistencia.py
│   └── cargar.py
│
└── utils/                   # Directorio de archivos de datos
    ├── grupos.json
    ├── modulos.json
    ├── estudiantes.json
    ├── docentes.json
    ├── asistencia.json
    ├── asignacion.json
    └── password.json
```

## 💻 Guía de uso

### Menú principal

Al iniciar el sistema, se presentará el siguiente menú:

```plaintext
*==========================================================================================*
88////////////////////////////////////////////////////////////////////////////////////////88
88////////////////////////////////////////////////////////////////////////////////////////88
88//////▄██████▄/////▄████████////▄████████  ▄████████//▄█/////▄████████//▄████████///////88
88//////███////███///███////███///███////███ ███/// ███/███////███////███/███////███//////88
88//////███////█▀////███////███///███////███ ███/// █▀//███▌///███////███/███////█▀///////88
88/////▄███/////////▄███▄▄▄▄██▀///███////███ ███////////███▌///███////███/███/////////////88
88////▀▀███ ████▄//▀▀███▀▀▀▀▀///▀███████████ ███////////███▌ ▀███████████/▀███████████////88
88//////███////███/▀███████████///███////███ ███/// █▄//███////███////███//////////███////88
88//////███////███///███////███///███////███ ███/// ███ ███////███////███///▄█////███/////88
88//////████████▀////███////███///███////█▀  ████████▀  █▀/////███////█▀///▄████████▀/////88
88///////////////////███////███///////////////////////////////////////////////////////////88
88////////////////////////////////////////////////////////////////////////////////////////88
88////////////////////////////////////////////////////////////////////////////////////////88
*==========================================================================================*

MENÚ PRINCIPAL
a. Registro de grupos
b. Registro de módulos
c. Registro de estudiantes
d. Asignación de estudiantes a grupos y módulos
e. Registro de docentes
f. Registro de asistencia
g. Consultas de información
h. Generación de informes
i. Cambio de contraseña
j. Salir del sistema

Seleccione una opción:
```

### Funcionalidades principales

#### a. Registro de grupos

Permite crear nuevos grupos académicos con código, nombre y sigla.

**Ejemplo:**

```plaintext
Ingrese el código del grupo: G001
Ingrese el nombre del grupo: Desarrollo de Software
Ingrese la sigla del grupo: DS
```

#### b. Registro de módulos

Permite registrar módulos académicos con código, nombre y duración en semanas.

**Ejemplo:**

```plaintext
Ingrese el código del módulo: M001
Ingrese el nombre del módulo: Programación en Python
Ingrese la duración en semanas: 16
```

#### c. Registro de estudiantes

Permite registrar estudiantes con código, nombre, sexo y edad.

**Ejemplo:**

```plaintext
Ingrese el código del estudiante: E001
Ingrese el nombre del estudiante: Juan Pérez
Seleccione el sexo (M/F): M
Ingrese la edad: 22
```

#### d. Asignación de estudiantes

Permite asignar estudiantes a grupos y módulos específicos.

**Ejemplo:**

```plaintext
Ingrese el código del estudiante: E001
Ingrese el código del grupo: G001
Seleccione los módulos (entre 1 y 3):
1. M001 - Programación en Python
2. M002 - Bases de Datos
Ingrese los números separados por comas: 1,2
```

#### e. Registro de docentes

Permite registrar docentes con cédula, nombre y asignación de módulos.

**Ejemplo:**

```plaintext
Ingrese la cédula del docente: D001
Ingrese el nombre del docente: María Rodríguez
Seleccione los módulos que impartirá (hasta 3):
1. M001 - Programación en Python
2. M002 - Bases de Datos
3. M003 - Desarrollo Web
Ingrese los números separados por comas: 1,3
```

#### f. Registro de asistencia

Permite registrar la asistencia de estudiantes a módulos específicos.

**Ejemplo:**

```plaintext
Ingrese el código del estudiante: E001
Ingrese el código del módulo: M001

Entrada registrada: 2023-11-15 08:30:45

Al finalizar la sesión, presione Enter para registrar la salida...

Salida registrada: 2023-11-15 10:15:30
```

#### i. Cambio de contraseña

Permite cambiar la contraseña de acceso al sistema.

**Ejemplo:**

```plaintext
Ingrese la contraseña actual: SISGESA
Ingrese la nueva contraseña: NuevaContraseña123
Confirme la nueva contraseña: NuevaContraseña123

Contraseña actualizada correctamente.
```

#### j. Salir del sistema

Cierra el sistema de manera segura, guardando todos los datos pendientes.

## 📊 Estructura de datos

### Estudiantes

```json
{
    "codigo_estudiante": {
        "nombre": "Nombre del Estudiante",
        "sexo": "M/F",
        "edad": 20,
        "grupo": "codigo_grupo",
        "modulos": ["codigo_modulo1", "codigo_modulo2"]
    }
}
```

### Grupos

```json
{
    "codigo_grupo": {
        "nombre": "Nombre del Grupo",
        "sigla": "SG"
    }
}
```

### Módulos

```json
{
    "codigo_modulo": {
        "nombre": "Nombre del Módulo",
        "duracion": 16
    }
}
```

### Docentes

```json
{
    "cedula_docente": {
        "nombre": "Nombre del Docente",
        "modulos": ["codigo_modulo1", "codigo_modulo2"]
    }
}
```

### Asistencia

```json
{
    "registro_id": {
        "codigo_estudiante": "codigo_estudiante",
        "codigo_modulo": "codigo_modulo",
        "fecha_entrada": "YYYY-MM-DD HH:MM:SS",
        "fecha_salida": "YYYY-MM-DD HH:MM:SS"
    }
}
```

## ⚠️ Solución de problemas

### Problemas de persistencia

Si encuentra errores al guardar o cargar datos:

1. **Verifique la estructura de directorios**:

1. Asegúrese de que exista la carpeta `Proyecto_ACME/utils/`
2. Si no existe, créela manualmente



2. **Verifique los permisos de archivos**:

1. El usuario debe tener permisos de lectura y escritura en el directorio `utils/`



3. **Corrija las rutas de archivo**:

1. Las rutas en las funciones de persistencia deben coincidir con la estructura real del proyecto
2. Modifique las rutas en `Persistencia/persistencia.py` y `Persistencia/cargar.py` si es necesario





### Solución implementada para problemas de persistencia

Se ha mejorado el módulo de persistencia para:

```python
# En Persistencia/cargar.py
import json
import os

def cargar_archivo_json(nombre_archivo):
    # Corregir la ruta para que sea relativa al directorio del proyecto
    ruta = f'Proyecto_ACME/utils/{nombre_archivo}.json'
    
    # Verificar si el directorio existe, si no, crearlo
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    
    try:
        with open(ruta, 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print(f"Archivo {nombre_archivo}.json no encontrado. Se creará uno nuevo.")
        return {}
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo {nombre_archivo}.json. Posible formato incorrecto.")
        return {}
```

```python
# En Persistencia/persistencia.py
import json
import os

def guardar(datos, nombre):
    # Corregir la ruta para que sea relativa al directorio del proyecto
    ruta_archivo = f'Proyecto_ACME/utils/{nombre}.json'
    
    # Verificar si el directorio existe, si no, crearlo
    os.makedirs(os.path.dirname(ruta_archivo), exist_ok=True)
    
    try:
        # Intentar cargar el archivo existente
        try:
            with open(ruta_archivo, 'r') as fd:
                contenido = json.load(fd)
                if not isinstance(contenido, dict):
                    print(f"El archivo {nombre}.json no contiene un diccionario. Se creará uno nuevo.")
                    contenido = {}
        except FileNotFoundError:
            contenido = {}
        except json.JSONDecodeError:
            print(f"Error al decodificar el archivo {nombre}.json. Se creará uno nuevo.")
            contenido = {}
        
        # Actualizar el contenido con los nuevos datos
        if datos:
            if isinstance(datos, dict):
                contenido.update(datos)
            else:
                print(f"Advertencia: Los datos para {nombre} no son un diccionario.")
                # Si no es un diccionario, intentar guardar directamente
                contenido = datos
        
        # Guardar los datos actualizados
        with open(ruta_archivo, 'w') as fd:
            json.dump(contenido, fd, indent=4)
        
        print(f"Datos guardados correctamente en {nombre}.json")
        
    except Exception as e:
        print(f"Error al guardar datos en {nombre}.json: {str(e)}")
```

### Otros problemas comunes

#### Error de autenticación

Si no puede acceder al sistema con la contraseña correcta:

1. Verifique que el archivo `password.json` exista y no esté corrupto
2. Si es necesario, elimine el archivo para que el sistema vuelva a la contraseña predeterminada


#### Errores en la entrada de datos

Si se producen errores al ingresar datos:

1. Verifique que esté ingresando los tipos de datos correctos
2. Siga las instrucciones específicas para cada campo




## 🔒 Seguridad

- Las contraseñas se almacenan encriptadas utilizando SHA-256
- No se almacenan datos sensibles en texto plano
- Se implementan validaciones para prevenir entradas incorrectas


## 📝 Consideraciones técnicas

- El sistema está desarrollado en Python puro, sin módulos adicionales
- Se utiliza JSON para la persistencia de datos
- La arquitectura es modular para facilitar el mantenimiento
- Se implementan validaciones para todos los datos ingresados


## 🤝 Contribuciones

Este proyecto fue desarrollado como parte de un ejercicio académico. Si desea contribuir:

1. Realice un fork del repositorio
2. Cree una rama para su funcionalidad (`git checkout -b feature/nueva-funcionalidad`)
3. Realice sus cambios y haga commit (`git commit -m 'Añadir nueva funcionalidad'`)
4. Envíe sus cambios (`git push origin feature/nueva-funcionalidad`)
5. Abra un Pull Request


## 📄 Licencia

Este proyecto está bajo la Licencia [MIT](https://opensource.org/licenses/MIT).

## 👥 Autores

- **Daniel Rodriguez** - *Desarrollo inicial* 


## 🙏 Agradecimientos

- ACME Education por la oportunidad de desarrollar este sistema
- A todos los que contribuyeron con pruebas y sugerencias