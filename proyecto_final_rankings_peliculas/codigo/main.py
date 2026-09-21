# Programa principal del mini proyecto

from itertools import combinations
from pathlib import Path
import csv

from algoritmos import (
    leer_peliculas,
    merge_sort_peliculas,
    comparar_rankings,
    maximo_inversiones,
    porcentaje_diferencia,
)


BASE = Path(__file__).resolve().parent.parent
ARCHIVO_DATOS = BASE / "datos" / "pelis.csv"
ARCHIVO_RANKINGS = BASE / "resultados" / "rankings.csv"
ARCHIVO_COMPARACIONES = BASE / "resultados" / "comparaciones.csv"

CRITERIOS = [
    "Tomatometer %",
    "Fresh",
    "Rotten",
    "Popcornmeter %",
]


def generar_rankings(peliculas):
    rankings = {}

    for criterio in CRITERIOS:
        ordenadas = merge_sort_peliculas(peliculas, criterio)

        rankings[criterio] = [
            pelicula["Nombre"] for pelicula in ordenadas
        ]

    return rankings


def guardar_rankings(rankings):
    cantidad = len(next(iter(rankings.values())))

    with open(ARCHIVO_RANKINGS, "w",
              newline="", encoding="utf-8-sig") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["Posicion"] + list(rankings.keys()))

        for i in range(cantidad):
            fila = [i + 1]

            for criterio in rankings:
                fila.append(rankings[criterio][i])

            escritor.writerow(fila)


def comparar_todos(rankings):
    resultados = []
    n = len(next(iter(rankings.values())))

    for criterio_a, criterio_b in combinations(CRITERIOS, 2):
        inversiones, _ = comparar_rankings(
            rankings[criterio_a],
            rankings[criterio_b]
        )

        diferencia = porcentaje_diferencia(inversiones, n)

        resultados.append({
            "criterio_a": criterio_a,
            "criterio_b": criterio_b,
            "inversiones": inversiones,
            "diferencia": diferencia,
        })

    return resultados


def guardar_comparaciones(resultados):
    with open(ARCHIVO_COMPARACIONES, "w",
              newline="", encoding="utf-8-sig") as archivo:
        escritor = csv.writer(archivo)

        escritor.writerow([
            "Criterio A",
            "Criterio B",
            "Inversiones",
            "Diferencia (%)",
        ])

        for r in resultados:
            escritor.writerow([
                r["criterio_a"],
                r["criterio_b"],
                r["inversiones"],
                f'{r["diferencia"]:.2f}',
            ])


def mostrar_resultados(rankings, comparaciones):
    n = len(next(iter(rankings.values())))

    print("MINI PROYECTO - COMPARACION DE RANKINGS")
    print("=" * 48)
    print("Peliculas:", n)
    print("Criterios:", len(CRITERIOS))
    print("Maximo de inversiones entre dos rankings:",
          maximo_inversiones(n))

    print("\nTOP 5 POR CADA INDICADOR")
    print("-" * 48)

    for criterio in CRITERIOS:
        print("\n" + criterio)

        for posicion, nombre in enumerate(rankings[criterio][:5], 1):
            print(f"{posicion}. {nombre}")

    print("\nCOMPARACIONES")
    print("-" * 48)

    for r in comparaciones:
        print(
            f'{r["criterio_a"]} vs {r["criterio_b"]}: '
            f'{r["inversiones"]} inversiones '
            f'({r["diferencia"]:.2f}% de diferencia)'
        )

    menor = min(comparaciones, key=lambda x: x["inversiones"])
    mayor = max(comparaciones, key=lambda x: x["inversiones"])

    print("\nINTERPRETACION")
    print("-" * 48)
    print(
        "Par mas parecido:",
        menor["criterio_a"], "vs", menor["criterio_b"],
        "-", menor["inversiones"], "inversiones"
    )
    print(
        "Par mas diferente:",
        mayor["criterio_a"], "vs", mayor["criterio_b"],
        "-", mayor["inversiones"], "inversiones"
    )

    print("\nArchivos generados:")
    print("-", ARCHIVO_RANKINGS)
    print("-", ARCHIVO_COMPARACIONES)


def main():
    peliculas = leer_peliculas(ARCHIVO_DATOS)

    if len(peliculas) == 0:
        print("No existen datos para procesar.")
        return

    rankings = generar_rankings(peliculas)
    comparaciones = comparar_todos(rankings)

    guardar_rankings(rankings)
    guardar_comparaciones(comparaciones)
    mostrar_resultados(rankings, comparaciones)


main()
