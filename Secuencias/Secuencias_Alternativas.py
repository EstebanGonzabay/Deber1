#Condicionales  if else (si, sino)

#Secuencia Simple

# edad = int(input("Ingresa la edad: "))

# if edad >= 18:
#     print("ERES MAYOR DE 18 AÑOS")

# print("Programa finalizado")

#Secuencia Doble

# edad = int(input("Ingresa la edad: "))

# if edad >= 18:
#     print("ERES MAYOR DE EDAD PORQUE TIENES MAS DE ", edad)
# else:
#     print("ERES MENOR DE EDAD PORQUE TIENES MENOS DE ", edad)

# print("Programa finalizado")


#Secuencia multiple

#Ingrese por pantalla una nota y segun las condiciones presente el resultado.
#9,10 = sobresaliente
#8 = notable
#6,7 = Buena
#5 = suficiente
#1,2,3,4 = ineficiente


nota = float(input("Ingrese la nota:  "))

if nota >= 1 and nota <= 4:
    print("Ineficiente")

elif nota == 5:
    print("SUFICIENTE")

elif nota == 6 or nota ==7:
    print("BUENO")

elif nota == 8:
    print("Notable")

elif nota == 9 or nota == 10:
    print("Sobresaliente")

else:
    print("ERROR NOTA INVALIDA")

print("PROGRAMA TERMINADO")



