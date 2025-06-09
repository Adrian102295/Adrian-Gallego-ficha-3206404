#Programa para saber la palabra mas grande

texto = input("Ingrese un texto: ")

palabras = texto.split()


num_palabras = len(palabras)
tamano_maximo = 0


for palabra in palabras:
    if len(palabra) > tamano_maximo:
        tamano_maximo = len(palabra)
        palabra_m = palabra
         


print("Número de palabras:", num_palabras)
print("Tamaño de la palabra más grande:", tamano_maximo)
print("Palabra mas grande:", palabra_m)
