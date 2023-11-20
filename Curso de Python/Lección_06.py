# Lección No.5 - Ciclos / Bucles

# --------- WHILE --------- #

""" condicion = True

while condicion:
    print("Ejecutando ciclo while")
else:
    print("Fin del ciclo while.")
 """

""" contador = 0
while contador < 3:
    print(contador)
    contador += 1 # Contador se incrementa en 1
else:
    print("Fin del ciclo while") """

# Ejercicio No.18 - Imprimir numeros del 0 al 5

""" num = 0

while num <= 5:
    print(num)
    num += 1
else:
    print("Fin del ciclo.") """

# Ejercicio No.19 - Imprimir números del 5 al 0 (de forma descendente)

""" num = 5

while num >= 0:
    print(num)
    num -= 1
else:
    print("Fin del ciclo.") """

# --------- FOR - EACH --------- #

""" cadena = "Hola"

for letra in cadena:
    print(letra)
else:
    print("Fin del ciclo.") """


# "break" en ciclos

""" for letra in "Holanda":
    if letra == "a":
        print(f"Letra encontrada: {letra}.")
        break
else:
    print("Fin del ciclo.") """

# "continue" en ciclos

""" for i in range(6):
    if i % 2 == 0:
        print(f"Valor: {i}") """

""" for i in range(6):
    if i % 2 != 0:
        continue
    print(f"Valor: {i}") """