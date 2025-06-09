#Programa para calcular el numero de digitos del valor ingresado

numero = int(input("Ingresa un número entero: "))

num = abs(numero)


cdg = len(str(num))

print(f"El número tiene {cdg} dígito(s).")
