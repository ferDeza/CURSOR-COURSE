"""
Script de análisis de ventas
Analiza datos de ventas desde un archivo CSV y genera gráficos
"""

import csv
from datetime import datetime
from collections import defaultdict
import matplotlib.pyplot as plt

# ============================================================================
# 1. CARGAR DATOS DEL CSV
# ============================================================================

def cargar_datos(archivo_csv='ventas.csv'):
    """
    Carga los datos de ventas desde un archivo CSV.
    
    Args:
        archivo_csv (str): Ruta al archivo CSV con los datos de ventas
        
    Returns:
        list: Lista de diccionarios con los datos de ventas
    """
    ventas = []
    
    try:
        with open(archivo_csv, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                venta = {
                    'fecha': datetime.strptime(row['fecha'], '%Y-%m-%d'),
                    'producto': row['producto'],
                    'cantidad': int(row['cantidad']),
                    'precio': float(row['precio']),
                    'total': int(row['cantidad']) * float(row['precio'])
                }
                ventas.append(venta)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {archivo_csv}")
    except Exception as e:
        print(f"Error al cargar datos: {e}")
    
    return ventas


# ============================================================================
# 2. CALCULAR VENTAS TOTALES POR MES
# ============================================================================

def calcular_ventas_por_mes(ventas):
    """
    Calcula el total de ventas agrupadas por mes.
    
    Args:
        ventas (list): Lista de diccionarios con datos de ventas
        
    Returns:
        dict: Diccionario con claves en formato 'YYYY-MM' y valores de total de ventas
    """
    ventas_por_mes = defaultdict(float)
    
    for venta in ventas:
        mes_clave = venta['fecha'].strftime('%Y-%m')
        ventas_por_mes[mes_clave] += venta['total']
    
    # Convertir a diccionario normal y ordenar por mes
    return dict(sorted(ventas_por_mes.items()))


# ============================================================================
# 3. DETERMINAR PRODUCTO MÁS VENDIDO Y CON MAYOR INGRESOS
# ============================================================================

def producto_mas_vendido(ventas):
    """
    Determina el producto con mayor cantidad de unidades vendidas.
    
    Args:
        ventas (list): Lista de diccionarios con datos de ventas
        
    Returns:
        tuple: (nombre_producto, cantidad_total)
    """
    cantidad_por_producto = defaultdict(int)
    
    for venta in ventas:
        cantidad_por_producto[venta['producto']] += venta['cantidad']
    
    if cantidad_por_producto:
        producto_max = max(cantidad_por_producto.items(), key=lambda x: x[1])
        return producto_max
    return None, 0


def producto_mayor_ingresos(ventas):
    """
    Determina el producto que genera mayores ingresos.
    
    Args:
        ventas (list): Lista de diccionarios con datos de ventas
        
    Returns:
        tuple: (nombre_producto, ingresos_totales)
    """
    ingresos_por_producto = defaultdict(float)
    
    for venta in ventas:
        ingresos_por_producto[venta['producto']] += venta['total']
    
    if ingresos_por_producto:
        producto_max = max(ingresos_por_producto.items(), key=lambda x: x[1])
        return producto_max
    return None, 0


# ============================================================================
# 4. GRAFICAR VENTAS POR MES
# ============================================================================

def graficar_ventas_por_mes(ventas_por_mes):
    """
    Genera un gráfico de barras con las ventas totales por mes.
    
    Args:
        ventas_por_mes (dict): Diccionario con ventas agrupadas por mes
    """
    if not ventas_por_mes:
        print("   ⚠ No hay datos para graficar")
        return
    
    meses = list(ventas_por_mes.keys())
    valores = list(ventas_por_mes.values())
    
    plt.figure(figsize=(12, 6))
    plt.bar(meses, valores, color='steelblue', edgecolor='black')
    plt.title('Ventas Totales por Mes', fontsize=16, fontweight='bold')
    plt.xlabel('Mes (YYYY-MM)', fontsize=12)
    plt.ylabel('Ventas Totales ($)', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', alpha=0.3, linestyle='--')
    plt.tight_layout()
    
    # Guardar el gráfico
    plt.savefig('ventas_por_mes.png', dpi=300, bbox_inches='tight')
    print("   ✓ Gráfico guardado: ventas_por_mes.png")
    plt.close()


# ============================================================================
# 5. GRAFICAR TOP 5 PRODUCTOS POR INGRESOS
# ============================================================================

def calcular_top_productos(ventas, top_n=5):
    """
    Calcula los top N productos por ingresos totales.
    
    Args:
        ventas (list): Lista de diccionarios con datos de ventas
        top_n (int): Número de productos a retornar (default: 5)
        
    Returns:
        list: Lista de tuplas (producto, ingresos) ordenadas por ingresos descendente
    """
    ingresos_por_producto = defaultdict(float)
    
    for venta in ventas:
        ingresos_por_producto[venta['producto']] += venta['total']
    
    # Ordenar por ingresos descendente y tomar los top N
    productos_ordenados = sorted(ingresos_por_producto.items(), key=lambda x: x[1], reverse=True)
    
    return productos_ordenados[:top_n]


def graficar_top_productos(top_productos):
    """
    Genera un gráfico de barras horizontales con los top 5 productos por ingresos.
    
    Args:
        top_productos (list): Lista de tuplas (producto, ingresos)
    """
    if not top_productos:
        print("   ⚠ No hay datos para graficar")
        return
    
    productos = [p[0] for p in top_productos]
    ingresos = [p[1] for p in top_productos]
    
    plt.figure(figsize=(10, 6))
    plt.barh(productos, ingresos, color='coral', edgecolor='black')
    plt.title('Top 5 Productos por Ingresos', fontsize=16, fontweight='bold')
    plt.xlabel('Ingresos Totales ($)', fontsize=12)
    plt.ylabel('Producto', fontsize=12)
    plt.grid(axis='x', alpha=0.3, linestyle='--')
    
    # Agregar valores en las barras
    for i, v in enumerate(ingresos):
        plt.text(v, i, f' ${v:,.2f}', va='center', fontweight='bold')
    
    plt.tight_layout()
    
    # Guardar el gráfico
    plt.savefig('top_productos.png', dpi=300, bbox_inches='tight')
    print("   ✓ Gráfico guardado: top_productos.png")
    plt.close()


# ============================================================================
# FUNCIÓN PRINCIPAL
# ============================================================================

def main():
    """
    Función principal que ejecuta el análisis completo de ventas.
    """
    print("=" * 60)
    print("ANÁLISIS DE VENTAS")
    print("=" * 60)
    
    # 1. Cargar datos
    print("\n1. Cargando datos del CSV...")
    ventas = cargar_datos('ventas.csv')
    print(f"   ✓ {len(ventas)} registros cargados")
    
    # 2. Calcular ventas por mes
    print("\n2. Calculando ventas totales por mes...")
    ventas_por_mes = calcular_ventas_por_mes(ventas)
    
    # 3. Productos destacados
    print("\n3. Analizando productos...")
    producto_cantidad, cantidad_total = producto_mas_vendido(ventas)
    producto_ingresos, ingresos_total = producto_mayor_ingresos(ventas)
    
    print(f"   ✓ Producto más vendido: {producto_cantidad} ({cantidad_total} unidades)")
    print(f"   ✓ Producto con mayor ingresos: {producto_ingresos} (${ingresos_total:,.2f})")
    
    # 4. Graficar ventas por mes
    print("\n4. Generando gráfico de ventas por mes...")
    graficar_ventas_por_mes(ventas_por_mes)
    
    # 5. Graficar top 5 productos
    print("\n5. Generando gráfico de top 5 productos...")
    top_productos = calcular_top_productos(ventas, top_n=5)
    graficar_top_productos(top_productos)
    
    print("\n" + "=" * 60)
    print("Análisis completado")
    print("=" * 60)


if __name__ == '__main__':
    main()

