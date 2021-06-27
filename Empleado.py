# Lady Mishell Gauin Gusñay
# 3er semestre de software A1

from Cargo import Cargo

class Empleado:
    secuencia=0
    def __init__(self,nom="",sue=0, car=None):
        # Empleado.secuencia=Empleado.secuencia+1
        # self.codigo=Empleado.secuencia
        self.codigo=self.generarCodigo()
        self.nombre=nom
        self.sueldo=sue
        self.cargoEmp=car
        
    def generarCodigo(self):
         Empleado.secuencia=Empleado.secuencia+1
         return Empleado.secuencia
     
    def mostrar(self):
         print("codigo:{} Nombre:{}, cargo({}): {}".format(self.codigo,self.nombre,self.cargo,self.cargo.descripción))

cargo1= Cargo("Docente")
emp1= Empleado("Lady",200,cargo1)
emp1.mostrar()
emp2= Empleado("Ruben",300,cargo1)
emp2.mostrar()