# Lady Mishell Gauin Gusñay
# 3er semestre de software A1

# Tuplas – Listas - Diccionarios
usuario = ('dchiki','1234','chiki@gmail.com')
materias = ["Python","PHP","POO","Go"]
docente = {'nombre':'JAVIER','edad':50,"fac":"faci"}
print(usuario[0],materias[1],docente['nombre'])
print(usuario[0:2],docente.keys(),docente.values())
materias.append('Programacion Movil')
docente["sexo"], docente['edad']="M", 19
print(materias,docente)
tupla,lista,diccionario=(),[],{}

# Recorridos tuplas y listas con in
for valor in usuario: print(valor)

# Recorridos listas con enumerate
for i, c in enumerate(materias): print(i,':',c)

# Recorridos diccionario con items
for c, v in docente.items(): print(c,':',v)
