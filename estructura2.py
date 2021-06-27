# Lady Mishell Gauin Gusñay
# 3er semestre de software A1

""" num=20
nombre="ana"
print(num,type(num))
print(nombre,type(nombre))

def mensaje(msg):
    print(msg)
    
mensaje("Mi primer programa en Python")
mensaje("Mi segundo programa en Python")  """




class Sintaxis:
    instancia=0 # atributo de clase
    #  __init__metodoconstructor que se ejecuta cuando se instancia la clase cuyo objetivo es crear
    # e inicializar los atributos de la clase. Self es un objeto que representa la clase creada """
    def __init__(self,dato="llamando al constructor1"):
        self.frase=dato # atributo de instancia
        Sintaxis.instancia = Sintaxis.instancia+1
        
    def usoVariables(self):
        eda, _peso = 19, 70.5
        nombres = 'Lady Gauin'
        Tipo_sexo = 'F'
        civil = True 
        # tuplas = () son colecciones de datos de cualquier tipo inmutables
        usuario=()
        usuario =('lgauing','1234','lgauing@gmail.com')
        # print(usuario[2],nombres[7])
        # #usuario[3]="milagro"
        # #listas = [] colecciones mutables
        materias = []
        materias = ['Programacion Web', 'PHP', 'POO']
        aux=materias[1]
        materias[1]="Python"
        materias.append("Go")
        #print(materias,aux, materias[1])
        
        #diccionario = {} colecciones de objetos clave:valor tipo json
        docente={}
        docente = {'nombres':'Lady','edad':19,'activo':True}
        edad=docente['edad']
        docente['edad']=24
        docente['carrera']='IS'
        # # print(docente,edad,docente['edad'])
        # # print(usuario,usuario[0], usuario[0:2],usuario[-1])
        # # print(nombres,nombres[0], nombres[0.2],nombres[-1])
        # print(materias,materias[2:],materias[:3], materias[::-1],materias[-2:])
        # presentacion con format
        print("""Mi nombre es {}, tengo{}
              años""" .format(nombres, edad))
# print("Sintaxis antes de instancia es: {}".format(Sintaxis.instancia))
ejer1=Sintaxis() # Instancia la clase sintaxis y crea el objeto ejer1(copia de la clase)
# print("Sintaxis de ejer1 es: {}".format(Sintaxis.instancia))
# ejer2 = Sintaxis("instancia2")
# print(ejer1.frase)
# print("Sintaxis de ejer2 es: {}".format(Sintaxis.instancia))
# print("Sintaxis nuevamente de ejer1 es: {}".format(Sintaxis.instancia))
# print(ejer2.frase)
ejer1.usoVariables()