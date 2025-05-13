--- ¿Que es Python?

Python es un lenguaje de programación creado por Guido van Rossum
a principios de los años 90 cuyo nombre está inspirado en el grupo de
cómicos ingleses “Monty Python”. Es un lenguaje similar a Perl, pero
con una sintaxis muy limpia y que favorece un código legible.

Se trata de un lenguaje interpretado o de script, con tipado dinámico,
fuertemente tipado, multiplataforma y orientado a objetos.


TIPOS DE NUMEROS EN PYTHON
    ## numeroEntero = 5  
    ## numeroDecimal = 5.0
        "decimal"  numeroDecimalCompuesto = (5,2) = 25555.00
                                                    452546.335
    ## numerosComplejos = 6 + 8j
    ## numerosComplejos = 6.5 + 8.6j
    ## numerosComplejos = 6.5 + 8j


    ***FUERTEMENTE**TIPADO*** 

sumaDeDosNumeros = 5 + "6"




EN CONCEPTOS DE FACILIDAD, NOS QUEDAMOS CON "DOUBLE"
EN SENTIDO DE EFICIENCIA, YO SI Y SI NECESITO SABER QUE TIPO DE DATOS ES CON EL QUE VOY A TRABAJAR POR LA OPTIMIZACION DE RECURSOS




--- #¿Script en Python?

Un lenguaje interpretado o de script se ejecuta mediante un intérprete en lugar de compilarse directamente a lenguaje máquina, como ocurre con los lenguajes compilados, que son más rápidos pero menos flexibles y portables. Python, aunque es interpretado, tiene características de lenguajes compilados, por lo que puede considerarse semi interpretado, ya que su código fuente se traduce primero a un bytecode (archivos .pyc o .pyo) que luego se ejecuta en sucesivas ocasiones, similar a lo que ocurre en Java y otros lenguajes.


--- #¿Fuertemente tipado?

Tipado fuerte: No permite tratar una variable como si fuera de un tipo distinto al que tiene, requiriendo una conversión explícita al nuevo tipo antes de operar.

Ejemplo: No se puede sumar directamente una cadena ("9") y un número (8) sin convertir antes el string a entero.

numero = int("10")  # Resultado: 10 (entero)
texto = str(42)  # Resultado: "42" (string)
texto_decimal = str(5.7)  # Resultado: "5.7" (string)


Mayor robustez: A diferencia de otros lenguajes que cambian automáticamente el tipo de variable (tipado débil), esta restricción reduce errores inesperados.




