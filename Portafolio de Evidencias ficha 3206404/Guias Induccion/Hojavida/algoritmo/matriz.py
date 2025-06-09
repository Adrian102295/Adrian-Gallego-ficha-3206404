from random import *

matriz = [[randint(10, 99) for j in range(10)] for i in range(10)]
#------------------------------------------------------------------


def linea_horizontal(columnas, ancho=4):
    print("|" + ("_" * ancho + "|") * columnas)

linea_horizontal(10)
for fila in matriz:
    for num in fila:
        print(f"| {num:2}", end=" ")
    print("|")
    linea_horizontal(10)

#------------------------------------------------------------------ 

print("\n------Diagonal Principal---------------")
for i in range(10):
    print(f"[{'       '*i}{matriz[i][i]}{'       '*(10-i-1)}]")


print("\n-------------Diagonal Inversa----------")
for i in range(10):
    print(f"[{'      '*(10-i-1)}{matriz[i][10-i-1]}{'      '* i}]")



print("\n-------Matriz Inferior Izquierda--------")
for i in range(10):
    print("" * i, end= "|")
    for j in range (i + 1):
        print( matriz[i][j], end=" | ")
    print("")


print("\n---------Matriz Superior Izquierda---------")
for i in range (10):
    print(" | ", end="")
    for j in range(10 - i ):
        print( matriz[i][j], end =" | " )
    print("  ")


print("\n-----------Matriz Inferior Derecha-----------")
for i  in range (10):
    print("   " *(10 - i), end= "|")
    for j in range(10 - i - 1, 10):
        print(matriz[i][j], end="|")
    print("")

print("\n---------Matriz Superior Derecha---------")
for i in range(10):
    # Imprimir espacios vacíos o separadores a la izquierda
    print("      " * i, end="")  # 4 espacios por celda vacía (ajustable)
    for j in range(i, 10):
        print(f"{matriz[i][j]:>3} |", end=" ")  # Alineado a la derecha
    print()


