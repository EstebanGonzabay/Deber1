import turtle
import math
import random

# POO (Programacion orientada a objetos)
# Funciones


# --- Configuración inicial de la pantalla ---
ventana = turtle.Screen()
ventana.title("Mini Pac-Man Nivel 1")
ventana.bgcolor("black")
ventana.setup(width=700, height=700)
ventana.tracer(0)  # Desactiva animación automática para mejor rendimiento

# --- Registro de sprites personalizados (opcional) ---
# ventana.register_shape("pacman.gif")
# ventana.register_shape("ghost.gif")

# --- Creación de los actores del juego ---
class Jugador(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.speed(0)
        self.direccion = "stop"

    def mover(self):
        x, y = self.xcor(), self.ycor()
        if self.direccion == "up":
            self.sety(y + 24)
        elif self.direccion == "down":
            self.sety(y - 24)
        elif self.direccion == "left":
            self.setx(x - 24)
        elif self.direccion == "right":
            self.setx(x + 24)

    def direccion_arriba(self):
        self.direccion = "up"

    def direccion_abajo(self):
        self.direccion = "down"

    def direccion_izquierda(self):
        self.direccion = "left"

    def direccion_derecha(self):
        self.direccion = "right"

# --- Clase para paredes ---
class Pared(turtle.Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.goto(x, y)

# --- Clase para puntos comestibles ---
class Punto(turtle.Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed(0)
        self.goto(x, y)

# --- Mapa del nivel 1: W = wall, . = punto ---
nivel1 = [
    "WWWWWWWWWWWWWW",
    "W............W",
    "W.WWW.WWWW.W.W",
    "W............W",
    "W.WWW.WWWW.W.W",
    "W............W",
    "WWWWWWWWWWWWWW"
]

# Listas para almacenar objetos
paredes = []
puntos = []

# --- Función para construir el nivel ---
def construir_nivel(mapa):
    for y in range(len(mapa)):
        for x in range(len(mapa[y])):
            caracter = mapa[y][x]
            pos_x = -288 + (x * 48)
            pos_y = 288 - (y * 48)

            if caracter == "W":
                pared = Pared(pos_x, pos_y)
                paredes.append(pared)
            elif caracter == ".":
                punto = Punto(pos_x, pos_y)
                puntos.append(punto)

# --- Crear jugador y construir mapa ---
jugador = Jugador()
construir_nivel(nivel1)

# --- Control del teclado ---
ventana.listen()
ventana.onkeypress(jugador.direccion_arriba, "Up")
ventana.onkeypress(jugador.direccion_abajo, "Down")
ventana.onkeypress(jugador.direccion_izquierda, "Left")
ventana.onkeypress(jugador.direccion_derecha, "Right")

# --- Lógica de colisiones (muy simple) ---
def colision_con_punto():
    for punto in puntos:
        if jugador.distance(punto) < 20:
            punto.hideturtle()
            puntos.remove(punto)

# --- Bucle principal del juego ---
def bucle_juego():
    jugador.mover()
    colision_con_punto()

    # Condición de victoria
    if len(puntos) == 0:
        print("¡Ganaste!")
        return

    ventana.update()
    ventana.ontimer(bucle_juego, 200)

bucle_juego()
ventana.mainloop()
