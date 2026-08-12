class Persona:
  def __init__(self,nombre):
    self.nombre = nombre
  def presentarse(self):
    print(f"Hola, soy {self.nombre}")

class Estudiante(Persona):
  def __init__(self,nombre,codigo):
    super()__init__(nombre)
    self.codigo = codigo
  def presentarse(self):
    print(f"Hola, soy {self.nombre} (Estudiante)")
  def mostrar_codigo(self):
    print(f"Codigo: {self.codigo}")

p = Persona("Ana")
e = Estudiante("Carlos", "2026-001")

p.presentarse()
e.presentarse()
e.mostrar_codigo()
