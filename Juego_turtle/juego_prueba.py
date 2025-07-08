import turtle  #pygames
import random

# Ventana
ventana = turtle.Screen()
ventana.title("Recolector de Estrellas")
ventana.bgcolor("cyan") #RGB (RED GREEN BLUE, 155,20,0)
ventana.setup(width=600 , height=600)



# # Jugador
jugador = turtle.Turtle()
jugador.shape("turtle")
jugador.color("white")
jugador.penup()
jugador.speed(0)

# # Estrella (objetivo)
estrella = turtle.Turtle()
estrella.shape("circle")
estrella.color("yellow")
estrella.penup()
estrella.goto(random.randint(-250, 250), random.randint(-250, 250))

# # Puntuación

puntaje = 0
texto = turtle.Turtle()
texto.hideturtle()
texto.penup()
texto.color("white")
texto.goto(0, 260)
texto.write("Puntaje: 0", align="center", font=("Arial", 16, "bold"))

# # Movimiento
def arriba():
    y = jugador.ycor()
    jugador.sety(y + 20)

def abajo():
    y = jugador.ycor()
    jugador.sety(y - 20)

def izquierda():
    x = jugador.xcor()
    jugador.setx(x - 20)

def derecha():
    x = jugador.xcor()
    jugador.setx(x + 20)


#Utilizacion de funciones definidas: arriba, abajo, izquierda, derecha

ventana.listen()
ventana.onkeypress(arriba, "Up")
ventana.onkeypress(abajo, "Down")
ventana.onkeypress(izquierda, "Left")
ventana.onkeypress(derecha, "Right")

# # Lógica principal
def jugar():
    global puntaje
    if jugador.distance(estrella) < 20:
        estrella.goto(random.randint(-250, 250), random.randint(-250, 250))
        puntaje += 1
        texto.clear()
        texto.write(f"Puntaje: {puntaje}", align="center", font=("Arial", 16, "bold"))

    if puntaje >= 5:
        texto.clear()
        texto.write("¡Ganaste!", align="center", font=("Arial", 20, "bold"))
    else:
        ventana.ontimer(jugar, 100)
# Iniciar el juego
jugar()

# Mantener ventana abierta
ventana.mainloop()
