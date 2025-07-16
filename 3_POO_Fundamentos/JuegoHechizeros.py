# Clase principal: Personaje
class Character:
    def __init__(self, nombre, vida, ataque, nivel):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.nivel = nivel
        # self.edad = edad  self = this

    def atacar(self, otro_personaje):
        print(f"{self.nombre} ataca a {otro_personaje.nombre} y causa {self.ataque} puntos de daño.")
        otro_personaje.vida -= self.ataque 
        # otro_personaje.vida = otro_personaje.vida - self.ataque
        if otro_personaje.vida < 0:
            otro_personaje.vida = 0

    def estado(self):
        print(f"{self.nombre} - Vida: {self.vida} | Nivel: {self.nivel} | Ataque: {self.ataque}")


# Clase secundaria: Objeto Mágico
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


# Clase del juego principal
class Game:
    def __init__(self):
        self.heroe = Character("Valiente", 100, 20, 1)
        self.enemigo = Character("Dragón", 120, 15, 2)
        # self.terceario = Character("Tercero",50,5,1)
        self.pocion = MagicItem("Poción de vida", "pocion", 30)
        self.espada = MagicItem("Espada mágica", "espada", 10)

    def iniciar(self):
        print("¡Bienvenido a la aventura en el Reino Encantado!\n")
        self.heroe.estado()
        self.enemigo.estado()

        turnos = 0
        while self.heroe.vida > 0 and self.enemigo.vida > 0 and turnos < 5:
            print("\n¿Qué deseas hacer?")
            print("1. Atacar al Dragón")
            print("2. Usar poción de vida")
            print("3. Usar espada mágica")

            opcion = input("Selecciona una opción (1-3): ")

            if opcion == "1":
                self.heroe.atacar(self.enemigo) #otro_personaje
            elif opcion == "2":
                self.pocion.usar(self.heroe)
            elif opcion == "3":
                self.espada.usar(self.heroe)
            else:
                print("Opción no válida.")

            # El dragón contraataca
            if self.enemigo.vida > 0:
                self.enemigo.atacar(self.heroe)

            # Mostrar estados después del turno
            print("\n--- Estado Actual ---")
            self.heroe.estado()
            self.enemigo.estado()
            turnos += 1

        print("\n--- Fin del juego ---")
        if self.heroe.vida > self.enemigo.vida:
            print("¡Has vencido al Dragón! 🏆😍")
        else:
            print("El Dragón te ha derrotado...")


# Ejecutar el juego
if __name__ == "__main__":
    juego = Game()
    juego.iniciar()
