class MagicItem:
    def __init__(self, nombre, tipo, efecto):
        self.nombre = nombre
        self.tipo = tipo
        self.efecto = efecto

    def usar(self, personaje):
        if self.tipo == "pocion":
            personaje.vida += self.efecto
            print(f"{personaje.nombre} usa {self.nombre} y recupera {self.efecto} puntos de vida.")
        elif self.tipo == "espada":
            personaje.ataque += self.efecto
            print(f"{personaje.nombre} equipa {self.nombre} y su ataque aumenta en {self.efecto} puntos.")
