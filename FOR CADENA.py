# Lady Mishell Gauin Gusñay
# 3er semestre de software A1

# for in cadena - in(tupla) – in[lista]
for car in frase:
    if car in ("a","e","i","o","u","A","E","I","O","U"):
        if car in ["A","E","I","O","U"]:
            continue
        else:
            cvoc=cvoc+1
print('cantidad vocales:{}'.format(cvoc))