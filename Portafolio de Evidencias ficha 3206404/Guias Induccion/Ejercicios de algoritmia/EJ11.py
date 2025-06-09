# Programa para calcular la media entre el numero menor y el numero mayor de la lista
import random


l = [random.randint(1, 100) for _ in range(20)]
print("Lista generada:", l)


mayor = max(l)
menor = min(l)
media = (mayor + menor) / 2
print(f"El número mayor es {mayor} y el menor es {menor}.")
print(f"La media entre el mayor y el menor es: {media:.2f}")


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
