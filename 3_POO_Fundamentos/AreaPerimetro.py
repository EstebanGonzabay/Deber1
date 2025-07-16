# import math

# Clase base Figura
class Figura:
    def calcular_area(self):
        # Método genérico, será sobreescrito
        return 0

# Clase Cuadrado
class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        
        return self.lado * self.lado
    def nombre(self):
        return f"Cuadrado: "

# Clase Circulo
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.14 * self.radio * self.radio  # Aprox. de pi
    def nombre(self):
        return f"Circulo: "

# Crear una lista de figuras
figuras = [
    Cuadrado(2),
    Circulo(3),
    Cuadrado(5),
    Circulo(1)
]

# Recorrer la lista y mostrar el área de cada figura
for figura in figuras:
    print(f"Área de {figura.nombre()} : {figura.calcular_area():.2f}")
