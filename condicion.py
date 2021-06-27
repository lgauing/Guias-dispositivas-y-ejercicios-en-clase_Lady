# Lady Mishell Gauin Gusñay
# 3er semestre de software A1

class condicion:

    def __init__(self,num1,num2):
       self.numero1=num1
       self.numero2=num2
       numeros=self.numero1+self.numero2
       self.numero3=numeros
    
    def usoIf(self):
        #if...elif ... else ...: permiten condicionar la ejecucion de uno o varios bloques
        # de sentencias al cumplimiento de una o varias condiciones.
        if self.numero1 == self.numero2:
            print("numero1={}=numero2={} : son iguales".format(self.numero1,self.numero2))
        elif self.numero1 == self.numero3:
            print("numero1 y numero3 son iguales")
        else:
            print ("numero diferentes")
        
# print("instancia de la clase
# cond2= condicion()
# print (cond2.numero3)
# cond2.usoIf()
cond1= condicion(10,10)
cond1.usoIf()
print("Gracias por su visita")