# Lección No.5 - Sentencias de Control (if-else)

# Ejercicio No.14 - Conversion de números a texto

""" numero = int(input("Proporciona un valor entre 1 y 3: "))

if numero == 1:
    numeroTexto = "Número uno"
elif numero == 2:
    numeroTexto = "Número dos"
elif numero == 3:
    numeroTexto = "Número tres"
else:
    numeroTexto = "Valor fuera de rango."
    
print(f"Número proporcionado: {numero} || {numeroTexto}.") """

# Operador ternario (abreviatura de if-else)

""" condicion = True
# Forma convencional
if condicion == True:
    print("Condicion verdadera.")
else:
    print("Condicion falsa.")
# Utilizando operador ternario (recomendado solo en sentencias pequeñas)
print("Condicion verdadera.") if condicion else print("Condicion falsa.") """

# Ejercicio No.15 - Calcular la estación según el mes proporcionado

""" mes = input("Proporciona el mes del año: ")
estacion = None

if mes == "Diciembre" or mes == "Enero" or mes == "Febrero":
    estacion = "Invierno"
elif mes == "Marzo" or mes == "Abril" or mes == "Mayo":
    estacion = "Primavera"
elif mes == "Junio" or mes == "Julio" or mes == "Agosto":
    estacion = "Verano"
elif mes == "Septiembre" or mes == "Octubre" or mes == "Noviembre":
    estacion = "Otoño"
else:
    estacion = "Mes incorrecto."
print(f"Para el mes de {mes} la estación es: {estacion}") """

# Ejercicio No.16 - Etapas de Vida según edad

""" edad = int(input("Proporciona tu edad: "))

if 0 <= edad < 10:
    mensaje = "La infancia es increíble..."
elif 10 <= edad < 20:
    mensaje = "Muchos cambios y mucho estudio..."
elif 20 <= edad <= 30:
    mensaje = "Llega el amor y comienza el trabajo..."
else:
    mensaje = "Etapa de vida no reconocida."
print (f"Tu edad es: {edad}. {mensaje}") """

# Ejercicio No.17 - Sistema de calificaciones

""" calificacion = int(input("Proporcione una calificación (1 al 10): "))

if 9 <= calificacion <= 10:
    nota = "A"
elif 8 <= calificacion < 9:
    nota = "B"
elif 7 <= calificacion < 8:
    nota = "C"
elif 6 <= calificacion < 7:
    nota = "D"
elif 0 <= calificacion < 6:
    nota = "F"
else:
    nota = "Calificación no válida."

print(f"Tu calificación es: {calificacion}. Tu nota es {nota}.") """