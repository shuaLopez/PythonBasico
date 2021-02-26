#Hoja de Trabajo 2

#Ejercicio 1

contraseña0M = input("Ingrese la contraseña que desea guardar: ")
contraseña0m = contraseña0M.lower()
contraseña1M = input("Ingrese su contraseña: ")
contraseña1m = contraseña1M.lower()

if contraseña0m == contraseña1m:
    print("La contraseña es correcta")
else:
    print("La contraseña es incorrecta")

#Ejercicio 2

sexoM = input("Ingrese M si es hombre y F si es mujer: ")
sexom = sexoM.lower()
nombreM = input("Ingrese su nombre: ")
nombrem = nombreM.lower()

if sexom == "f":
    if nombrem[0] < "m":
        print("Le corresponde el Grupo A")
    else:
        print("Le corresponde el Grupo B")
elif sexom == "m":
    if nombrem[0] > "n":
        print("Le corresponde el Grupo A")
    else:
        print("Le corresponde el Grupo B")