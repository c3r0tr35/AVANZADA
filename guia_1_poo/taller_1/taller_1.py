class Persona:
    def __init__(self, nombre, identificacion):
        self._nombre = nombre
        self._identificacion = identificacion
    def presentarse(self):
        raise NotImplementedError


class Estudiante(Persona):
    def __init__(self, nombre, identificacion, codigo):
        super().__init__(nombre, identificacion)
        self.codigo = codigo
    def presentarse(self):
        print(f"Hola mi nombre es {self._nombre} con numero de identificación {self._identificacion} y mi rol en la institución es Estudiante con codigo numero {self.codigo}")
    pass
class Profesor(Persona):
    def __init__(self, nombre, identificacion, area):
        super().__init__(nombre, identificacion)
        self.area = area
    def presentarse(self):
        print(f"Hola mi nombre es {self._nombre} con numero de identificación {self._identificacion} y mi rol en la institución es Profesor con area en {self.area}")
    pass
class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.participantes = []
    def agregar_participante(self, persona):
        self.participantes.append(persona)
    def pasar_lista(self):
        for p in self.participantes:
            p.presentarse()


p = Estudiante("Ana", 1045, 90)
o = Profesor("Perez", 8900, "Ingles")
curso= Curso("Clase Basica Ingles")

curso.agregar_participante(p)
curso.agregar_participante(o)

curso.pasar_lista()
