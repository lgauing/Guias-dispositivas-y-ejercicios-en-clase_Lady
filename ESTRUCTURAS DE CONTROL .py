# Lady Mishell Gauin Gusñay
# 3er semestre de software A1

x=int(input("Ingresa un numero entero: "))
if x < 0:
      x = 0
      print('Negativo cambiado a cero')
elif x == 0:
      print('Cero')
elif x == 1:
      print("Uno")
else:
      print("Ninguna opcion")
print("Ok") if type(x) == int else print("-")
