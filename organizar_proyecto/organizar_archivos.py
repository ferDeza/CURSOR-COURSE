"""
Script para organizar archivos en una carpeta
Distribuye archivos en subcarpetas según su tipo/extensión
"""

import os
from pathlib import Path
import shutil

# Carpeta objetivo: Downloads del usuario
carpeta_objetivo = Path.home() / "Downloads"

# Diccionario de tipos de archivo y sus extensiones
TIPOS_ARCHIVO = {
    'Imagenes': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp', '.ico', '.tiff'],
    'Documentos': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.xls', '.xlsx', '.ppt', '.pptx'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.m4v'],
    'Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a'],
    'Archivos_Comprimidos': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2'],
    'Codigo': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.php', '.rb', '.go'],
    'Ejecutables': ['.exe', '.msi', '.deb', '.rpm', '.dmg', '.pkg'],
    'Otros': []  # Para archivos sin extensión o extensiones no reconocidas
}


def obtener_tipo_archivo(archivo):
    """
    Determina el tipo de archivo basándose en su extensión.
    
    Args:
        archivo (Path): Ruta al archivo
        
    Returns:
        str: Nombre de la carpeta de tipo correspondiente
    """
    extension = archivo.suffix.lower()
    
    for tipo, extensiones in TIPOS_ARCHIVO.items():
        if extension in extensiones:
            return tipo
    
    # Si no coincide con ningún tipo conocido, va a "Otros"
    return 'Otros'


def organizar_archivos(carpeta_origen=None):
    """
    Organiza los archivos de una carpeta en subcarpetas según su tipo.
    
    Args:
        carpeta_origen (Path, optional): Carpeta a organizar. Si es None, usa carpeta_objetivo
    """
    if carpeta_origen is None:
        carpeta_origen = carpeta_objetivo
    
    # Verificar que la carpeta existe
    if not carpeta_origen.exists():
        print(f"Error: La carpeta {carpeta_origen} no existe.")
        return
    
    if not carpeta_origen.is_dir():
        print(f"Error: {carpeta_origen} no es una carpeta.")
        return
    
    print(f"Organizando archivos en: {carpeta_origen}")
    print("=" * 60)
    
    # Contador de archivos movidos
    archivos_movidos = {tipo: 0 for tipo in TIPOS_ARCHIVO.keys()}
    errores = []
    
    # Iterar sobre todos los archivos en la carpeta
    for item in carpeta_origen.iterdir():
        # Solo procesar archivos, no carpetas
        if item.is_file():
            tipo = obtener_tipo_archivo(item)
            
            # Crear la carpeta de destino si no existe
            carpeta_destino = carpeta_origen / tipo
            carpeta_destino.mkdir(exist_ok=True)
            
            # Ruta completa del archivo de destino
            archivo_destino = carpeta_destino / item.name
            
            # Verificar si ya existe un archivo con el mismo nombre
            if archivo_destino.exists():
                # Agregar número al nombre si ya existe
                contador = 1
                nombre_base = item.stem
                extension = item.suffix
                while archivo_destino.exists():
                    nuevo_nombre = f"{nombre_base}_{contador}{extension}"
                    archivo_destino = carpeta_destino / nuevo_nombre
                    contador += 1
            
            try:
                # Mover el archivo
                shutil.move(str(item), str(archivo_destino))
                archivos_movidos[tipo] += 1
                print(f"✓ {item.name} → {tipo}/")
            except Exception as e:
                error_msg = f"Error al mover {item.name}: {e}"
                errores.append(error_msg)
                print(f"✗ {error_msg}")
    
    # Resumen
    print("\n" + "=" * 60)
    print("RESUMEN DE ORGANIZACIÓN")
    print("=" * 60)
    total_movidos = 0
    for tipo, cantidad in archivos_movidos.items():
        if cantidad > 0:
            print(f"{tipo}: {cantidad} archivo(s)")
            total_movidos += cantidad
    
    if total_movidos == 0:
        print("No se encontraron archivos para organizar.")
    else:
        print(f"\nTotal: {total_movidos} archivo(s) organizado(s)")
    
    if errores:
        print(f"\nErrores: {len(errores)}")
        for error in errores:
            print(f"  - {error}")


def main():
    """
    Función principal del script.
    """
    print("=" * 60)
    print("ORGANIZADOR DE ARCHIVOS")
    print("=" * 60)
    print(f"\nCarpeta objetivo: {carpeta_objetivo}")
    
    # Confirmar antes de organizar
    respuesta = input("\n¿Deseas organizar los archivos? (s/n): ").strip().lower()
    
    if respuesta in ['s', 'si', 'sí', 'y', 'yes']:
        organizar_archivos()
    else:
        print("Operación cancelada.")


if __name__ == '__main__':
    main()

