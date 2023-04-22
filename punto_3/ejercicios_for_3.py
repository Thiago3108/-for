# Simular el lanzamiento de 2 dados, e imprimir cuantas veces cayo cada cara. Mostrar resultado con barra de asteriscos.
import random

c1 = ""
c2 = ""
c3 = ""
c4 = ""
c5 = ""
c6 = ""

# input
n = int(input("¿Cuántas veces se va a lanzar el dado?: "))

# procesing
for i in range(n*2):
    cara = random.randint(1, 6)
    if cara == 1:
        c1 += "*"
    elif cara == 2:
        c2 += "*"
    elif cara == 3:
        c3 += "*"
    elif cara == 4:
        c4 += "*"
    elif cara == 5:
        c5 += "*"
    elif cara == 6:
        c6 += "*"

# output
print("Resultados")
print("1:", c1)
print("2:", c2)
print("3:", c3)
print("4:", c4)
print("5:", c5)
print("6:", c6)