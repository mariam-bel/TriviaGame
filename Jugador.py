import uuid

class Jugador:
    def __init__(self, nombre, aciertos=0, fallos=0, id_jugador=None):
        self.nombre = nombre
        self.id = id_jugador if id_jugador else str(uuid.uuid4())[:4]
        self.aciertos = aciertos
        self.fallos = fallos

    def acierto(self):
        self.aciertos += 1

    def fallo(self):
        self.fallos += 1

    def __str__(self):
        return f"{self.nombre} | {self.id} | {self.aciertos} | {self.fallos}"
