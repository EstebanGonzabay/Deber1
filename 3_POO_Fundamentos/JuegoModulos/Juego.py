from Personaje import Personaje
from Magic_item import MagicItem
from Magic_item import MagicItem2

class Juego:
    def __init__(self):
        self.heroe = Personaje("Valiente", 100, 20, 1)
        self.enemigo = Personaje("Dragón", 120, 15, 2)
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

            opcion = int(input("Selecciona una opción (1-3): "))

            if opcion == 1:
                self.heroe.atacar(self.enemigo)
            elif opcion == 2:
                self.pocion.usar(self.heroe)
            elif opcion == 3:
                self.espada.usar(self.heroe)
            else:
                print("Opción no válida.")

            if self.enemigo.vida > 0:
                self.enemigo.atacar(self.heroe)

            print("\n--- Estado Actual ---")
            self.heroe.estado()
            self.enemigo.estado()
            turnos += 1

        print("\n--- Fin del juego ---")
        if self.heroe.vida > self.enemigo.vida:
            print("¡Has vencido al Dragón!")
        else:
            print("El Dragón te ha derrotado...")
