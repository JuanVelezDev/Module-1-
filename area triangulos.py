n = int(input("¿Cuántos triángulos deseas procesar? "))
mayores_a_12 = 0

for i in range(n):
    base = float(input(f"Ingrese la base del triángulo {i+1}: "))
    altura = float(input(f"Ingrese la altura del triángulo {i+1}: "))
    superficie = (base * altura) / 2
    print(f"Triángulo {i+1} - Base: {base}, Altura: {altura}, Superficie: {superficie}")

    if superficie > 12:
        mayores_a_12 += 1

print(f"Cantidad de triángulos con superficie mayor a 12: {mayores_a_12}")