# programa para encontrar el numero y contar veces que aparece

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
    c = l.count(nb)
    print(f"el numero aparece {c} veces en la lista")
else:
    print("Numero no encontrado")
