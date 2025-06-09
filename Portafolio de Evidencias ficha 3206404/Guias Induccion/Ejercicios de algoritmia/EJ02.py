# Dado un número N, calcular la suma 1 + 2 + 3 +...+ N


N = int(input("Ingresa un número: "))


suma = 0


for i in range(1, N + 1):
    suma += i


print(f"La suma desde 1 hasta {N} es: {suma}")
