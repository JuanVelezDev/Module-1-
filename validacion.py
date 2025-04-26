# Solicita al usuario el nombre del producto
producto = input("Introduce el nombre del producto: ")

# se solicita el precio unitario del producto y lo convierte a número decimal
preciounitario = float(input("Introduce el precio del producto: "))

# se soolicita la cantidad de productos y lo convierte a número entero
cantidad = int(input("Introduce la cantidad de productos obtenidos: "))

# se solicita el descuento y lo convierte a número decimal
descuento = float(input("Introduce el descuento del producto (en porcentaje): "))

# Validación sencilla para asegurarse de que los valores sean positivos y el descuento esté entre 0 y 100
if preciounitario < 0 or cantidad < 0 or descuento < 0 or descuento > 100:
    print("Error: Verifica que los valores sean positivos y el descuento esté entre 0 y 100.")
else:
    # se calcula el costo sin descuento
    costosindescuento = preciounitario * cantidad

    # Calcula el monto del descuento
    montodedescuento = (descuento / 100) * costosindescuento

    # calcula el costo total después de aplicar el descuento
    costototal = costosindescuento - montodedescuento

    # y MUeuestra la información final al usuario
    print("El producto es:", producto)
    print("El precio unitario es:", preciounitario)
    print(f"La cantidad es de: {cantidad} producto(s)")
    print("El descuento aplicado es de:", descuento, "%")
    print("El costo total después del descuento es:", costototal)
