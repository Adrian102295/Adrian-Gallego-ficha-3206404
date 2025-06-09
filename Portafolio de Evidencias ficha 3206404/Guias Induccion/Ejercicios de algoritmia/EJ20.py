#Programa para calcular la cuota mensual



capital = float(input("Ingrese el capital del préstamo: "))
interes_anual = float(input("Ingrese el interés anual (en %): "))
anios = int(input("Ingrese el número de años del préstamo: "))


tasa_mensual = interes_anual / 100 / 12
num_pagos = anios * 12


if tasa_mensual == 0:
    cuota_mensual = capital / num_pagos
else:
    cuota_mensual = capital * (tasa_mensual * (1 + tasa_mensual) ** num_pagos) / ((1 + tasa_mensual) ** num_pagos - 1)


total_a_pagar = cuota_mensual * num_pagos

# Mostrar resultados
print(f"Cuota mensual: {cuota_mensual:.2f} cop")
print(f"Total a pagar: {total_a_pagar:.2f} cop")
