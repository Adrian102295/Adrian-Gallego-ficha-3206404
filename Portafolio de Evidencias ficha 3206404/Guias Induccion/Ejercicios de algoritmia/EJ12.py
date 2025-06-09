# programa para crear una lista que invierta la primera
import random


l = [random.randint(1, 100) for _ in range(20)]
print("Lista original:", l)

# Crear la lista inversa
l_inversa = l[::-1]
print("Lista inversa :", l_inversa)


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
