import csv
import random
from datetime import datetime, timedelta

# Productos disponibles
productos = [
    'Laptop', 'Mouse', 'Teclado', 'Monitor', 'Auriculares',
    'Webcam', 'Tablet', 'Smartphone', 'Impresora', 'Router',
    'Disco Duro', 'Memoria RAM', 'Procesador', 'Tarjeta Gráfica', 'Fuente de Poder'
]

# Fecha de inicio
fecha_inicio = datetime(2024, 1, 1)
fecha_fin = datetime(2024, 12, 31)

# Generar datos sintéticos
ventas = []
random.seed(42)  # Para resultados reproducibles

# Generar 200 registros de ventas
for _ in range(200):
    fecha = fecha_inicio + timedelta(days=random.randint(0, 365))
    producto = random.choice(productos)
    cantidad = random.randint(1, 10)
    # Precios variados según el producto
    if producto in ['Laptop', 'Smartphone', 'Tablet']:
        precio = round(random.uniform(200.0, 1500.0), 2)
    elif producto in ['Monitor', 'Impresora']:
        precio = round(random.uniform(100.0, 500.0), 2)
    else:
        precio = round(random.uniform(10.0, 150.0), 2)
    
    ventas.append([
        fecha.strftime('%Y-%m-%d'),
        producto,
        cantidad,
        precio
    ])

# Ordenar por fecha
ventas.sort(key=lambda x: x[0])

# Escribir al archivo CSV
with open('ventas.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['fecha', 'producto', 'cantidad', 'precio'])
    writer.writerows(ventas)

print(f'CSV creado exitosamente con {len(ventas)} registros de ventas')
print('Archivo: ventas.csv')

