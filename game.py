#!/usr/bin/env python3
from utils import get_random_word


class HangmanGame():
    def __init__(self):
        self.word = get_random_word()
        self.guessed_letters = []
        self.max_errors = 6
        self.errors = 0
        self.processed_letters = [] # guarda todas las letras jugadas

    def display_progress(self):
        '''para mostrar el estado actual de la palabra (por ejemplo, "_ _ e _ _ a _ _").'''
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
        if self.errors >= self.max_errors:
            return True
        else:
            return False    

    def is_won(self):
        if "_" not in self.display_progress():
            return True
        else:
            return False
