# Organizador de Archivos

Script para organizar archivos en una carpeta, distribuyéndolos en subcarpetas según su tipo/extensión.

## Descripción

Este script organiza automáticamente los archivos de una carpeta (por defecto, la carpeta Downloads) creando subcarpetas según el tipo de archivo y moviendo los archivos a su carpeta correspondiente.

## Características

- Organiza archivos por tipo (Imágenes, Documentos, Videos, Audio, etc.)
- Crea subcarpetas automáticamente según el tipo de archivo
- Evita sobrescribir archivos con el mismo nombre (agrega numeración)
- Muestra un resumen de archivos organizados
- Manejo de errores

## Tipos de Archivos Soportados

El script organiza los archivos en las siguientes categorías:

- **Imagenes**: .jpg, .jpeg, .png, .gif, .bmp, .svg, .webp, .ico, .tiff
- **Documentos**: .pdf, .doc, .docx, .txt, .rtf, .odt, .xls, .xlsx, .ppt, .pptx
- **Videos**: .mp4, .avi, .mkv, .mov, .wmv, .flv, .webm, .m4v
- **Audio**: .mp3, .wav, .flac, .aac, .ogg, .wma, .m4a
- **Archivos_Comprimidos**: .zip, .rar, .7z, .tar, .gz, .bz2
- **Codigo**: .py, .js, .html, .css, .java, .cpp, .c, .php, .rb, .go
- **Ejecutables**: .exe, .msi, .deb, .rpm, .dmg, .pkg
- **Otros**: Cualquier archivo que no coincida con las categorías anteriores

## Uso

### Uso Básico

```bash
python organizar_archivos.py
```

Por defecto, organiza los archivos en la carpeta `Downloads` del usuario.

### Modificar la Carpeta Objetivo

Para cambiar la carpeta objetivo, modifica la variable `carpeta_objetivo` en el script:

```python
carpeta_objetivo = Path.home() / "Downloads"  # Cambia "Downloads" por la carpeta deseada
```

O también puedes usar una ruta absoluta:

```python
carpeta_objetivo = Path("C:/Ruta/A/Tu/Carpeta")
```

### Uso Programático

```python
from organizar_archivos import organizar_archivos
from pathlib import Path

# Organizar una carpeta específica
carpeta = Path("C:/MiCarpeta")
organizar_archivos(carpeta)
```

## Estructura del Proyecto

```
organizar_proyecto/
├── organizar_archivos.py   # Script principal
└── README.md               # Este archivo
```

## Requisitos

- Python 3.6 o superior
- Módulos estándar: `os`, `pathlib`, `shutil` (incluidos en Python)

## Ejemplo de Ejecución

```
============================================================
ORGANIZADOR DE ARCHIVOS
============================================================

Carpeta objetivo: C:\Users\Usuario\Downloads

¿Deseas organizar los archivos? (s/n): s
Organizando archivos en: C:\Users\Usuario\Downloads
============================================================
✓ foto.jpg → Imagenes/
✓ documento.pdf → Documentos/
✓ video.mp4 → Videos/
✓ musica.mp3 → Audio/
...

============================================================
RESUMEN DE ORGANIZACIÓN
============================================================
Imagenes: 15 archivo(s)
Documentos: 8 archivo(s)
Videos: 3 archivo(s)
Audio: 12 archivo(s)

Total: 38 archivo(s) organizado(s)
```

## Notas

- El script **mueve** los archivos, no los copia. Asegúrate de tener una copia de seguridad si es necesario.
- El script no organiza subcarpetas, solo archivos en el nivel raíz de la carpeta objetivo.
- Si un archivo ya existe en la carpeta destino, se agregará un número al nombre (ej: `archivo_1.pdf`).

## Personalización

Puedes personalizar los tipos de archivo modificando el diccionario `TIPOS_ARCHIVO` en el script para agregar o quitar extensiones según tus necesidades.

