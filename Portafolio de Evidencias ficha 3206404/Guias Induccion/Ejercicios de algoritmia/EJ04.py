# Programa para sumar pares entre valores ingresados

try:
    n1 = int(input("Ingrese el primer número: "))
    n2 = int(input("Ingrese el segundo número: "))

    if n1 <= 0 or n2 <= 0:
        print("Error: ambos números deben ser mayores a 0.")
    else:
        if n1 > n2:
            n1, n2 = n2, n1

        suma = 0
        for i in range(n1, n2 + 1):
            if i % 2 == 0:
                suma += i

        print(f"La suma de los números pares entre {n1} y {n2} es: {suma}")

except ValueError:
    print("Error: debe ingresar solo números enteros.")
