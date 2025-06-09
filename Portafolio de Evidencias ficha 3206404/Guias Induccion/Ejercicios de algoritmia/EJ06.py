# Programa para ver si el valor ingresado esta en la lista

import random

l = [random.randint(1, 100) for _ in range(20)]
print(l)

nb = int(input("ingrese el numero a buscar: "))

try:
    if nb < 1:
        print("el numero debe ser mayor a 0")
except:
    print("ingrese un valor entero")

if nb in l:
    p = l.index(nb)
    print(f"numero encontrado en la posicion {p}")
else:
    print("Numero no encontrado")
