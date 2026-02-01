import random
import os

from Jugador import Jugador

ficheroPreguntas = "trivia_cultura.csv"
ficheroJugadores = "jugadores.csv"

def buscar_jugador(nombre):
    if not os.path.exists(ficheroJugadores):
        return None
    with open(ficheroJugadores, encoding="utf-8-sig") as f:
        for linea in f:
            nombre, id, aciertos, fallos = linea.strip().split(";")
            if nombre.lower() == nombre.lower():
                return nombre, id, int(aciertos), int(fallos)
    return None


def guardarJugador(jugador):
    with open(ficheroJugadores, "a", encoding="utf-8-sig") as f:
        f.write(str(jugador) + "\n")


def mostrarRanking():
    if not os.path.exists(ficheroJugadores):
        print("No hay ranking todavía.")
        return
    jugadores = []
    with open(ficheroJugadores, encoding="utf-8-sig") as f:
        for linea in f:
            nombre, _, aciertos, _ = linea.strip().split(";")
            jugadores.append((nombre, int(aciertos)))
    jugadores.sort(key=lambda x: x[1], reverse=True)

    print("\nRANKING")
    for i, j in enumerate(jugadores, 1):
        print(f"{i}. {j[0]} - {j[1]} aciertos")


def preguntaAleatoria():
    with open(ficheroPreguntas, encoding="utf-8-sig") as f:
        lineas = f.read().splitlines()[1:]

    datos = random.choice(lineas).split(";")
    return datos[0], datos[1:5], datos[5]


def main():

    nombre = input("Introduce tu nombre (o 'ranking'): ").strip()

    if nombre.lower() == "ranking":
        mostrarRanking()
        return

    datos = buscar_jugador(nombre)
    if datos:
        print("Usuario existente. Se reinicia la partida.")
        jugador = Jugador(nombre)
    else:
        jugador = Jugador(nombre)

    seguir = True
    while seguir:
        pregunta, respuestas, correcta = preguntaAleatoria()
        print("\n" + pregunta)

        for i, respuesta in enumerate(respuestas):
            print(f"{i}. {respuesta}")

        intento = input("Respuesta: ")

        if intento == correcta:
            print("¡Braavooo! 🤸🏻")
            jugador.acierto()
        else:
            print("No...? 👁️👄👁️")
            jugador.fallo()

        seguir = input("¿Seguir jugando? (s/n): ").lower() == "s"

    print(f"Aciertos: {jugador.aciertos}")
    print(f"Fallos: {jugador.fallos}")

    guardarJugador(jugador)


if __name__ == "__main__":
    main()
