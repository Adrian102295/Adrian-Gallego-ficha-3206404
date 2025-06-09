# programa para encontrar la media de la lista

import random


l = [random.randint(1, 100) for _ in range(20)]
print("Lista generada:", l)


media = sum(l) / len(l)
print(f"La media de los números en la lista es: {media:.2f}")


try:
    nb = int(input("Ingrese el número a buscar: "))
    if nb < 1:
        print("El número debe ser mayor a 0")
    else:
        if nb in l:
            p = l.index(nb)
            print(f"Número encontrado en la posición {p}")
        else:
            print("Número no encontrado")
except ValueError:
    print("Debe ingresar un número entero")
