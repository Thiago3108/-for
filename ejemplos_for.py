# ejm 1 con listas
rta = "salida = |"
for i in [1,2,3,4,5,6,7,8,9,10]:
    rta = rta + str(i) + ", "
rta = rta + "|"
print(rta)

# ejm 2
for numero in [1,2,3,4,5,6,7,8,9,10]:
    print("UIS NO ES UNO....")

# ejm 3 con tuplas
rta = "salida = |"
for i in (1,2,3,4,5,6,7,8,9,10):
    rta = rta + str(i) + ", "
rta = rta + "|"
print(rta)

# ejm 4
rta = "salida = |"
for i in range(1,11):
    rta = rta + str(i) + ", "
rta = rta + "|"
print(rta)

# ejm 5
rta = "salida = |"
for i in "uis":
    rta = rta + str(i) + ", "
rta = rta + "|"
print(rta)

# ejm 6
suma = 0
for i in range(1,11):
    suma = suma + i
print(f"La suma es: {suma}")

# ejm 7
frase = input("Digite una frase: ")
vocales = "aeiouAEIOU"
numero_vocales = 0
for i in frase:
    if i in vocales:
        numero_vocales += 1
print(f"En la frase hay {numero_vocales} vocales")