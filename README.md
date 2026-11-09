# UTEC_Ahoracado

Juego interactivo del **Ahorcado (Hangman Game)** desarrollado en Python para consola. Este proyecto permite a los usuarios poner a prueba su vocabulario adivinando palabras secretas a través de una interfaz de texto limpia, organizada por categorías temáticas y niveles de dificultad.

---

## 📋 Descripción General

El objetivo clásico del juego consiste en descubrir una palabra oculta ingresando una letra a la vez, antes de agotar el límite de 6 intentos fallidos. El jugador puede seleccionar la categoría temática al inicio de la sesión, visualizando en tiempo real el progreso de la palabra, las letras ya utilizadas y el contador de errores.

---

## 🗂️ Estructura del Proyecto

El código está estructurado en módulos para separar responsabilidades:

- **`main.py`**: Punto de entrada del programa. Administra el flujo del menú principal, la interacción por consola con el usuario, la visualización en cada turno y la detección del desenlace de la partida (victoria o derrota).
- **`game.py`**: Define la clase `HangmanGame`, responsable de gestionar la lógica del juego (palabra secreta, letras ingresadas, registro de aciertos/errores y evaluación del estado de la partida).
- **`utils.py`**: Módulo con funciones utilitarias para la selección de categorías, lectura de archivos de texto, extracción aleatoria de palabras y limpieza de pantalla.
- **Archivos de palabras (`wordlist_*.txt`)**:
  - `wordlist_1.txt`: Palabras cortas (modo fácil).
  - `wordlist_2.txt`: Palabras largas (modo intermedio).
  - `wordlist_3.txt`: Títulos de películas (modo difícil).

---

## 🎮 Categorías Disponibles

Al ejecutar el juego, se presenta el siguiente menú para elegir la temática:

| Opción | Categoría | Dificultad | Archivo Fuente |
| :---: | :--- | :---: | :--- |
| **A** | Palabras cortas | Fácil | `wordlist_1.txt` |
| **B** | Palabras largas | Intermedio | `wordlist_2.txt` |
| **C** | Películas | Difícil | `wordlist_3.txt` |

---

## ⚙️ Reglas y Dinámica de Juego

1. **Selección inicial**: Elige una de las categorías válidas (`A`, `B` o `C`). Si se ingresa una opción inválida, el sistema solicitará intentarlo nuevamente.
2. **Ingreso de letras**: En cada turno, ingresa exactamente una letra del abecedario.
3. **Validación de entradas**:
   - Solo se aceptan caracteres alfabéticos individuales.
   - Si ingresas una letra que ya jugaste en esa partida, el juego te lo indicará sin sumarte un error adicional.
4. **Condición de derrota**: Cuentas con un máximo de **6 errores**. Al cometer el sexto error, la partida finaliza y se revela la palabra oculta.
5. **Condición de victoria**: Ganas la partida si logras descubrir todas las letras de la palabra antes de alcanzar el límite de errores.

---

## 🚀 Requisitos e Instalación

### Requisitos
- **Python 3.6** o superior.
- No requiere librerías externas (utiliza únicamente módulos de la biblioteca estándar de Python: `os` y `random`).

### Cómo ejecutar

1. Clona o descarga este repositorio en tu equipo.
2. Asegúrate de contar con los archivos de texto de palabras (`wordlist_1.txt`, `wordlist_2.txt`, `wordlist_3.txt`) en el mismo directorio.
3. Abre una terminal en la carpeta del proyecto y ejecuta:

```bash
python3 main.py
```
