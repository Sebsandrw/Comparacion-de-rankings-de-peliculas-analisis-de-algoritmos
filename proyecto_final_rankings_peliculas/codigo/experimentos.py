# Prueba experimental de crecimiento.
# se utiliza una permutacion de posiciones para medir solamente el algoritmo de conteo de inversiones

import random
import time

from algoritmos import contar_inversiones


def medir(n):
    secuencia = list(range(n))
    random.shuffle(secuencia)

    inicio = time.perf_counter()
    _, inversiones = contar_inversiones(secuencia)
    fin = time.perf_counter()

    return inversiones, fin - inicio


random.seed(2026)

tamanos = [100, 500, 1000, 5000, 10000]

print("n,inversiones,tiempo_segundos")

for n in tamanos:
    inversiones, tiempo = medir(n)
    print(f"{n},{inversiones},{tiempo:.6f}")
