#!/usr/bin/env python3
import random

class Utils():

    def get_random_word(filename=""):
        """Este metodo obtiene todas las palabras del juego de forma aleatoria."""
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            lineas = content.splitlines()
        return random.choice(lineas)


#words = Utils.get_random_word("wordlist.txt")
#print(words)
