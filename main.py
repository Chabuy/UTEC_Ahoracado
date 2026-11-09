#!/usr/bin/env python3
from utils import get_random_word, get_filename, get_category_name, limpiar_pantalla
from game import HangmanGame




while True:
    limpiar_pantalla()
    print("    HANGMAN GAME")
    print("=" * 20 + "\n")
    print (" Categorias: \n A-Palabras cortas  \n B-Palabras largas")
    print("=" * 20 + "\n")
    opcion =  input("elija una categoria para comenzar: ").strip().upper()

    if get_filename(opcion) is not None:
        break
    input("el valor elegido no es correcto. Presiona [Enter] y Reintenta.")
    
partida = HangmanGame()
categoria = get_category_name()

while True:  
    limpiar_pantalla()
    print("    HANGMAN GAME")
    print("=" * 20 + "\n")
    print(f"Nombre categoria:  {categoria}")
    print(f"Letras jugadas:    {', '.join(partida.processed_letters)}")
    print(f"Progreso actual:   {partida.display_progress()}")
    print(f"Errores cometidos: {partida.errors} / {partida.max_errors}")
    print("\n" + "=" * 20 + "\n")

    letra = input("Ingresa una letra y presiona la tecla [Enter]: ").strip().lower()
    partida.process_guess(letra)
    
    if partida.is_lost() == True:
        limpiar_pantalla()
        print("    HANGMAN GAME")
        print("=" * 20 + "\n")
        print(f"Letras jugadas:    {', '.join(partida.processed_letters)}")
        print(f"Progreso actual:   {partida.display_progress()}")
        print(f"Errores cometidos: {partida.errors} / {partida.max_errors}")
        print("\n" + "=" * 20 + "\n")
        print(f"La letra {letra} no forma parte de la palabra.")
        limpiar_pantalla()
        print("    HANGMAN GAME")
        print("=" * 20 + "\n")
        print(f"Letras jugadas:    {', '.join(partida.processed_letters)}")
        print(f"Progreso actual:   {partida.display_progress()}")
        print(f"Errores cometidos: {partida.errors} / {partida.max_errors}") 
        print("=" * 20 + "\n")
        print ("PERDISTE :(")
        print (f"La palabra era: {partida.word}")
        input (f"Presiona [Enter] para continuar ")
        break
    
    if partida.is_won() == True:
        limpiar_pantalla()
        print("    HANGMAN GAME")
        print("=" * 20 + "\n")
        print(f"Letras jugadas:    {', '.join(partida.processed_letters)}")
        print(f"Progreso actual:   {partida.display_progress()}")
        print(f"Errores cometidos: {partida.errors} / {partida.max_errors}")
        print("\n" + "=" * 20 + "\n")
        print("¡FELICITACIONES, GANASTE!")
        print(f"Adivinaste la palabra: {partida.word}")
        input (f"Presiona [Enter] para continuar")
        break
