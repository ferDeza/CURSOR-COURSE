from flask import Blueprint, render_template, request, redirect, url_for
from app import tasks

# Crear un Blueprint para las rutas principales
main = Blueprint('main', __name__)

@main.route('/')
def index():
    """Ruta principal - página de lista de tareas"""
    return render_template('index.html', tareas=tasks.tareas)

@main.route('/agregar', methods=['POST'])
def agregar():
    """Ruta para agregar una nueva tarea"""
    texto = request.form.get('texto', '').strip()
    if texto:
        tasks.agregar_tarea(texto)
    return redirect(url_for('main.index'))

@main.route('/completar/<int:id>')
def completar(id):
    """Ruta para marcar una tarea como completada"""
    tasks.completar_tarea(id)
    return redirect(url_for('main.index'))

@main.route('/about')
def about():
    """Ruta para la página 'Acerca de'"""
    return render_template('about.html')

