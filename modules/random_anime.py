"""Módulo que contiene la función random_anime, la cual elige un anime"""
import random
import time

from typing import List

def random_anime(lista_de_animes: List[str]):
    """Imprime en pantalla un anime aleatorio de la lista de animes que se le 
    pase como argumento."""
    numero_aleatorio = random.randint(0, len(lista_de_animes) - 1)
    anime_aleatorio = lista_de_animes[numero_aleatorio]

    for num in range(3, 0, -1):
        print(f"{num}...")
        time.sleep(1)

    print(f"\nEl anime elegido es: {anime_aleatorio.title()}")
