#!/usr/bin/env python3
"""Módulo que contiene la lógica central del juego del Ahorcado."""

from utils import get_random_word


class HangmanGame():
    """clase del juego. Contiene el estado y las reglas del juego"""

    def __init__(self):
        """Inicializa una nueva partida del juego"""
        self.word = get_random_word() # palabra secreta de forma aleatoria
        self.guessed_letters = [] # Letras adivinadas correctamente
        self.max_errors = 6 # Límite máximo de errores permitidos
        self.errors = 0 # Cantidad actual de errores cometidos
        self.processed_letters = [] # guarda todas las letras jugadas por el usuario

    def display_progress(self):
        """Muestra el progreso de la palabra (letras adivinadas o guiones)."""
        palabra = ""
        for letra in self.word:
            if letra in self.guessed_letters:
                palabra = palabra + letra + " "
            elif letra.isalpha() == False:
                palabra = palabra + letra + " "
            else:
                palabra = palabra + "_ "
        return palabra.strip().lower()
        
    def process_guess(self, letter):
        """Procesa el intento del jugador con la letra ingresada."""

        self.letter = letter.strip().lower()
        if self.letter.isalpha() != True or len(self.letter) != 1:
            return input("el valor ingresado no es correcto, debe ser exactamente una letra. Reintenta. presiona [Enter]")
             
        if self.letter in self.processed_letters:
            return input("ya jugaste esta letra. Reintenta. presiona [Enter]")

        self.processed_letters.append(self.letter)

        if self.letter in self.word:
            self.guessed_letters.append(self.letter)
            return input(f"¡Bien! Acertaste. Presiona [Enter] para continuar")
        else:
            self.errors += 1
            return input(f"La letra {self.letter} no forma parte de la palabra. Reintenta. presiona [Enter]")

    def is_lost(self):
        """Determina si la partida ha finalizado en derrota"""
        
        if self.errors >= self.max_errors:
            return True
        else:
            return False    

    def is_won(self):
        """Determina si la partida ha finalizado con victoria."""
        
        if "_" not in self.display_progress():
            return True
        else:
            return False
