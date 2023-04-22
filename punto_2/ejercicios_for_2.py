# Mostrar e imprimir cuantos multiplos de 7, y cuantos multiplos de 9 hay entre 1000 y 5000.

MIN = 1
MAX = 12
rta, rta_2 = "|", "|"
count, count_1 = 0, 0
for i in range(MIN, MAX):
    if i % 7 == 0:
        rta = rta + str(i)+ " "
        count += 1
    elif i % 9 == 0:
        rta_2 = rta_2 + str(i)+ " "
        count_1 += 1

print(f"multiplos de 7= {count}, multiplos de 9= {count_1}")