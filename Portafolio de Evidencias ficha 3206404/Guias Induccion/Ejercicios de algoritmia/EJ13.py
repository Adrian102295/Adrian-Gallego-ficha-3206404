# Programa que integra a un menu los ejercicios del 6 al 12

import random


l = [random.randint(1, 100) for _ in range(20)]
print(l)


def mostrar_lista():
    print("\nLista generada:", l)


def buscar_numero():
    try:
        nb = int(input("Ingrese el número a buscar: "))
        if nb < 1:
            print("El número debe ser mayor a 0")
            return
        if nb in l:
            p = l.index(nb)
            print(f"Número encontrado en la posición {p}")
        else:
            print("Número no encontrado")
    except ValueError:
        print("Debe ingresar un número entero")


def contar_apariciones():
    try:
        nb = int(input("Ingrese el número a buscar: "))
        if nb < 1:
            print("El número debe ser mayor a 0")
            return
        if nb in l:
            p = l.index(nb)
            c = l.count(nb)
            print(f"Número encontrado en la posición {p}")
            print(f"El número aparece {c} veces en la lista")
        else:
            print("Número no encontrado")
    except ValueError:
        print("Debe ingresar un número entero")


def mayor_y_cantidad():
    mayor = max(l)
    cantidad = l.count(mayor)
    print(f"El número mayor es {mayor} y aparece {cantidad} veces")


def aparece_mas_que_mayor():
    try:
        nb = int(input("Ingrese un número: "))
        if nb < 1:
            print("El número debe ser mayor a 0")
            return
        cantidad_nb = l.count(nb)
        cantidad_mayor = l.count(max(l))
        print(f"El número ingresado ({nb}) aparece {cantidad_nb} veces")
        print(f"El número mayor ({max(l)}) aparece {cantidad_mayor} veces")
        print("¿El número ingresado aparece más veces que el mayor?:",
              cantidad_nb > cantidad_mayor)
    except ValueError:
        print("Debe ingresar un número entero")


def media_general():
    media = sum(l) / len(l)
    print(f"La media de los números en la lista es: {media:.2f}")


def media_mayor_menor():
    mayor = max(l)
    menor = min(l)
    media = (mayor + menor) / 2
    print(f"El número mayor es {mayor}, el menor es {menor}")
    print(f"La media entre ellos es: {media:.2f}")


def lista_inversa():
    inversa = l[::-1]
    print("Lista inversa:", inversa)


# Menú principal
while True:
    print("\n------ MENÚ DE OPCIONES ------")
    print("1. Mostrar la lista original")
    print("2. Buscar un número en la lista")
    print("3. Buscar y contar cuántas veces aparece un número")
    print("4. Encontrar el número mayor y cuántas veces aparece")
    print("5. Verificar si un número aparece más veces que el mayor")
    print("6. Calcular la media de todos los números")
    print("7. Calcular la media entre el mayor y el menor")
    print("8. Crear una lista inversa")
    print("9. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        mostrar_lista()
    elif opcion == '2':
        buscar_numero()
    elif opcion == '3':
        contar_apariciones()
    elif opcion == '4':
        mayor_y_cantidad()
    elif opcion == '5':
        aparece_mas_que_mayor()
    elif opcion == '6':
        media_general()
    elif opcion == '7':
        media_mayor_menor()
    elif opcion == '8':
        lista_inversa()
    elif opcion == '9':
        print("Programa finalizado.")
        break
    else:
        print("Opción inválida. Intente nuevamente.")
