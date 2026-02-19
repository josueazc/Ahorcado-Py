import random

palabras = ["gato", "perro", "casa", "libro", "sol"]
palabra = random.choice(palabras)

oculta = ["_"] * len(palabra)
intentos = 0

while intentos < 10 and "_" in oculta:
    print("Palabra:", " ".join(oculta))
    letra = input("Escribe una letra: ")

    if letra in palabra:
        for i in range(len(palabra)):
            if palabra[i] == letra:
                oculta[i] = letra
    else:
        intentos += 1
        print("Incorrecto. Intentos:", intentos)

if "_" not in oculta:
    print("¡Ganaste! La palabra era:", palabra)
else:
    print("Perdiste. La palabra era:", palabra)
