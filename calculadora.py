def suma(a, b):
    """Función para sumar dos números"""
    return a + b

def resta(a, b):
    """Función para restar dos números"""
    return a - b

def multiplicacion(a, b):
    """Función para multiplicar dos números"""
    return a * b

def division(a, b):
    """Función para dividir dos números"""
    if b == 0:
        return None  # Retorna None si se intenta dividir por cero
    return a / b

def calculadora():
    """Calculadora interactiva con ciclo while para múltiples operaciones"""
    print("=== CALCULADORA ===")
    print("Operaciones disponibles:")
    print("1. Suma (+)")
    print("2. Resta (-)")
    print("3. Multiplicación (*)")
    print("4. División (/)")
    print("5. Salir")
    
    while True:
        # Solicitar operación al usuario
        print("\n" + "-" * 30)
        operacion = input("Selecciona una operación (1-5): ").strip()
        
        # Salir del programa
        if operacion == "5":
            print("¡Hasta luego!")
            break
        
        # Validar que la operación sea válida
        if operacion not in ["1", "2", "3", "4"]:
            print("❌ Operación no válida. Por favor, selecciona una opción del 1 al 5.")
            continue
        
        # Solicitar valores al usuario
        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
        except ValueError:
            print("❌ Error: Por favor, ingresa números válidos.")
            continue
        
        # Realizar la operación seleccionada
        resultado = None
        simbolo = ""
        
        if operacion == "1":
            resultado = suma(num1, num2)
            simbolo = "+"
        elif operacion == "2":
            resultado = resta(num1, num2)
            simbolo = "-"
        elif operacion == "3":
            resultado = multiplicacion(num1, num2)
            simbolo = "*"
        elif operacion == "4":
            resultado = division(num1, num2)
            simbolo = "/"
            if resultado is None:
                print("❌ Error: No se puede dividir por cero.")
                continue
        
        # Mostrar el resultado
        print(f"\n✅ Resultado: {num1} {simbolo} {num2} = {resultado}")

# Ejecutar la calculadora
if __name__ == "__main__":
    calculadora()

