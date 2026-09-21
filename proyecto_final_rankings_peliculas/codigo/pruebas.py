# Pruebas del mini proyecto

from itertools import combinations
from pathlib import Path
import random

from algoritmos import (
    leer_peliculas,
    merge_sort_peliculas,
    comparar_rankings,
    contar_inversiones,
    contar_inversiones_fuerza_bruta,
    maximo_inversiones,
)


BASE = Path(__file__).resolve().parent.parent
ARCHIVO = BASE / "datos" / "pelis.csv"

CRITERIOS = [
    "Tomatometer %",
    "Fresh",
    "Rotten",
    "Popcornmeter %",
]


def prueba_casos_pequenos():
    casos = [
        ([0, 1, 2, 3], 0),
        ([3, 2, 1, 0], 6),
        ([1, 0, 3, 2], 2),
        ([2, 4, 1, 3, 5], 3),
    ]

    for secuencia, esperado in casos:
        _, obtenido = contar_inversiones(secuencia)
        assert obtenido == esperado

    print("Prueba 1 - casos pequenos conocidos: OK")


def prueba_orden_inverso():
    for n in [2, 5, 10, 20]:
        secuencia = list(range(n - 1, -1, -1))
        _, obtenido = contar_inversiones(secuencia)

        assert obtenido == maximo_inversiones(n)

    print("Prueba 2 - maximo de inversiones: OK")


def prueba_datos_reales():
    peliculas = leer_peliculas(ARCHIVO)
    rankings = {}

    for criterio in CRITERIOS:
        ordenadas = merge_sort_peliculas(peliculas, criterio)
        rankings[criterio] = [
            pelicula["Nombre"] for pelicula in ordenadas
        ]

    for a, b in combinations(CRITERIOS, 2):
        inv_merge, secuencia = comparar_rankings(
            rankings[a],
            rankings[b]
        )

        inv_bruta = contar_inversiones_fuerza_bruta(secuencia)

        assert inv_merge == inv_bruta

    print("Prueba 3 - datos reales vs fuerza bruta: OK")


def prueba_aleatoria():
    random.seed(2026)

    for _ in range(30):
        n = 40
        secuencia = list(range(n))
        random.shuffle(secuencia)

        _, inv_merge = contar_inversiones(secuencia)
        inv_bruta = contar_inversiones_fuerza_bruta(secuencia)

        assert inv_merge == inv_bruta

    print("Prueba 4 - 30 permutaciones aleatorias: OK")


prueba_casos_pequenos()
prueba_orden_inverso()
prueba_datos_reales()
prueba_aleatoria()

print("\nTodas las pruebas finalizaron correctamente.")
