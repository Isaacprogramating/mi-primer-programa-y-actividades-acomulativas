def sumar(a, b):
    """
    Función que suma dos números.
    
    Args:
        a (float): Primer número.
        b (float): Segundo número.
        
    Returns:
        float: Resultado de la suma.
    """
    return a + b

def restar(a, b):
    """
    Función que resta dos números.
    
    Args:
        a (float): Minuendo.
        b (float): Sustraendo.
        
    Returns:
        float: Resultado de la resta.
    """
    return a - b

def multiplicar(a, b):
    """
    Función que multiplica dos números.
    
    Args:
        a (float): Primer factor.
        b (float): Segundo factor.
        
    Returns:
        float: Resultado de la multiplicación.
    """
    return a * b

def dividir(a, b):
    """
    Función que divide dos números.
    
    Args:
        a (float): Dividendo.
        b (float): Divisor.
        
    Returns:
        float: Resultado de la división.
        
    Raises:
        ZeroDivisionError: Si el divisor es cero.
    """
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero.")
    return a / b

# Ejemplo de uso
print("Calculadora")
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

operacion = input("Ingrese la operación (+, -, *, /): ")

if operacion == "+":
    resultado = sumar(num1, num2)
    print(f"El resultado de {num1} + {num2} es: {resultado}")
elif operacion == "-":
    resultado = restar(num1, num2)
    print(f"El resultado de {num1} - {num2} es: {resultado}")
elif operacion == "*":
    resultado = multiplicar(num1, num2)
    print(f"El resultado de {num1} * {num2} es: {resultado}")
elif operacion == "/":
    try:
        resultado = dividir(num1, num2)
        print(f"El resultado de {num1} / {num2} es: {resultado}")
    except ZeroDivisionError as e:
        print(e)
else:
    print("Operación inválida.")