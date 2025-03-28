"""
Este script permite al usuario ingresar una lista de elementos y luego selecciona uno al azar para mostrarlo.

Funciones:
    - random_element: Función importada del módulo `random_element` que selecciona un elemento al azar de una lista.

Variables:
    - elementos_lista: Lista que almacena los elementos ingresados por el usuario.

Flujo del programa:
    1. Solicita al usuario que ingrese elementos.
    2. Almacena los nombres en la lista `elementos_lista`.
    3. Cuando el usuario ingresa 'q', se detiene la entrada de datos.
    4. Llama a la función `random_element` para seleccionar y mostrar un elemento al azar de la lista.
"""

from modules.random_element import random_element as random_element

from typing import List

elementos_lista: List[str] = []

while True:
    elemento = input("Escribe el elemento que queres poner en la ruleta (escribe 'q' para salir): ").lower()
    if elemento != 'q':
        elementos_lista.append(elemento)
    else:
        break

random_element(elementos_lista)
