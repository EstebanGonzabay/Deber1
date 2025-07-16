class Personaje:
    def __init__(self, nombre, vida, ataque, nivel, otro_atributo):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.nivel = nivel

    def atacar(self, otro_personaje):
        print(f"{self.nombre} ataca a {otro_personaje.nombre} y causa {self.ataque} puntos de daño.")
        otro_personaje.vida -= self.ataque
        if otro_personaje.vida < 0:
            otro_personaje.vida = 0

    def estado(self):
        print(f"{self.nombre} - Vida: {self.vida} | Nivel: {self.nivel} | Ataque: {self.ataque}")
