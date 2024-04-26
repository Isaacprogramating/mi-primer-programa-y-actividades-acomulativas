# Solicitar el nombre del producto
producto = input("Ingrese el nombre del producto: ")

# Solicitar el valor del producto
valor_producto = int(input("Ingrese el valor del producto: "))

# Calcular el valor neto (sin IVA)
valor_neto = valor_producto * 0.81

# Imprimir los detalles del producto
print("-----Detalle producto----")
print(f"NOMBRE PRODUCTO: {producto}")
print(f"VALOR PRODUCTO: {valor_producto}")
print(f"VALOR PRODUCTO SIN IVA: {valor_neto}")