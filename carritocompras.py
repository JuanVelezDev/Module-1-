nombre1= input("Ingrese el nombre del primer producto: ")
precio1= float(input("Ingrese el precio del primer producto: "))

nombre2= input("Ingrese el nombre del segundo producto: ")
precio2= float(input("Ingrese el precio del segundo producto: "))

nombre3= input("Ingrese el nombre del tercer producto: ")
precio3= float(input("Ingrese el precio del tercer producto: "))

Total= precio1 + precio2 + precio3 
print("El total de la compra es:", Total)

if Total < 50000:
    metodo= "Efectivo"
    Beneficio= "5% Descuento"
    Totalfinal= Total * 0.95
elif Total >= 50000 and Total <= 100000:
    metodo= "Tarjeta"
    Beneficio= "Sin cambios"
    Totalfinal= Total
else: 
    metodo= "Tranferencia"
    Beneficio= "2 % Cashback"
    Cashback=  Total * 00.2
    Totalfinal= Total 

print("Metodo recomendado", metodo)
print("Beneficio: ", Beneficio)
print("Total a pagar: ", Totalfinal)
