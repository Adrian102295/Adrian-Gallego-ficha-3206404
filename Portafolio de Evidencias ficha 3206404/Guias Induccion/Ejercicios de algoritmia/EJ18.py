#Calcule la letra de control para el NIT


letras_control = [
    'T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B',
    'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E'
]


nit = int(input("Ingrese el número de NIT: "))


resto = nit % 23


letra = letras_control[resto]


print(f"La letra de control para el NIT {nit} es: {letra}")
