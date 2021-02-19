#Hoja de Trabajo 0
print("Ingrese su peso en Kilogramos (kg)")
peso = float(input())
print("Ingrese su estatura en Metros (m)")
estatura = float(input())
imc = round(peso/(estatura**2),2)
print("Su índice de masa corporal (IMC) es: ",imc)