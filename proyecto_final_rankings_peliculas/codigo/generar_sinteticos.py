# Generador de datos sinteticos.

from pathlib import Path
import csv
import random


BASE = Path(__file__).resolve().parent.parent
SALIDA = BASE / "datos" / "pelis_sinteticas.csv"

CANTIDAD = 500
SEMILLA = 2026


def main():
    random.seed(SEMILLA)

    with open(SALIDA, "w",
              newline="", encoding="utf-8-sig") as archivo:
        escritor = csv.writer(archivo)

        escritor.writerow([
            "Nombre",
            "Tomatometer %",
            "Fresh",
            "Rotten",
            "Popcornmeter %",
        ])

        for i in range(1, CANTIDAD + 1):
            escritor.writerow([
                f"Pelicula sintetica {i:04d}",
                random.randint(0, 100),
                random.randint(0, 600),
                random.randint(0, 300),
                random.randint(0, 100),
            ])

    print("Archivo creado:", SALIDA)
    print("Cantidad:", CANTIDAD)


main()
