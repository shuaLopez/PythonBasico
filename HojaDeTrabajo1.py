#Hoja de Trabajo 1

#Ejercicio 1
print("-----|IMPRIMIR TRIÁNGULO|-----")
asterisco = "*"
base = int(input("Ingrese la base del triángulo: "))
for i in range(base+1):
    print(asterisco * i)

#Ejercicio 2
print("-----|VERIFICAR NÚMERO PRIMO|-----")
numero = int(input("Ingrese el número a verificar: "))
contador = 0
for i in range(1,numero+1):
    if (numero%i)==0:
        contador= contador + 1
if contador == 2:
    print("El número es primo")
else:
    print("El número no es primo")