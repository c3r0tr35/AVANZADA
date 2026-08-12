class Producto:
    def __init__(self, nombre, precio ,stock_inicial=0):
        self.nombre = nombre
        self.precio = precio
        self.__stock = stock_inicial
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Precio: {self.precio}")
        print(f"Stock: {self.__stock}")

    def reponer(self,stock):
        if stock <= 0:
            print("No hay stock")
            return
        self.__stock += stock

    def vender(self,stock):
        if stock <= 0:
            print("No hay stock a vender")
            return
        if stock > self.__stock:
            print("No hay suficiente stock a vender")
            return
        self.__stock -= stock

p = Producto("Zapato", 7000, 30)
p.mostrar_info()
p.vender(20)
p.mostrar_info()
p.reponer(2)
p.mostrar_info()
p.vender(20)
p.vender(4)
p.mostrar_info()

#1)La responsabilidad que debe tener es hacia el catalogo de productos, con sus caracteristicas.
#2)La responsabilidad que no debe tener es ya tener entradas de teclado, o ya cosas de pagos que deberia ser de otra clase.
#3)Donde se puede evidenciar es cuando se valida por encapsulamiento el stock.