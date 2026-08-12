class Empleado:
    def __init__(self,nombre,edad,puesto):
        self.nombre= nombre
        self.edad= edad
        self.puesto= puesto
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Puesto: {self.puesto}")

empleado = Empleado("Carlos Perez", 30, "Desarrollador")
empleado.mostrar_info()
