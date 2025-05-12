
Servidor= "www.riwi.com/"
Puerto= "3080"
N_bd="Pruebo1"
NombreUsuario= "JuanVelez"
Contraseña= "Ingreso20"

urlcorrecta= Servidor + ":" + Puerto + "/" + N_bd + "/" + NombreUsuario + "&" + Contraseña 
print("URL correcta: " + urlcorrecta)


User=input("Ingrese el nombre de usuario")
Password=input("Ingrese la contraseña del usuario")
Puertob=input("Ingrese el puerto")
Pedirbase=input("Ingrese el nombre de la base de datos")
Pedirurl=input("Ingrese la url")

Urlingresada= User= Pedirurl + ":" + Puertob + "/" + Pedirbase + "/" + User + "&" + Password 
print("URL correcta: " + Urlingresada)


if urlcorrecta == Urlingresada:
    print("Acceso concedido")
else:
    print("Acceso denegado")
    print("La URL solicitada no coincide con la URL correcta.")
    print("Por favor, verifique los datos ingresados.")
    




 







    



