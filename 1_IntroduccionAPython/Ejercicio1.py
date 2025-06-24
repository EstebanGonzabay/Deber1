# ### Ejercicio 1
# Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.
    # Cadena de caracteres "Hola"
    # Caracter ['h', 'o', 'l', 'a']

# print("Hola Mundo" * int(5)) # lista "lista = [numericos, boleanos, caracteres]""
# print('Hola Mundo')


# ### Ejercicio 2
# Escribir un programa que almacene la cadena ¡Hola Mundo! en una 
# variable y luego muestre por pantalla el contenido de la variable.
    #Siempre vamos a utilizar varibles descriptivas


# cadena_hola_mundo = "!Hola Mudno¡" # snake_case
# print(cadena_hola_mundo)

# ### Ejercicio 3
# Escribir un programa que pregunte el nombre del usuario en la consola
# y después de que el usuario lo introduzca muestre por pantalla la cadena 
# ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.

# nombre_usario = (input("Ingrese nombre: "))
# print("Hola" + nombre_usario)
# print( "Hola" + "5" )

# ### Ejercicio 4
# Escribir un programa que muestre por pantalla el resultado de la siguiente 
# operación aritmética 
# 3+2 / 2.5 elevado al cuadrado

# resultado_operacion = ((3+2)/(2*5)) ** 2
# print(resultado_operacion)


# ### Ejercicio 5
# Escribir un programa que pregunte al usuario por el número de horas trabajadas y 
# el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

# numero_horas = int(input("Ingrese numero de horas trabajadas:\n"))
# valor_por_hora = float(input("Ingrese $ por hora:\n"))

# paga_total = numero_horas * valor_por_hora

# print("La paga es:\n", paga_total)


# ### Ejercicio 6
# Escribir un programa que lea un entero positivo,introducido por el usuario y después muestre en pantalla la suma 
# de todos los enteros desde 1 hasta 
# . La suma de los 
# #  primeros enteros positivos puede ser calculada de la siguiente forma:

    ## bucle for   se lo utiliza solo y solo si se cuantas iteraciones voy a tener
    ## bucle while va a iterar las veces que sean necesarias y que no esten especificadas
    ## bucle do while

# entero_positivo = int(input("Ingrese numero entero: "))

# suma = (entero_positivo*(entero_positivo+1))/2

# print(suma)


# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice 
# de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa 
# corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales

peso_usuario = float(input("Ingrese el peso en libras: "))
estatura_usuario = float(input("Ingrese la estatura del usuario en metros: "))

imc = peso_usuario/(estatura_usuario*2)

indice_masa_corporal = round(imc, 2)

#round es una palabra reservada, son palabras que python las contiene y son utilizadas para ciertos procesos

print("El indice de masa corporal es: ", indice_masa_corporal)

# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por 
# correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso 
# de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. 
# Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso 
# total del paquete que será enviado.

peso_payasos = 112 
peso_muniecas = 75

cantidad_payasos = int (input("Ingrese la cantidad de payasos: "))
cantidad_muniecas = int (input("Ingrese la cantidad de muñecas: "))

peso_total_payasos = cantidad_payasos * peso_payasos
peso_total_muniecas = cantidad_muniecas * peso_muniecas

print("El peso total de la caja de payasos es: ", peso_total_payasos
      , "\nEl peso total de muñecas es: ", peso_total_muniecas)


