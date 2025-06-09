# Programa oredenar valores

n1 = int(input("ingrese el primer valor: "))
n2 = int(input("ingrese el segundo valor: "))
n3 = int(input("ingrese el tercer valor: "))
n4 = int(input("ingrese el cuarto valor: "))
n5 = int(input("ingrese el quinto valor: "))

try:
    if n1 < 1 or n2 < 1 or n3 < 1 or n4 < 1 or n5 < 1:
        print("El numero debe ser mayor a 0: ")
except ValueError:
    print("Debe ingresar un numero entero")

l = [n1, n2, n3, n4, n5]
lo = sorted(l)
print(lo)
