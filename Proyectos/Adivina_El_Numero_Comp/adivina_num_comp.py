import random

def adivina_el_numero_comp(x):
    print("========================")
    print("¡Bienvenido(a) al juego!")
    print("========================")
    print(f"Selecciona un número entre 1 y {x} para que la computadora intente adivinar.")

    lim_inf = 1
    lim_sup = x
    
    resp = ""
    predict = 0

    while resp != "c":
        #Generar predicción
        if lim_inf != lim_sup:
            predict = random.randint(lim_inf, lim_sup)
        else:
            predict = lim_inf

        resp = input(f"Mi predicción es {predict}. Si es muy alta, ingresa (A). Si es muy baja, ingresa (B). Si es correcta, ingresa (C): ").lower()
        # Pedir al usuario su respuesta
        if resp == "a":
            lim_sup = predict - 1
        elif resp == "b":
            lim_inf = predict + 1
            
    print(f"¡Sí! La computadora adivinó tu número correctamente: {predict}")

adivina_el_numero_comp(10)