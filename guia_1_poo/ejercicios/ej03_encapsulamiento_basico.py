class CuentaBancaria:
    def __init__(self, saldo_inicial=0):
        self.__saldo = saldo_inicial
    def depositar(self,cantidad):
        if cantidad <= 0:
            print("La cantidad debe ser positiva")
            return
        self.__saldo += cantidad

    def retirar(self,cantidad):
        if cantidad <= 0:
            print("La cantidad debe ser positiva")
            return
        if cantidad > self.__saldo:
            print("Fondos insuficientes")
            return
        self.__saldo -= cantidad
    def consultar_saldo(self):
        print(f"Saldo actual: {self.__saldo}")

c= CuentaBancaria(1000)
c.consultar_saldo()
c.depositar(500)
c.consultar_saldo()

c.retirar(2000)
c.retirar(300)
c.consultar_saldo()
