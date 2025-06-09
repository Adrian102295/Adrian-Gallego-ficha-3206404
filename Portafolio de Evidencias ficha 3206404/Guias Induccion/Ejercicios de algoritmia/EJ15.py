#Programa para indicar si un año es bisiesto


año = int(input("ingrese el año que desea verificar: "))


if(año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"el año {año} es bisiesto")
else:
    print(f"el año {año} no es bisiesto")