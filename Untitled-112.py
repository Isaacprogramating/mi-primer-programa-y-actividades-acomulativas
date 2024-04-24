def conversion_temperatura():
    """
    Función que convierte grados Celsius a Fahrenheit.
    """
    celsius = float(input("Ingrese grados en Celsius (Valores deben ser sobre -273.15): "))
    
    while celsius < -273.15:
        print("Error, grado bajo 273.15 (cero absoluto). Ingrese grados nuevamente:")
        celsius = float(input())
    
    fahrenheit = celsius * (9/5) + 32
    print(f"Los grados en Fahrenheit son: {fahrenheit} grados")

# Llamada a la función
conversion_temperatura()