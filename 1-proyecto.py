# El juego debe tener una lista de palabras predefinidas de las cuales se
# elige una palabra aleatoriamente para que el jugador adivine.
from random import randint

palabras = ["messi", "casa", "auto", "maradona", "river", "bicicleta"]
indice_palabras_max = len(palabras) - 1
indice_aleatorio = randint(0, indice_palabras_max)

palabra_aleatoria = palabras[indice_aleatorio] # palabra aleatoria

# El jugador tiene un número limitado de intentos para adivinar la palabra
# (por ejemplo, 6 intentos).
intentos = 6

# Debe mostrar las letras adivinadas y las letras incorrectas.
correctas = []
incorrectas = []
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
palabra_secreta = ['?'] * len(palabra_aleatoria)
print(palabra_secreta)
print(palabra_aleatoria)
# El juego debe verificar si la letra ingresada por el jugador está en la
# palabra secreta y actualizar el estado del juego en consecuencia.
letra_ingresada = input("Por favor ingrese una letra: ")

ind = 0
existe_letra = False
for letra in palabra_aleatoria: # messi
    if letra == letra_ingresada:
        existe_letra = True
        palabra_secreta[ind] = letra_ingresada

    ind += 1

if existe_letra:
    correctas.append(letra_ingresada)
else:
    incorrectas.append(letra_ingresada)
    intentos -= 1

letras.remove(letra_ingresada)


# El juego debe terminar cuando el jugador adivine la palabra o se quede
# sin intentos.

# Debe mostrar un mensaje de victoria o derrota al final del juego.
# Opcional: debe mostrar una representación gráfica del estado actual del
# ahorcado. Puedes usar arte ASCII para esto.