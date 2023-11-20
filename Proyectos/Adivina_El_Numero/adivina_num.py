# Programa simple para adivinar un número
import random


def adivina_el_numero(x):

    print("------------------------")
    print("¡Bienvenido(a) al juego!")
    print("------------------------")
    print("Tu meta es adivinar el número generado por la computadora.")

    numero_rndm = random.randint(1, x) # Número aleatorio entre 1 y x
    predict = 0

    while predict != numero_rndm:
        # Ingresar un número
        predict = int(input(f"Adivina un número entre 1 y {x}: "))
        if predict < numero_rndm:
            print("Intenta otra vez. El número es muy pequeño.")
        elif predict > numero_rndm:
            print("Intenta otra vez. El número es muy grande.")
    
    print(f"¡Felicidades! Adivinaste el número {numero_rndm} correctamente.")

print(f"ADIVINA EL NÚMERO")
adivina_el_numero(20)