def greetings(name:str="Juan!")->str:  
     result:str ="Hello" +name
     return result

print(greetings())


def numbers(numer1:int=1, number2:int=2):
    result:int= numer1 + number2
    return result

print(numbers())



def area_circulo(radio:float = 0):
    radio = float(input("Ingrese el radio: ")) 
    area:float=(3.1416 * radio**2)
    return print(area)

area_circulo()

def es_par(number:int=0):
    number=int(input("Ingrese un numero: "))
    if number %2 ==0:
        print("El numero es par")
    else:
        print("El numero es impar")    
     

es_par()


def numero_mayor(num1:int=0, num2:int=0, num3:int=0):
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    num3 = int(input("Ingrese el tercero numero: "))
    if num1 > num2:
        print(f"El numero mayor es {num1}")
    elif    num2 > num3:
        print(f"El numero mayor es {num2}")
    else:
        print(f"El numero mayor es {num3}")


numero_mayor()


def contar_vocales(text:str=""):
    text:str=input("Ingrese una palabra: ")
    vowels:str="aeiouAEIOU"
    count:int=0
    for char in text:
        if char in vowels:
            count += 1
    return print(count)

contar_vocales()     


def es_palindromo():
    word=input("Ingresa una palabra: ")
    result=word=word-1
    if int (result) == True:
        print(f"La palabra {word} es palindromo")
        return 
    else:
        print(f"La palabras {word} no es un palindromo")
        return
    

es_palindromo()


def es_palindromo():
    palabra=input("Ingrese una palabra: ")
    return palabra==palabra[::-1]

print(es_palindromo())


def celsius_farenheit():
    cel:float=float(input("Ingresa una temperatura para convertir a farenheit: "))
    f:float=float ((cel * 9/5) + 32)
    return f"Le temperatura en farenheit es: {f}"


print(celsius_farenheit())


     
