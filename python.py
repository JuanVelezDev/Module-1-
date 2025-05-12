producto=input("Introduce el nombre de producto: ")
preciounitario=float(input("Introduce el precio del producto "))
cantidad=int(input("Introduce la cantidad de los productos obtenidos "))
descuento=float(input("Introduce el descuento del producto "))

preciounitario<0 or cantidad or descuento< 0 or descuento>100



costosindescuento=preciounitario*cantidad
montodedescuento=descuento/100 * costosindescuento
costototal= costosindescuento - montodedescuento


print("EL producto es:", producto)
print("El precio unitario es:", preciounitario)
print(f"La cantidad es de: {cantidad} producto") 
print ("El Descuento aplicado es de:" , descuento)
print("El costo total fue:" , costototal)