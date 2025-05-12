n=int(input("¿Cuantos numeros desea ingresar?: "))
contador= 0

for i in range(n):
    numero=int(input(f"Ingresa un numero {i +1}: "))
    if  numero >=1000:
        contador += 1 
        print(f"La cantidada de numeros mayores a 1000 es: {contador}")
     
