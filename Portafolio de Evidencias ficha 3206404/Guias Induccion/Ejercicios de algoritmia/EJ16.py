# Programa que devuelve el cambio con monedas disponibles


vc = int(input("Ingrese el valor a cobrar: "))
me = int(input("Ingrese el monto entregado: "))


if me < vc:
    print("El monto entregado no es suficiente.")
else:
    
    cambio = me - vc
    print(f"Cambio a devolver: {cambio} pesos")

    
    monedas = [1000, 500, 200, 100, 50]

   
    for moneda in monedas:
        cantidad = cambio // moneda
        if cantidad > 0:
            print(f"{cantidad} moneda(s) de {moneda}")
            cambio -= cantidad * moneda

    
    if cambio > 0:
        print(f"No se puede devolver {cambio} pesos con las monedas disponibles.")
