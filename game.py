#!/usr/bin/env python3

Utils = __import__('utils').Utils

class HangmanGame():
    def __init__(self, word="TITANIC", guessed_letters=[], max_errors=6, errors=0):
        self.word = Utils.get_random_word("wordlist.txt")
        self.guessed_letters = []
        self.max_errors = max_errors
        self.errors = errors

    def display_progress(self):
        self.__display = []
        if self.guessed_letters == []:
            for f in range (len(self.word)):
                self.__display.append("_")
        elif self.len(guessed_letters) > 0:
            self.__display = guessed_letters
        return self.__display

    def guessed_letters(self):
        self.letra = input("ingrese letra: ")
        for f in self.word:
            if letra == self.display[f]:
                self._display[f]=letra


juego = HangmanGame()
tablero = juego.display_progress()
print (tablero)

