#!/usr/bin/env python3
import random
import os

selected_filename= "wordlist_1.txt"

CATEGORIAS = {
    "A": {"nombre": "Palabras cortas", "archivo": "wordlist_1.txt"},
    "B": {"nombre": "Palabras largas", "archivo": "wordlist_2.txt"},
}

def get_filename(opcion):
    global selected_filename
    cat = CATEGORIAS.get(opcion.strip().upper())
    if cat is not None:
        selected_filename = cat["archivo"]
        return True
    else:
     return None

def get_category_name():
    for cat in CATEGORIAS.values():
        if cat["archivo"] == selected_filename:
            return cat["nombre"]
    return None

def get_random_word():
    """Este metodo obtiene todas las palabras del juego de forma aleatoria."""
    with open(selected_filename, "r", encoding="utf-8") as file:
        content = file.read()
        lineas = content.splitlines()
    return random.choice(lineas).strip().lower()

    
def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")
