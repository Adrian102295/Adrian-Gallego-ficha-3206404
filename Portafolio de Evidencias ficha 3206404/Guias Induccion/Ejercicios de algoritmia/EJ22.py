#Programa juego rojo amarillo verde mas dificil

import random

def generar_codigo():
    """Genera una lista de 4 dígitos aleatorios distintos entre 0 y 9."""
    return random.sample(range(10), 4)

def evaluar_intento(codigo, intento):
    """Evalúa el intento del jugador devolviendo la cantidad de colores."""
    verdes = 0
    amarillos = 0

    for i in range(4):
        if intento[i] == codigo[i]:
            verdes += 1
        elif intento[i] in codigo:
            amarillos += 1
    
    rojos = 4 - verdes - amarillos
    return verdes, amarillos, rojos

def juego_dificil_rojo_amarillo_verde():
    print("=== Juego del Rojo-Amarillo-Verde (Modo Difícil) ===")
    print("Debes adivinar 4 dígitos distintos entre 0 y 9.")
    print("Se mostrará cuántos dígitos están en cada estado:")
    print("- Verde: correcto y en la posición correcta")
    print("- Amarillo: correcto pero en posición incorrecta")
    print("- Rojo: no aparece en el código\n")

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
        verdes, amarillos, rojos = evaluar_intento(codigo, intento)
        print(f"Pista: {verdes} Verde(s), {amarillos} Amarillo(s), {rojos} Rojo(s)")

        if verdes == 4:
            print(f"\n¡Felicidades! Adivinaste el código en {intentos} intento(s).")
            break

juego_dificil_rojo_amarillo_verde()
