#!/usr/bin/env python3
"""Módulo de utilidades y funciones auxiliares para el juego del Ahorcado."""

import random
import os

# Archivo por defecto para cargar palabra
selected_filename= "wordlist_1.txt"

# Diccionario de categorías disponibles con su descripción y archivo de palabras
CATEGORIAS = {
    "A": {"nombre": "Palabras cortas (fácil)", "archivo": "wordlist_1.txt"},
    "B": {"nombre": "Palabras largas (intermedio)", "archivo": "wordlist_2.txt"},
    "C": {"nombre": "Peliculas (dificil)", "archivo": "wordlist_3.txt"},
}

def get_filename(opcion):
    """Establece el archivo de palabras según la opción de categoría elegida.
    Actualiza la variable global 'selected_filename' si la opción es válida."""
    global selected_filename
    cat = CATEGORIAS.get(opcion.strip().upper())
    if cat is not None:
        selected_filename = cat["archivo"]
        return True
    else:
     return None

def get_category_name():
    """Obtiene el nombre legible de la categoría actualmente seleccionada."""
    for cat in CATEGORIAS.values():
        if cat["archivo"] == selected_filename:
            return cat["nombre"]
    return None


def get_random_word():
    """Este metodo obtiene todas las palabras del juego de forma aleatoria desde el archivo de la categoria elegida."""
    with open(selected_filename, "r", encoding="utf-8") as file:
        content = file.read()
        lineas = content.splitlines()
    return random.choice(lineas).strip().lower()

    
def limpiar_pantalla():
    """Limpia la terminal de comandos según el sistema operativo detectado."""
    os.system("cls" if os.name == "nt" else "clear")
