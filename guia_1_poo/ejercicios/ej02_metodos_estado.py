class Empleado:
    def __init__(self,nombre,edad,puesto):
        self.nombre= nombre
        self.edad= edad
        self.puesto= puesto
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Puesto: {self.puesto}")

    def cambiar_puesto(self, nuevo_puesto):
        self.puesto = nuevo_puesto

empleado = Empleado("Carlos Perez", 30, "Desarrollador")
print("Información Inicial: ")
empleado.mostrar_info()

empleado.cambiar_puesto("Gerente")

print("\nInformación Actualizada: ")
empleado.mostrar_info()
