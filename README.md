# CURSOR-COURSE

Repositorio del curso "Tópicos en Ingeniería de Software" siguiendo los contenidos del curso sobre Cursor disponible en Santander Open Academy.

Este repositorio contiene múltiples proyectos prácticos desarrollados durante el curso, cubriendo diferentes aspectos de programación en Python, desarrollo web con Flask, análisis de datos y automatización.

## Instalación

### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Configuración del Entorno Virtual

1. **Crear el entorno virtual (venv)**
   
   En Windows (PowerShell o CMD):
   ```bash
   python -m venv venv
   ```

2. **Activar el entorno virtual**
   
   En Windows (PowerShell):
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```
   
   En Windows (CMD):
   ```cmd
   venv\Scripts\activate.bat
   ```

3. **Instalar las dependencias**
   
   Una vez activado el entorno virtual, instala las dependencias del proyecto:
   ```bash
   pip install -r requirements.txt
   ```

### Desactivar el Entorno Virtual

Para desactivar el entorno virtual cuando hayas terminado, simplemente ejecuta:
```bash
deactivate
```

## Proyectos Incluidos

Este repositorio contiene los siguientes proyectos:

### 1. Calculadora Básica (`calculadora.py`)

**Descripción**: Calculadora básica en Python que realiza operaciones matemáticas (suma, resta, multiplicación y división). Incluye manejo de errores para valores no numéricos y división por cero.

**Cómo ejecutar**:
```bash
python calculadora.py
```

**Características**:
- Operaciones básicas: suma, resta, multiplicación, división
- Manejo de errores (valores no numéricos, división por cero)
- Interfaz de consola interactiva

---

### 2. Contador (`contador.py`)

**Descripción**: Script simple de contador en Python.

**Cómo ejecutar**:
```bash
python contador.py
```

---

### 3. Aplicación Web Flask - Lista de Tareas (`app/`)

**Descripción**: Aplicación web desarrollada con Flask para gestionar tareas pendientes (to-do list). Permite agregar tareas, marcarlas como completadas, y guarda los datos de forma persistente en un archivo JSON.

**Cómo ejecutar**:
```bash
# Asegúrate de tener el entorno virtual activado y las dependencias instaladas
python app.py
```

Luego abre tu navegador en: `http://localhost:5000`

**Características**:
- Interfaz web moderna y responsive
- Agregar nuevas tareas
- Marcar tareas como completadas
- Persistencia de datos en JSON
- Estructura modular con Blueprints
- Templates HTML organizados

**Estructura**:
```
app/
├── __init__.py          # Factory function para crear la app
├── routes.py            # Rutas de la aplicación
├── tasks.py             # Lógica de gestión de tareas
├── templates/           # Templates HTML
└── static/              # Archivos estáticos (CSS)
```

---

### 4. Análisis de Ventas (`analisis_ventas/`)

**Descripción**: Proyecto de análisis de datos de ventas que procesa un archivo CSV, calcula estadísticas y genera gráficos visuales. Incluye análisis de ventas por mes, productos más vendidos, y visualizaciones con matplotlib.

**Cómo ejecutar**:
```bash
cd analisis_ventas

# Primero, genera datos de ejemplo (si no tienes ventas.csv)
python generar_ventas.py

# Luego ejecuta el análisis
python analisis.py
```

**Requisitos adicionales**:
```bash
pip install matplotlib
```

**Características**:
- Carga y procesa datos desde CSV
- Calcula ventas totales por mes
- Identifica producto más vendido y con mayores ingresos
- Genera gráficos de ventas por mes
- Genera gráfico de top 5 productos por ingresos
- Guarda gráficos como imágenes PNG

**Archivos generados**:
- `ventas_por_mes.png` - Gráfico de barras de ventas mensuales
- `top_productos.png` - Gráfico de barras horizontales del top 5 productos

---

### 5. Organizador de Archivos (`organizar_proyecto/`)

**Descripción**: Script que organiza automáticamente archivos en una carpeta, distribuyéndolos en subcarpetas según su tipo/extensión. Por defecto organiza los archivos en la carpeta Downloads.

**Cómo ejecutar**:
```bash
cd organizar_proyecto
python organizar_archivos.py
```

**Características**:
- Organiza archivos por tipo (Imágenes, Documentos, Videos, Audio, etc.)
- Crea subcarpetas automáticamente
- Previene sobrescritura de archivos
- Muestra resumen de archivos organizados
- Confirmación antes de ejecutar

**Tipos de archivos soportados**:
- Imagenes: .jpg, .png, .gif, etc.
- Documentos: .pdf, .doc, .txt, .xlsx, etc.
- Videos: .mp4, .avi, .mkv, etc.
- Audio: .mp3, .wav, .flac, etc.
- Archivos comprimidos: .zip, .rar, .7z, etc.
- Código: .py, .js, .html, .css, etc.
- Ejecutables: .exe, .msi, etc.

---
### 5. Aplicacion de escritorio NotePad (`notepad_proyecto/`)

**Descripción**: Una aplicación de edición de texto ligera y funcional que replica las capacidades básicas del Bloc de Notas tradicional. Está desarrollada utilizando Tkinter, la biblioteca gráfica estándar de Python, empleando Programación Orientada a Objetos (POO).

**Cómo ejecutar**:
```bash
cd notepad_proyecto
python notepad.py
```

**Características**:
- Manejo de archivos: Crear, abrir y guardar documentos .txt.
- Edición: Cortar, copiar, pegar y usar atajos de teclado (Ctrl+C, Ctrl+V, Ctrl+S).
- Barra de estado: Indica en qué línea estás y cuántos caracteres has escrito.
- Aviso de guardado: Te pregunta si quieres guardar antes de cerrar para no perder información.


---
## Dependencias

Las dependencias principales se encuentran en `requirements.txt`:
- Flask 3.0.0 - Framework web para Python
- Werkzeug 3.0.1 - Utilidades WSGI (incluido con Flask)

**Dependencias adicionales para proyectos específicos**:
- `matplotlib` - Requerido para el proyecto de análisis de ventas
  ```bash
  pip install matplotlib
  ```
