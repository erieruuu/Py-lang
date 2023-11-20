# Lección No.6 - Colecciones

# ----- LISTAS ----- #
# Es un conjunto de varios datos llamados elementos

""" nombres = ["Juan", "Karla", "Ricardo", "María"] """

# Imprimir lista
""" print(nombres, "\n") """

# Acceder a los elementos
""" print(nombres[0])
print(nombres[1])
print(nombres[2])
print(nombres[3], "\n") """

# Acceder a los elementos de manera inversa
""" print(nombres[-1])
print(nombres[-2])
print(nombres[-3])
print(nombres[-4], "\n") """

# Imprimir un rango
""" print(nombres[0 : 2], "\n") """

# Ir del inicio de la lista al índice (sin incluirlo)
""" print(nombres[  : 3], "\n") """

# Desde el índice indicado hasta el final de nuestra lista
""" print(nombres[1 :  ], "\n") """

# Cambiar un valor
""" nombres[3] = "Ivonne"
print(nombres, "\n") """

# Iterar lista
""" for nombre in nombres:
    print(nombre)
else:
    print("No existen más nombres en la lista.") """

# Preguntar largo de una lista "len()"
""" print(len(nombres), "\n") """

# Agregar un nuevo elemento "append()"
""" nombres.append("Lorenzo")
print(nombres, "\n") """

# Insertar elemento en un índice específico "insert()"
""" nombres.insert(1, "Octavio")
print(nombres, "\n") """

# Remover un elemento "remove()"
""" nombres.remove("Octavio")
print(nombres, "\n") """

# Remover el último valor agregado "pop()"
""" nombres.pop()
print(nombres, "\n") """

# Eliminar un elemento en un índice específico "del"
""" del nombres[0]
print(nombres, "\n") """

# Limpiar la lista "clear()"
""" nombres.clear()
print(nombres) """

# Borrar la lista por completo "deñ {Lista}"
""" del nombres """

# Ejercicio No.20 - Uso de rangos

## Iterar un rango de 0 a 10 e imprimir números divisibles entre 3
""" for i in range(0, 11):
    if i % 3 == 0:
        print(i)
print("\n") """

## Crear un rango de números de 2 a 6 e imprimirlos
""" for i in range(2, 7):
    print(i)
print("\n") """

## Crear un rango de 3 a 10, incremento de 2, en lugar de 1
""" for i in range(3, 11, 2):
    print(i)
print("\n") """

# ----- TUPLAS ----- #
# Es una lista no modificable


""" frutas = ("Naranja", "Plátano", "Guayaba")
print(frutas, "\n") """

# Determinar el largo
""" print(len(frutas), "\n") """

# Acceder a un elemento
""" print(frutas[0], "\n") """

# Navegación inversa
""" print(frutas[-1], "\n") """

# Acceder a un rango de valores
""" print(frutas[0:1], "\n") """ # Sin incluir el último índice

# Recorrer los elementos
""" for fruta in frutas:
    print(fruta, end=" ") """

# Cambiar valores 
# Se convierte a lista, se cambia el valor y luego se vuelve a convertir en tupla

""" frutasLista = list(frutas)
frutasLista[0] = "Pera"
frutas = tuple(frutasLista)
print(frutas, "\n") """

# Eliminar la tupla "del"
""" del frutas """

# Ejercicio No.21 - Uso de tuplas y listas
# Dada la siguiente tupla, se debe crear un lista que incluya los números menores a 5

""" tupla = (13,1,8,3,2,5,8)
lista = []

for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)
        
print(lista) """

# ----- SET ----- #

# Son listas que no guardan orden y no se repiten sus elementos
""" planetas = {"Marte", "Júpiter", "Venus"}
print(planetas, "\n") """

# Largo "len()"
""" print(len(planetas), "\n") """

# Preguntar sobre un elemento específico "{elemento} in {set}"
""" print("Marte" in planetas, "\n") """

# Agregar elemento "add()"
""" planetas.add("Tierra")
print(planetas, "\n") """

# Eliminar elementos posiblemente arrojando error "remove()"
""" planetas.remove("Tierra")
print(planetas, "\n") """

# Eliminar sin arrojar error "discard()"
""" planetas.discard("Júpiter")
print(planetas, "\n") """

# Limpiar set por completo "clear()"
""" planetas.clear()
print(planetas, "\n") """

# Eliminar el set "del"
""" del planetas """

# ----- DICCIONARIOS ----- #
# diccionario (key, value)

""" diccionario = {
    "IDE" : "Integrated Development Environment",
    "OOP" : "Object Oriented Programming",
    "DBMS" : "Database Management System"
}
print(diccionario, "\n") """

# Largo
""" print(len(diccionario), "\n") """

# Acceder a un elemento (key)
""" print(diccionario["IDE"], "\n") """

# Otra forma de recuperar un elemento 
""" print(diccionario.get("OOP"), "\n") """

# Modificar elementos 
""" diccionario["IDE"] = "integrated development environment"
print(diccionario, "\n") """

# Recorrer elementos "items()"
""" for termino, valor in diccionario.items():
    print(termino, valor)
print("\n") """
# Solo elemento "keys()"
""" for termino in diccionario.keys():
    print(termino)
print("\n") """
# Solo valor "values()"
""" for valor in diccionario.values():
    print(valor)
print("\n") """

#Comprobar existencia de algún elemento
""" print("IDE" in diccionario, "\n") """

# Agregar elementos
""" diccionario["PK"] = "Primary Key"
print(diccionario, "\n") """

# Remover elemento "pop()"
""" diccionario.pop("DBMS") """

# Limpiar un diccionario "clear()"
""" diccionario.clear()
print(diccionario, "\n") """

# Eliminar por completo
""" del diccionario """