import uuid

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.id = self.generateId

    @property
    def generateId(self):
        idsGuardados = []
        prov = hex(3)
        for idGuardador in idsGuardados:
            if idGuardador.id == self.id:
                prov = hex(3)
            idsGuardados.append(prov)
        return prov

    def __str__(self):
        return f"Nombre: {self.nombre}, id: {self.id}"

    def getNombre(self):
        return self.nombre
    def getId(self):
        return self.id
