# Desarrolla un programa que modele una jerarquía de clases para diferentes 
# tipos de animales. Define una clase base llamada Animal que contenga un 
# atributo nombre y un método hacerSonido(). 
# Luego, crea dos clases hijas: Perro y Gato, que sobrescriban el método hacerSonido() 
# para imprimir un sonido característico de cada animal.
# Por ejemplo, "¡Guau!" para el perro y "¡Miau!" para el gato.
# En el programa principal, crea instancias de Perro y Gato, y 
# llama al método hacerSonido() en cada instancia para verificar su funcionamiento.

#CREA LA CLASE PRINCIPAL

class Animal:
    def __init__(self, nombre, edad, estatura):
        self.nombre = nombre
        self.edad = edad
        self.estatura = estatura
        pass
#creando metodos principales
    def hacerSonido(self):
        print("Hacer sonido")

    def saltar(self):
        print("Estoy saltando")

    
#Clase hija perro

class Perro(Animal):
    #utilizando metodo creado en la clase principal
    def hacerSonido(self):
        print(f"Mi nombre es {self.nombre} tengo {self.edad} años y hago !Guau!")

#Clase hija gato
class Gato(Animal):
    def hacerSonido(self):
        print(f"Mi nombre es {self.nombre} tengo {self.edad} años y hago !Miau!")


# creacion de objetos
#Objeto 1
perro = Perro("Firualis", 5)
gato = Gato("Michi", 10)

perro.hacerSonido()
perro.saltar()
gato.hacerSonido()
gato.saltar()

#Objeto 2

perro1 = Perro("Bethoven", 8)
gato1 = Gato("Pelusa", 9)

perro1.hacerSonido()
gato1.hacerSonido()


    