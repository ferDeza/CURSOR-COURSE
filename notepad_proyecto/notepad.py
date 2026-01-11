"""
Aplicación de Bloc de Notas (Notepad) simplificado
Creado con Tkinter - Biblioteca gráfica estándar de Python
"""

import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox
import os


class NotepadApp:
    """Clase principal para la aplicación de bloc de notas"""
    
    def __init__(self, root):
        """
        Inicializa la aplicación
        
        Args:
            root: Ventana principal de Tkinter
        """
        self.root = root
        self.root.title("Bloc de Notas")
        self.root.geometry("800x600")
        
        # Variable para rastrear el archivo actual
        self.archivo_actual = None
        
        # Crear la interfaz
        self.crear_menu()
        self.crear_widgets()
        
        # Centrar la ventana
        self.centrar_ventana()
    
    def centrar_ventana(self):
        """Centra la ventana en la pantalla"""
        self.root.update_idletasks()
        ancho = self.root.winfo_width()
        alto = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (ancho // 2)
        y = (self.root.winfo_screenheight() // 2) - (alto // 2)
        self.root.geometry(f'{ancho}x{alto}+{x}+{y}')
    
    def crear_menu(self):
        """Crea la barra de menú"""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # Menú Archivo
        menu_archivo = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Archivo", menu=menu_archivo)
        menu_archivo.add_command(label="Nuevo", command=self.nuevo_archivo, accelerator="Ctrl+N")
        menu_archivo.add_command(label="Abrir", command=self.abrir_archivo, accelerator="Ctrl+O")
        menu_archivo.add_command(label="Guardar", command=self.guardar_archivo, accelerator="Ctrl+S")
        menu_archivo.add_command(label="Guardar Como", command=self.guardar_como, accelerator="Ctrl+Shift+S")
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Salir", command=self.salir)
        
        # Menú Editar
        menu_editar = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Editar", menu=menu_editar)
        menu_editar.add_command(label="Deshacer", command=lambda: self.area_texto.event_generate("<<Undo>>"), accelerator="Ctrl+Z")
        menu_editar.add_command(label="Rehacer", command=lambda: self.area_texto.event_generate("<<Redo>>"), accelerator="Ctrl+Y")
        menu_editar.add_separator()
        menu_editar.add_command(label="Cortar", command=lambda: self.area_texto.event_generate("<<Cut>>"), accelerator="Ctrl+X")
        menu_editar.add_command(label="Copiar", command=lambda: self.area_texto.event_generate("<<Copy>>"), accelerator="Ctrl+C")
        menu_editar.add_command(label="Pegar", command=lambda: self.area_texto.event_generate("<<Paste>>"), accelerator="Ctrl+V")
        menu_editar.add_separator()
        menu_editar.add_command(label="Seleccionar Todo", command=lambda: self.area_texto.tag_add("sel", "1.0", "end"), accelerator="Ctrl+A")
        
        # Menú Ayuda
        menu_ayuda = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Ayuda", menu=menu_ayuda)
        menu_ayuda.add_command(label="Acerca de", command=self.mostrar_acerca_de)
        
        # Atajos de teclado
        self.root.bind('<Control-n>', lambda e: self.nuevo_archivo())
        self.root.bind('<Control-o>', lambda e: self.abrir_archivo())
        self.root.bind('<Control-s>', lambda e: self.guardar_archivo())
        self.root.bind('<Control-S>', lambda e: self.guardar_como())
    
    def crear_widgets(self):
        """Crea los widgets de la interfaz"""
        # Área de texto con scroll
        self.area_texto = scrolledtext.ScrolledText(
            self.root,
            wrap=tk.WORD,
            undo=True,
            font=("Consolas", 11),
            bg="white",
            fg="black"
        )
        self.area_texto.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Barra de estado
        self.barra_estado = tk.Label(
            self.root,
            text="Listo",
            bd=1,
            relief=tk.SUNKEN,
            anchor=tk.W
        )
        self.barra_estado.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Bind para actualizar barra de estado
        self.area_texto.bind('<KeyRelease>', self.actualizar_barra_estado)
        self.area_texto.bind('<Button-1>', self.actualizar_barra_estado)
    
    def actualizar_barra_estado(self, event=None):
        """Actualiza la barra de estado con información del cursor"""
        linea, columna = self.area_texto.index(tk.INSERT).split('.')
        total_lineas = self.area_texto.index('end-1c').split('.')[0]
        total_caracteres = len(self.area_texto.get("1.0", "end-1c"))
        
        nombre_archivo = os.path.basename(self.archivo_actual) if self.archivo_actual else "Sin título"
        self.barra_estado.config(
            text=f"Archivo: {nombre_archivo} | Línea: {linea}/{total_lineas} | Columna: {int(columna)+1} | Caracteres: {total_caracteres}"
        )
    
    def nuevo_archivo(self):
        """Crea un nuevo archivo"""
        if self.hay_cambios_sin_guardar():
            if not self.confirmar_guardar():
                return
        
        self.area_texto.delete("1.0", tk.END)
        self.archivo_actual = None
        self.root.title("Bloc de Notas - Sin título")
        self.actualizar_barra_estado()
    
    def abrir_archivo(self):
        """Abre un archivo de texto existente"""
        if self.hay_cambios_sin_guardar():
            if not self.confirmar_guardar():
                return
        
        archivo = filedialog.askopenfilename(
            title="Abrir archivo",
            filetypes=[
                ("Archivos de texto", "*.txt"),
                ("Todos los archivos", "*.*")
            ]
        )
        
        if archivo:
            try:
                with open(archivo, 'r', encoding='utf-8') as f:
                    contenido = f.read()
                
                self.area_texto.delete("1.0", tk.END)
                self.area_texto.insert("1.0", contenido)
                self.archivo_actual = archivo
                self.root.title(f"Bloc de Notas - {os.path.basename(archivo)}")
                self.actualizar_barra_estado()
                self.barra_estado.config(text="Archivo cargado correctamente")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo abrir el archivo:\n{str(e)}")
    
    def guardar_archivo(self):
        """Guarda el archivo actual"""
        if self.archivo_actual:
            self.guardar_a_archivo(self.archivo_actual)
        else:
            self.guardar_como()
    
    def guardar_como(self):
        """Guarda el archivo con un nombre nuevo"""
        archivo = filedialog.asksaveasfilename(
            title="Guardar archivo como",
            defaultextension=".txt",
            filetypes=[
                ("Archivos de texto", "*.txt"),
                ("Todos los archivos", "*.*")
            ]
        )
        
        if archivo:
            self.guardar_a_archivo(archivo)
            self.archivo_actual = archivo
            self.root.title(f"Bloc de Notas - {os.path.basename(archivo)}")
    
    def guardar_a_archivo(self, archivo):
        """Guarda el contenido en un archivo"""
        try:
            contenido = self.area_texto.get("1.0", "end-1c")
            with open(archivo, 'w', encoding='utf-8') as f:
                f.write(contenido)
            self.barra_estado.config(text="Archivo guardado correctamente")
            messagebox.showinfo("Guardado", "Archivo guardado exitosamente")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar el archivo:\n{str(e)}")
    
    def hay_cambios_sin_guardar(self):
        """Verifica si hay cambios sin guardar"""
        # Por simplicidad, siempre asumimos que hay cambios
        # En una versión más avanzada, podrías rastrear el estado
        return True
    
    def confirmar_guardar(self):
        """Pregunta al usuario si desea guardar los cambios"""
        respuesta = messagebox.askyesnocancel(
            "Guardar cambios",
            "¿Deseas guardar los cambios antes de continuar?"
        )
        
        if respuesta is True:  # Sí
            self.guardar_archivo()
            return True
        elif respuesta is False:  # No
            return True
        else:  # Cancelar
            return False
    
    def salir(self):
        """Cierra la aplicación"""
        if self.hay_cambios_sin_guardar():
            if not self.confirmar_guardar():
                return
        
        self.root.quit()
        self.root.destroy()
    
    def mostrar_acerca_de(self):
        """Muestra información sobre la aplicación"""
        messagebox.showinfo(
            "Acerca de",
            "Bloc de Notas Simplificado\n\n"
            "Aplicación de bloc de notas creada con Tkinter\n"
            "Versión 1.0\n\n"
            "Funcionalidades:\n"
            "- Crear, abrir y guardar archivos de texto\n"
            "- Editar texto con opciones básicas\n"
            "- Interfaz gráfica intuitiva"
        )


def main():
    """Función principal"""
    root = tk.Tk()
    app = NotepadApp(root)
    
    # Manejar cierre de ventana
    root.protocol("WM_DELETE_WINDOW", app.salir)
    
    root.mainloop()


if __name__ == "__main__":
    main()

