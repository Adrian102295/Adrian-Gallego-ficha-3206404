#Programa juego rojon amarillo verde

import random

def generar_codigo():
    """Genera una lista de 4 dígitos aleatorios distintos entre 0 y 9."""
    return random.sample(range(10), 4)

def evaluar_intento(codigo, intento):
    """Evalúa el intento del jugador comparándolo con el código secreto."""
    resultado = []

    for i in range(4):
        if intento[i] == codigo[i]:
            resultado.append("Verde")
        elif intento[i] in codigo:
            resultado.append("Amarillo")
        else:
            resultado.append("Rojo")
    
    return resultado

def juego_rojo_amarillo_verde():
    print("=== Juego del Rojo-Amarillo-Verde ===")
    print("Debes adivinar 4 dígitos distintos entre 0 y 9.")
    print("Te diremos Verde si el dígito está en la posición correcta,")
    print("Amarillo si está pero en otra posición, y Rojo si no está en el código.\n")

    codigo = generar_codigo()
    intentos = 0

    while True:
        entrada = input("Introduce 4 dígitos separados por espacios (ej: 1 2 3 4): ")

        try:
            intento = list(map(int, entrada.strip().split()))
            if len(intento) != 4 or len(set(intento)) != 4 or any(d < 0 or d > 9 for d in intento):
                raise ValueError
        except ValueError:
            print("Entrada inválida. Asegúrate de ingresar 4 dígitos distintos entre 0 y 9.\n")
            continue

        intentos += 1
        resultado = evaluar_intento(codigo, intento)
        print("Resultado:", resultado)

        if resultado == ["Verde"] * 4:
            print(f"\n¡Felicidades! Adivinaste el código en {intentos} intento(s).")
            break


juego_rojo_amarillo_verde()
