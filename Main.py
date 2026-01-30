"""
    Un documento CSV hecho por IA con preguntas y respuestas y otro de jugadores.csv donde se guardan,
    efectivamente, los jugadores. Los jugadores se registran con nombre.
    Si ya existe, sigue con la partida según estaba. Si no existe empieza de cero.
    Al final de la partida, dice el número de aciertos y fallos.
    Si has terminado la partida e introduces el mismo nombre avisas de que se reinicia la partida.
    Si introduces el nombre "ranking" te muestra, efectivamente, el ranking.
    El ranking de jugadores que han terminado.
    Para trastornados mentales hacer que las preguntas sean aleatorias

"""
from Jugador import Jugador

ficheroPreguntas = "trivia_cultura_general.csv"
ficheroJugadores = "jugadores.csv"

def devolverDatos():
    opcion = int(input("Elige una pregunta: "))
    with open(ficheroPreguntas, "r", encoding="utf-8") as f:
        lineas = f.read().splitlines()
    datos = lineas[opcion].split(",")
    pregunta = datos[0]
    respuestas = datos[1:5]
    correcta = datos[5]
    return pregunta, respuestas, correcta


def menu():
    with open(ficheroPreguntas, "r", encoding="utf-8") as f:
        lineas = f.read().splitlines()

    print("Elige una opción: ")
    indice = 0
    for l in lineas:
        print(f"[{indice}] {l}")
        indice += 1



def addJugador():
    tupla = []
    jugador = Jugador(input("Introduzca su nombre: "))
    tupla.append(jugador.getNombre())
    tupla.append(jugador.getId())
    return tupla

def addInfo():
    tupla = addJugador()
    info = ""
    for i in range(len(tupla)-1):
        info += f"{tupla[i]}, "
    info += f"{tupla[-1]}\n"
    with open(ficheroJugadores, "a") as f:
        f.write(info)

def buscarJugador():
    buscarJugador = input("Introduzca su ID: ")
    with open(ficheroJugadores, "r", encoding="utf-8") as f:
        lineas = f.read().splitlines()
        for linea in lineas:
            if buscarJugador in linea:
                return linea[0]
        return False

seguir = True
aciertos = 0
fallos = 0
while True:
    buscarParticipante = buscarJugador()
    while seguir:
        if not buscarJugador:
            addInfo()
        else:
            menu()
            pregunta, datos, correcta = devolverDatos()
            print(pregunta)
            for i in range(len(datos)):
                print(f"{i}. {datos[i]}")
            intento = input("¿Cuál es la opción correcta?").lower().capitalize()
            if intento == correcta:
                print("Braavoooo 🤸🏻")
                aciertos += 1
            else:
                print("No...? 👁️👄👁️")
                fallos += 1
            continuar = input("¿Seguir jugando? (S/N)").lower()
            if continuar == "n":
                seguir = False







