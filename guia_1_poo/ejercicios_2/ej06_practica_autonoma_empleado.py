class Empleado:
    def __init__(self, nombre):
        self.nombre=nombre
    def calcular_pago(self):
        pass

class ETC(Empleado):
    def __init__(self,nombre,sueldom):
        super().__init__(nombre)
        self.sueldom=sueldom
    def calcular_pago(self):
        return self.sueldom
class EPH(Empleado):
    def __init__(self, nombre, horas, tarifa):
        super().__init__(nombre)
        self.horas=horas
        self.tarifa=tarifa

    def calcular_pago(self): 
        return self.horas*self.tarifa


empleados=[ETC("Ana",45000), EPH("Oscar",94,2400), EPH("Tatiana", 140, 5000)]
total=0

for e in empleados:
    pago = e.calcular_pago()
    total += pago
    print(f"Empleado: {e.nombre} // Pago: {pago:.2f}")
print(f"Total acumulado de la nomina: ${total:.2f}")
