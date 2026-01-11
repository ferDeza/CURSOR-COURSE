# Análisis de Ventas

Proyecto para el análisis de datos de ventas usando Python.

## Estructura del Proyecto

```
analisis_ventas/
├── ventas.csv          # Archivo CSV con datos de ventas
├── generar_ventas.py   # Script para generar datos sintéticos
└── README.md           # Este archivo
```

## Datos de Ventas

El archivo `ventas.csv` contiene datos sintéticos de ventas con las siguientes columnas:

- **fecha**: Fecha de la venta (YYYY-MM-DD)
- **producto**: Nombre del producto vendido
- **cantidad**: Cantidad de unidades vendidas
- **precio**: Precio unitario del producto

## Generar Datos

Para generar nuevos datos sintéticos, ejecuta:

```bash
python generar_ventas.py
```

Esto creará/sobrescribirá el archivo `ventas.csv` con 200 registros de ventas aleatorias.

## Ejemplo de Uso

```python
import csv

with open('ventas.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for fila in reader:
        print(f"{fila['fecha']}: {fila['producto']} - {fila['cantidad']} unidades a ${fila['precio']}")
```

