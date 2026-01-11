# Bloc de Notas (Notepad) - Aplicación de Escritorio

Aplicación de bloc de notas simplificado creada con Tkinter, la biblioteca gráfica estándar incluida con Python.

## Descripción

Esta es una aplicación de escritorio que proporciona una interfaz gráfica para editar archivos de texto. Incluye funcionalidades básicas como crear, abrir, guardar archivos y edición de texto.

## Características

- ✅ Interfaz gráfica intuitiva con Tkinter
- ✅ Área de texto multi-línea con scroll
- ✅ Crear nuevos archivos de texto
- ✅ Abrir archivos de texto existentes
- ✅ Guardar archivos (Guardar y Guardar Como)
- ✅ Menú completo (Archivo, Editar, Ayuda)
- ✅ Atajos de teclado
- ✅ Barra de estado con información del cursor
- ✅ Operaciones de edición: Deshacer, Rehacer, Cortar, Copiar, Pegar
- ✅ Confirmación antes de cerrar si hay cambios sin guardar

## Requisitos

- Python 3.6 o superior
- Tkinter (incluido por defecto en la mayoría de instalaciones de Python)

**Nota**: Tkinter viene preinstalado con Python en la mayoría de sistemas. Si no lo tienes:

- **Windows**: Generalmente viene incluido
- **Linux**: Puede necesitar instalarse: `sudo apt-get install python3-tk`
- **macOS**: Viene incluido con Python

## Instalación

No se requieren instalaciones adicionales. Tkinter está incluido en Python.

## Uso

### Ejecutar la aplicación

```bash
cd notepad_proyecto
python notepad.py
```

### Funcionalidades

#### Menú Archivo

- **Nuevo** (Ctrl+N): Crea un nuevo archivo
- **Abrir** (Ctrl+O): Abre un archivo de texto existente
- **Guardar** (Ctrl+S): Guarda el archivo actual
- **Guardar Como** (Ctrl+Shift+S): Guarda con un nombre nuevo
- **Salir**: Cierra la aplicación

#### Menú Editar

- **Deshacer** (Ctrl+Z): Deshace la última acción
- **Rehacer** (Ctrl+Y): Rehace la acción deshecha
- **Cortar** (Ctrl+X): Corta el texto seleccionado
- **Copiar** (Ctrl+C): Copia el texto seleccionado
- **Pegar** (Ctrl+V): Pega el texto del portapapeles
- **Seleccionar Todo** (Ctrl+A): Selecciona todo el texto

#### Barra de Estado

La barra de estado en la parte inferior muestra:
- Nombre del archivo actual
- Línea y columna del cursor
- Número total de líneas y caracteres

## Estructura del Proyecto

```
notepad_proyecto/
├── notepad.py      # Aplicación principal
└── README.md       # Este archivo
```

## Ejemplo de Uso

1. Ejecuta la aplicación: `python notepad.py`
2. Escribe texto en el área de texto
3. Usa **Archivo → Guardar Como** para guardar tu nota
4. Usa **Archivo → Abrir** para cargar un archivo existente
5. Edita el texto usando las opciones del menú Editar
6. Observa la información del cursor en la barra de estado

## Capturas de Pantalla

La aplicación muestra:
- Una ventana principal con área de texto grande
- Menú superior con opciones de Archivo, Editar y Ayuda
- Barra de estado en la parte inferior con información del cursor
- Interfaz limpia y fácil de usar

## Personalización

Puedes personalizar la aplicación modificando:

- **Fuente**: Cambia `font=("Consolas", 11)` en `crear_widgets()`
- **Tamaño de ventana**: Modifica `self.root.geometry("800x600")`
- **Colores**: Cambia `bg` y `fg` en el área de texto
- **Tipos de archivo**: Modifica `filetypes` en los diálogos de archivo

## Notas

- La aplicación guarda archivos con codificación UTF-8
- Soporta archivos de texto (.txt) por defecto
- Muestra confirmación antes de cerrar si hay cambios sin guardar
- Usa ScrolledText para manejar texto largo automáticamente

## Desarrollo Futuro

Posibles mejoras:
- Soporte para múltiples pestañas
- Búsqueda y reemplazo de texto
- Numeración de líneas
- Temas de color (modo oscuro/claro)
- Soporte para más formatos de archivo (Markdown, etc.)

