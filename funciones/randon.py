import random

numero_secreto = random.randint(1, 50)
intentos_realizados = 0
max_intentos = 5



while intentos_realizados < max_intentos:
    rango_minimo = 1
    rango_maximo = 50
    print(f"Intento {intentos_realizados + 1}/{max_intentos}")
    numero_adivinado = int(input(f"Ingrese un número entre {rango_minimo} y {rango_maximo}: "))
    intentos_realizados += 1

    if numero_adivinado == numero_secreto:
        print(f"Felicidades adivinastes{intentos_realizados} intentos!")
        break
    elif numero_adivinado < numero_secreto:
        print("El número secreto es mayor.")
    else:
        print("El número secreto es menor.")

if numero_adivinado != numero_secreto:
    print(f"Perdiste el número secreto era {numero_secreto}.")
