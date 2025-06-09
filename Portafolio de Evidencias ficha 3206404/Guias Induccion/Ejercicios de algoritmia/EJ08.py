# programa para ver cual es el numero mas grande en la lista y cuantas veces aparece
import random


l = [random.randint(1, 100) for _ in range(20)]
print("Lista generada:", l)


mayor = max(l)
cantidad = l.count(mayor)
print(f"\nEl número mayor es {mayor} y aparece {cantidad} veces.\n")
