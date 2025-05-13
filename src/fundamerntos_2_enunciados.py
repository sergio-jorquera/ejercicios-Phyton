# 🧪 Fundamentos Python II
# Listas, Tuplas, Diccionarios, Sets

# ------------------------------
# LISTAS
# ------------------------------

# ✨ Ejercicio 1: Lista de la compra
# Crea una lista con al menos 5 elementos. Muestra el primero y el último elemento.

compra = ["fruta", "pan", "yogures", "pollo", "leche"]
print(compra[0], compra[4])


# ✨ Ejercicio 2: Añadir y eliminar
# Añade un nuevo elemento a la lista anterior y elimina otro. Imprime la lista actualizada.

compra.append("huevos")
compra.remove("pollo")
print(compra)

# ✨ Ejercicio 3: Ordenar números
# Crea una lista de números desordenados y ordénala de menor a mayor.

numeros = [1, 6, 3, 9, 5]
numeros.sort()
print(numeros)
# ------------------------------
# TUPLAS
# ------------------------------

# ✨ Ejercicio 4: Coordenadas
# Crea una tupla con una coordenada (latitud, longitud) y muéstrala.

coordenada = (40.4168, -3.7038)  
print(coordenada)

# ✨ Ejercicio 5: Elemento fijo
# Crea una tupla de 3 elementos. Intenta cambiar uno y observa qué sucede.
fechas = ("15/03", "16/05", "03/01")
#fechas[0] = "20/12"

# ------------------------------
# DICCIONARIOS
# ------------------------------

# ✨ Ejercicio 6: Diccionario de usuario
# Crea un diccionario con las claves: nombre, edad, ciudad.

diccionario = {"nombre": "Andrés", "edad":"37", "ciudad":"Avilés"}
print(diccionario)

# ✨ Ejercicio 7: Actualizar valores
# Cambia el valor de ciudad y añade una nueva clave llamada email.
diccionario["ciudad"] = "Oviedo"             # Cambiar el valor de la clave "ciudad"
diccionario["email"] = "andres@mail.com"     # Añadir una nueva clave "email"

print(diccionario)


# ✨ Ejercicio 8: Iterar claves y valores
# Imprime cada clave y su valor en una línea distinta.

print("/Pares clave-valor/")
for clave, valor in diccionario.items():
    print(f"{clave}: {valor}")

# ------------------------------
# SETS
# ------------------------------

# ✨ Ejercicio 9: Eliminar duplicados
# A partir de una lista con nombres repetidos, crea un set para mostrar solo los nombres únicos.

set = {"Ana", "María", "Juan", "Manuel", "Ana", "Manuel"}
print(set)

# ✨ Ejercicio 10: Operaciones de conjuntos
# Dado dos sets A y B, muestra qué elementos están en A pero no en B.

A = {"Ana", "María", "Juan", "Manuel"}
B = {"Ana", "Pepe", "Juan", "Andrea"}

resultado = A.difference(B)
print(resultado)

# ------------------------------
# EXTRA
# ------------------------------

# 🌟 Ejercicio Extra: Mezcla total
# Crea un diccionario donde cada clave sea el nombre de una persona y el valor una lista de hobbies.
# Añade un nuevo hobby a una persona y muestra todos los hobbies de otra.

hobbies = {
    "Ana": ["Tenis", "Lectura"],
    "María": ["Música"],
    "Juan": ["Pesca", "Ajedrez"],
    "Manuel": ["Montaña"]
}

# Añadir un nuevo hobby a una persona
hobbies["Ana"].append("Bailar")

# Mostrar todos los hobbies de otra persona
print("Hobbies de Juan:", hobbies["Juan"])
#Mostramos todos los valores del diccionario
for persona, lista_hobbies in hobbies.items():
    print(f"{persona}: {', '.join(lista_hobbies)}")