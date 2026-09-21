# Proyecto Final - Rankings de Películas

Este proyecto fue realizado para la materia de Análisis de Algoritmos. La idea principal fue trabajar con un conjunto de películas y comparar los rankings que se obtienen utilizando diferentes indicadores.

Para realizar las comparaciones se utilizó Merge Sort para ordenar las películas y el método de conteo de inversiones para identificar qué tanto cambia el orden de las películas entre un ranking y otro.

## ¿Qué hace el proyecto

El programa trabaja con cuatro indicadores

 Tomatometer %
 Fresh
 Rotten
 Popcornmeter %

A partir de estos datos se generan diferentes rankings de las películas. Después se comparan los rankings entre sí para contar cuántas posiciones cambian.

Mientras más inversiones existan entre dos rankings, mayor es la diferencia en el orden de las películas.

## Organización del proyecto

```text
proyecto_final_rankings_peliculas
│
├── codigo
│   ├── algoritmos.py
│   ├── experimentos.py
│   ├── generar_sinteticos.py
│   ├── main.py
│   └── pruebas.py
│
├── datos
│   ├── pelis.csv
│   ├── pelis.xlsx
│   └── pelis_sinteticas.csv
│
├── resultados
│   ├── comparaciones.csv
│   └── rankings.csv
│
└── Ejecucion Algoritmo G1.pdf
```

## ¿Cómo ejecutarlo

Se necesita tener Python instalado.

Desde la carpeta principal del proyecto se puede ejecutar

```bash
python codigomain.py
```

Este programa genera los rankings y realiza las comparaciones entre los diferentes criterios.

Para ejecutar las pruebas

```bash
python codigopruebas.py
```

También se puede generar un conjunto de datos sintéticos para realizar pruebas

```bash
python codigogenerar_sinteticos.py
```

Y para observar el comportamiento del algoritmo con diferentes tamaños de entrada

```bash
python codigoexperimentos.py
```

No se necesitan librerías externas para ejecutar el proyecto.

## Algoritmos utilizados

El algoritmo principal utilizado para ordenar las películas es Merge Sort, cuya complejidad temporal es

O(n log n)

Para comparar los rankings se utiliza el conteo de inversiones mediante una modificación del proceso de Merge. De esta manera se puede obtener la cantidad de pares de películas que cambian de posición entre dos rankings.

La versión de fuerza bruta también fue implementada para poder comprobar los resultados obtenidos por el algoritmo de conteo de inversiones.

## Datos

El conjunto utilizado contiene 35 películas reales con los indicadores utilizados para generar los rankings.

También se incluye un archivo con datos sintéticos que permite probar el algoritmo con una cantidad mayor de registros.

## Resultados

Los resultados generados por el programa se guardan en la carpeta `resultados`.

 `rankings.csv` contiene los rankings generados para cada indicador.
 `comparaciones.csv` contiene las comparaciones entre los diferentes rankings y el número de inversiones encontrado.

