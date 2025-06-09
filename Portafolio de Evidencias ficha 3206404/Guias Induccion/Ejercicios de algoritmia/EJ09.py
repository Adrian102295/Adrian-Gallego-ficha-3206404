# Programa para commparar cuantas veces sale el numero ingrezado y cuantas el numero mayor de la lista

import random

l = [random.randint(1, 100) for _ in range(20)]
print("Lista generada:", l)


try:
    nb = int(input("Ingrese el número a buscar: "))
    if nb < 1:
        print("El número debe ser mayor a 0")
    else:

        mayor = max(l)
        cantidad_mayor = l.count(mayor)
        cantidad_nb = l.count(nb)

        print(f"El número mayor es {mayor} y aparece {cantidad_mayor} veces")
        print(f"El número ingresado ({nb}) aparece {cantidad_nb} veces")

        resultado = cantidad_nb > cantidad_mayor
        print("¿El número ingresado aparece más veces que el mayor?:", resultado)

except ValueError:
    print("Debe ingresar un número entero")
