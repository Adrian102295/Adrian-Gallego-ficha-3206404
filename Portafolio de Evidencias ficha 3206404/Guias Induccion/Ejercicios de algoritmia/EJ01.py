# --------------PROG_NUMEROS PAR---------------

# --------------INGREASR EL NUMERO--------------
num = -10
while type(num) != int or num < 1:
    try:
        num = int(input("Ingrese un entero mayor a 0: "))
        if num < 1:
            print("El numero debe ser mayor a 0: ")
    except ValueError:
        print("Debe ingresar un numero entero")
        num = -1

# ----------------VALIDACION DE NUMERO----------

if num % 2 == 0:
    print(f"el numero {num} es par")
else:
    print(f"el numero {num} no es par")
