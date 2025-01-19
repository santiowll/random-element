"""
Este script permite al usuario ingresar una lista de animes y luego selecciona uno al azar para mostrarlo.

Funciones:
    - random_anime: Función importada del módulo `random_anime` que selecciona un anime al azar de una lista.

Variables:
    - anime_lista: Lista que almacena los nombres de los animes ingresados por el usuario.

Flujo del programa:
    1. Solicita al usuario que ingrese nombres de animes.
    2. Almacena los nombres en la lista `anime_lista`.
    3. Cuando el usuario ingresa 'q', se detiene la entrada de datos.
    4. Llama a la función `random_anime` para seleccionar y mostrar un anime al azar de la lista.
"""

from modules.random_anime import random_anime as random_anime

from typing import List

anime_lista: List[str] = []

while True:
    anime = input("Escribe el anime que poner en una ruleta (escribe 'q' para salir): ").lower()
    if anime != 'q':
        anime_lista.append(anime)
    else:
        break

random_anime(anime_lista)
