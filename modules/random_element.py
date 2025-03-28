"""Módulo que contiene la función random_element, la cual elige un elemento"""
import random
import time

from typing import List

def random_element(lista_de_elementos: List[str]):
    """Imprime en pantalla un elemento aleatorio de la lista de elementos que se le 
    pase como argumento."""
    numero_aleatorio = random.randint(0, len(lista_de_elementos) - 1)
    elemento_aleatorio = lista_de_elementos[numero_aleatorio]

    for num in range(3, 0, -1):
        print(f"{num}...")
        time.sleep(1)

    print(f"\nEl elemento elegido es: {elemento_aleatorio.title()}")
