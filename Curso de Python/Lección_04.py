# Lección No.4 - Operadores

# Operadores aritméticos:|| + || - || * || / || // || ** || % ||
# Operadores de asignación: || += || -= || *= || /= ||
# Operadores de comparación: || == || != || > || >= || < || <= ||
# Operadores lógicos: 
# || and (devuelve True solo si ambos operandos son True) ||
# || or (devuelve True si: ambos operandos son True o uno de los dos es True; si ambos son False, devuelve false) ||
# || not (devuelve el valor contrario del valor del operando actual) ||

""" 
# Ejercicio No.5 - Calcular el área y perímetro de un rectángulo

# ---------------------------
# Instrucciones de la tarea:
# - En el siguiente ejercicio se solicita calcular el área y el perímetro de un Rectángulo,
# para ello deberemos crear las siguientes variables:

# alto (int)
# ancho (int)

# - El usuario debe proporcionar los valores de alto y ancho,
# y después se debe imprimir el resultado en el siguiente formato
# (no usar acentos y respetar los espacios, mayúsculas, minúsculas y saltos de línea):

# Proporciona el alto:
# Proporciona el ancho:
# Area: <area>
# Perímetro: <perímetro>

# Las formulas para calcular el area y el perímetro de un Rectángulo son:
# Area: alto * ancho
# Perímetro: (alto + ancho) * 2
# ---------------------------

altoRect = float(input("Proporciona el alto del rectángulo: "))
anchoRect = float(input("\nProporciona el ancho del rectángulo: "))

# Área
areaRect = altoRect * anchoRect
print(f"\nEl área del rectángulo es: {areaRect} m^2.")

# Perímetro
perímetroRect = (altoRect + anchoRect) * 2
print(f"\nEl perímetro del rectángulo es: {perímetroRect} m.")

# Ejercicio No.6 - Número par o impar

numero = int(input("\n\nPor favor ingrese un número: "))

if numero % 2 != 0:
    print(f"{numero} es un número impar.")
else:
    print(f"{numero} es un número par.")
    
# Ejercicio No.7 - Determinar si es mayor de edad o no

edadAdulto = 18
edadPersona = int(input("\n\nProporciona tu edad: "))

if edadPersona >= edadAdulto:
    print(f"La persona con edad {edadPersona} es mayor de edad.")
else:
    print(f"La persona con edad {edadPersona} es menor de edad.")

# Ejercicio No.8 - Valor dentro de rango (and)

valor = int(input("Escribe el valor: "))
valorMín = 0
valorMáx = 5
# dentroRango = (valor >= valorMín) and (valor <= valorMáx)
dentroRango = valor >= valorMín and valor <= valorMáx

if dentroRango:
    print(f"El valor {valor} está dentro de rango.")
else:
    print(f"El valor {valor} está fuera de rango.")
    
# Ejercicio No.9 - Asistir a un juego (or)

vacaciones = False
díaDescanso = False

if vacaciones or díaDescanso:
    print("Puede asistir al juego.")
else:
    print("Tiene deberes por hacer.")

# Ejercicio No.10 - Asistir a un juego (not)

vacaciones = False
díaDescanso = True

if not (vacaciones or díaDescanso):
    print("Tiene deberes por hacer.")
else:
    print("Puede asistir al juego.")
    
# Ejercicio No.11 - Rango entre 20's y 30's

edad = int(input("Introduce tu edad: "))
# rango20s = edad >= 20 and edad < 30
# rango30s = edad >= 30 and edad < 40


# if rango20s or rango30s:
#     print("Dentro de los 20's o 30's.")
# else:
#     print("No está dentro de los 20's ni 30's.")

if (20 <= edad < 30 ) or (30 <= edad < 40):
    print("Dentro de los 20's o 30's.")
else:
    print("No está dentro de los 20's ni 30's.")

    
# Ejercicio No.12 - El mayor de dos números
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

numMayor = num1 > num2

if numMayor:
    print(f"El primer número, {num1}, es el mayor.")
elif num1 == num2:
    print(f"Los números son iguales.")
else:
    print(f"El segundo número, {num2}, es el mayor.")
"""
# Ejercicio No.13 - Tienda de Libros
print("Proporcione los siguientes datos del libro.")

nombreLib = input("Proporcione el nombre: ")
idLib = input("Proporcione el ID: No.")
precioLib = float(input("Proporcione el precio: $"))
envíoGratis = bool(input("Indica si el envío es gratuito (True/False): "))

# print(f"\nNombre: {nombreLib}", f"\nID: No.{idLib}", f"\nPrecio: ${precioLib}", f"\nEl envío es gratis?: {envíoGratis}")
print(f"""
      Nombre: {nombreLib}
      ID: No.{idLib}
      Precio: ${precioLib}
      Envío Gratuito: {envíoGratis}
      """)