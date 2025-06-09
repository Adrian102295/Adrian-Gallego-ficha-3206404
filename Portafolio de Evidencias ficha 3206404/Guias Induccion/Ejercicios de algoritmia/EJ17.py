#Programa para agregar nuevo aprendiz y organizarlo por el apellido
aprendices = [
    "Anderson Avila",
    "Endri Bracho",
    "Santiago Igua",
    "Jhon Beltran",
    "Samael Lemus",
    "Nicolas Sanchez",
    "Breiner Alvarado",
    "Juan Velasquez",
    "Paula Huertas",
    "Angela Rodriguez"
]


aprendices.sort(key=lambda nombre: nombre.split()[-1])

print("Lista original de aprendices (ordenada por apellido):")
for nombre in aprendices:
    print(nombre)

aprendizn = input("Ingrese el nombre completo del nuevo aprendiz: ")


aprendices.append(aprendizn)
aprendices.sort(key=lambda nombre: nombre.split()[-1])

print("Lista actualizada de aprendices (ordenada por apellido):")
for nombre in aprendices:
    print(nombre)
