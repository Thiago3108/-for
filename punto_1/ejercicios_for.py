# Leer n numeros enteros (uno en cada lectura), y mostrar e imprimir cuantos son pares y cuantos son impares
n = int(input("Digite el ultimo numero entero que desea:"))
n = n + 1
rta, rta_2 = "| ", "| "
for i in range(1, n):
    if i % 2 == 0:
        rta = rta + str(i) + ", "
    else:
        rta_2 = rta_2 + str(i) + ", "  

print(f"los numeros pares son: {rta}| y los numeros impares son: {rta_2}|")