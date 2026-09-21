# Mini Proyecto Final - Análisis de Algoritmos

# Comparación de rankings de películas mediante inversiones

# Integrantes:
# Arias Aucapena Andrey Alejandro
# Escobar Bailón Sebastián Andrey
# Mendoza Placencia Luis Alejandro
# Terán Mendoza Guillermo Isaac

# - Los elementos son registros de películas.
# - Los rankings se generan usando los indicadores del archivo.
# - Los empates se resuelven alfabéticamente por nombre.
# - Dos rankings se comparan convirtiendo el segundo en posiciones.
# - Durante el merge se cuentan inversiones cruzadas.

# Referencias
# [1] Cormen, Leiserson, Rivest y Stein, Introduction to Algorithms,
#     3rd ed., pp. 29-36 (Merge Sort) y pp. 41-42 (Problema 2-4:
#     Inversions).
# [2] Kleinberg y Tardos, Algorithm Design, sec. 5.3,
#     pp. 221-224 (Counting Inversions y comparación de rankings).
# [3] Goodrich, Tamassia y Goldwasser, Data Structures and Algorithms
#     in Python, sec. 12.2, pp. 538-547 (Merge-Sort en Python).



import csv


def leer_peliculas(ruta):
    """Lee el archivo CSV y devuelve una lista de diccionarios."""
    peliculas = []

    with open(ruta, "r", encoding="utf-8-sig", newline="") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            pelicula = {
                "Nombre": fila["Nombre"].strip(),
                "Tomatometer %": int(float(fila["Tomatometer %"])),
                "Fresh": int(float(fila["Fresh"])),
                "Rotten": int(float(fila["Rotten"])),
                "Popcornmeter %": int(float(fila["Popcornmeter %"])),
            }
            peliculas.append(pelicula)

    return peliculas


def va_antes(a, b, criterio):
    """
    Todos los indicadores se ordenan de mayor a menor, de acuerdo con
    la definicion formal del problema. Si hay empate, se usa el nombre.
    """
    if a[criterio] == b[criterio]:
        return a["Nombre"].lower() <= b["Nombre"].lower()

    return a[criterio] > b[criterio]


def mezclar(izquierda, derecha, criterio):
    resultado = []
    i = 0
    j = 0

    while i < len(izquierda) and j < len(derecha):
        if va_antes(izquierda[i], derecha[j], criterio):
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    while i < len(izquierda):
        resultado.append(izquierda[i])
        i += 1

    while j < len(derecha):
        resultado.append(derecha[j])
        j += 1

    return resultado


def merge_sort_peliculas(peliculas, criterio):
    """
    Merge Sort adaptado para ordenar registros de peliculas.
    Complejidad temporal: Theta(n log n).
    """
    if len(peliculas) <= 1:
        return peliculas[:]

    mitad = len(peliculas) // 2

    izquierda = merge_sort_peliculas(peliculas[:mitad], criterio)
    derecha = merge_sort_peliculas(peliculas[mitad:], criterio)

    return mezclar(izquierda, derecha, criterio)


def merge_contando(izquierda, derecha):
    """
    Mezcla dos listas ordenadas y cuenta las inversiones cruzadas.
    """
    mezcla = []
    inversiones = 0
    i = 0
    j = 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            mezcla.append(izquierda[i])
            i += 1
        else:
            mezcla.append(derecha[j])
            j += 1

            # Si derecha[j-1] es menor que izquierda[i], tambien es
            # menor que todos los elementos restantes de izquierda.
            inversiones += len(izquierda) - i

    while i < len(izquierda):
        mezcla.append(izquierda[i])
        i += 1

    while j < len(derecha):
        mezcla.append(derecha[j])
        j += 1

    return mezcla, inversiones


def contar_inversiones(secuencia):
    """
    Variante de Merge Sort para contar inversiones.
    Devuelve (secuencia_ordenada, cantidad_inversiones).
    """
    if len(secuencia) <= 1:
        return secuencia[:], 0

    mitad = len(secuencia) // 2

    izq_ordenada, inv_izq = contar_inversiones(secuencia[:mitad])
    der_ordenada, inv_der = contar_inversiones(secuencia[mitad:])

    mezcla, inv_cruzadas = merge_contando(izq_ordenada, der_ordenada)

    total = inv_izq + inv_der + inv_cruzadas
    return mezcla, total


def comparar_rankings(ranking_a, ranking_b):
    """
    Convierte el orden del ranking A a las posiciones que esos mismos
    elementos tienen en B. Luego cuenta las inversiones de esa secuencia.
    """
    if set(ranking_a) != set(ranking_b):
        raise ValueError("Los rankings no contienen las mismas peliculas.")

    posiciones_b = {}

    for posicion, nombre in enumerate(ranking_b):
        posiciones_b[nombre] = posicion

    secuencia = []

    for nombre in ranking_a:
        secuencia.append(posiciones_b[nombre])

    _, inversiones = contar_inversiones(secuencia)

    return inversiones, secuencia


def maximo_inversiones(n):
    return n * (n - 1) // 2


def porcentaje_diferencia(inversiones, n):
    """
    Medida auxiliar:
    0% = mismo orden.
    100% = orden completamente inverso.
    """
    maximo = maximo_inversiones(n)

    if maximo == 0:
        return 0.0

    return 100.0 * inversiones / maximo


def contar_inversiones_fuerza_bruta(secuencia):
    """
    Version O(n^2) usada solamente para validar las pruebas.
    """
    total = 0

    for i in range(len(secuencia)):
        for j in range(i + 1, len(secuencia)):
            if secuencia[i] > secuencia[j]:
                total += 1

    return total
