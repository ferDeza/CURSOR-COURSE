import json
import os

# Archivo JSON para persistencia
ARCHIVO_TAREAS = 'tareas.json'

# Lista global de tareas con ID incremental
tareas = []
contador_id = 1

def cargar_tareas():
    """Carga las tareas desde el archivo JSON"""
    global tareas, contador_id
    if os.path.exists(ARCHIVO_TAREAS):
        try:
            with open(ARCHIVO_TAREAS, 'r', encoding='utf-8') as f:
                data = json.load(f)
                tareas = data.get('tareas', [])
                contador_id = data.get('contador_id', 1)
        except (json.JSONDecodeError, IOError):
            # Si hay error al leer, inicializar con valores por defecto
            tareas = []
            contador_id = 1
    else:
        tareas = []
        contador_id = 1

def guardar_tareas():
    """Guarda las tareas en el archivo JSON"""
    try:
        data = {
            'tareas': tareas,
            'contador_id': contador_id
        }
        with open(ARCHIVO_TAREAS, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except IOError:
        # Si hay error al escribir, simplemente continuar
        pass

def agregar_tarea(texto):
    """Agrega una nueva tarea a la lista con un ID incremental"""
    global contador_id, tareas
    nueva_tarea = {
        'id': contador_id,
        'texto': texto,
        'completada': False
    }
    tareas.append(nueva_tarea)
    contador_id += 1
    guardar_tareas()  # Guardar después de agregar
    return nueva_tarea

def completar_tarea(id):
    """Marca una tarea como completada basándose en su ID"""
    global tareas
    for tarea in tareas:
        if tarea['id'] == id:
            tarea['completada'] = True
            guardar_tareas()  # Guardar después de completar
            return tarea
    return None

# Cargar tareas al importar el módulo
cargar_tareas()

