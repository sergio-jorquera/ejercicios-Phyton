# 🧪 Ejercicios – Consola + Buenas Prácticas (KISS, DRY, Excepciones)

# Ejercicio 1: Sistema de votaciones
# -----------------------------------
# Crea un programa en consola con las siguientes opciones:
# 1. Añadir película
# 2. Votar por una película
# 3. Mostrar resultados
# 4. Salir
# Si se intenta votar por una película no registrada, muestra error (usa try/except con KeyError).
# Usa funciones separadas por funcionalidad.
# (Bonus: guardar votos en un fichero CSV)

import csv

peliculas = {}
archivo_csv = 'votos.csv'

# Cargar datos desde CSV si existe
def cargar_votos():
    try:
        with open(archivo_csv, mode='r', newline='') as f:
            lector = csv.reader(f)
            for fila in lector:
                if fila:  # evita líneas vacías
                    pelicula = fila[0].strip().lower()
                    peliculas[pelicula] = int(fila[1])
    except FileNotFoundError:
        pass  # El archivo no existe aún

# Guardar votos en CSV
def guardar_votos():
    with open(archivo_csv, mode='w', newline='') as f:
        escritor = csv.writer(f)
        for pelicula, votos in peliculas.items():
            escritor.writerow([pelicula.title(), votos])

def añadir_pelicula():
    nombre = input("Nombre de la película: ").strip().lower()
    if nombre in peliculas:
        print("La película ya está registrada.")
    else:
        peliculas[nombre] = 0
        print(f"Película '{nombre.title()}' añadida.")

def votar_pelicula():
    nombre = input("Nombre de la película a votar: ").strip().lower()
    try:
        peliculas[nombre] += 1
        print(f"¡Voto registrado para '{nombre.title()}'!")
    except KeyError:
        print("Error: la película no está registrada.")

def mostrar_resultados():
    if not peliculas:
        print("No hay películas registradas aún.")
    else:
        print("Resultados de la votación:")
        for pelicula, votos in peliculas.items():
            print(f"{pelicula.title()}: {votos} votos")

def menu():
    cargar_votos()
    while True:
        print("\n--- Sistema de Votaciones ---")
        print("1. Añadir película")
        print("2. Votar por una película")
        print("3. Mostrar resultados")
        print("4. Salir")

        opcion = input("Elige una opción (1-4): ").strip()

        if opcion == '1':
            añadir_pelicula()
        elif opcion == '2':
            votar_pelicula()
        elif opcion == '3':
            mostrar_resultados()
        elif opcion == '4':
            guardar_votos()
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar el programa





# Ejercicio 2: Limpieza de datos crudos
# -------------------------------------
# Dada una lista de nombres con errores (espacios, mayúsculas, duplicados),
# crea una función que la limpie devolviendo una lista ordenada y sin duplicados.
# Todos los nombres deben tener solo la primera letra en mayúscula.
# Muestra cuántos nombres únicos hay.
# 💡 Añade manejo de errores si algún elemento no es una cadena (TypeError o AttributeError)

lista = [
    '  Ana', 
    'ANA', 
    ' Pedro ', 
    'pedro', 
    ' Maria', 
    'maria ', 
    'JUAN', 
    ' juan', 
    ' JuAn ', 
    'Carlos', 
    'carlos  ', 
    'CARLOS'
]

def limpiar_lista(lista):
    nombres_limpios = set()

    for elemento in lista:
        try:
            limpiar = elemento.strip().title()
            nombres_limpios.add(limpiar)
        except (AttributeError, TypeError):
            print(f"Error: {elemento} no es una cadena válida.")
    
    lista_ordenada = sorted (nombres_limpios)

    print(f"Nombres únicos encontrados: {len(lista_ordenada)}")
    print(lista_ordenada)

    return lista_ordenada

limpiar_lista(lista)

if __name__ == "__main__":
    menu()
        



# Ejercicio 3: Analizador de texto
# --------------------------------
# Pide al usuario un párrafo.
# Luego:
# - Cuenta cuántas palabras contiene
# - Muestra cuántas veces aparece cada palabra
# - Muestra la palabra más repetida
# 💡 Controla que el texto no esté vacío. Usa ValueError.

parrafo = input(print("Introduce un párrafo"))

# Ejercicio 4: Simulador de inventario
# -------------------------------------
# Crea un sistema que permita gestionar productos en un inventario.
# Cada producto tiene nombre, stock y precio.
# Opciones:
# 1. Añadir producto
# 2. Actualizar stock
# 3. Eliminar producto
# 4. Ver inventario
# 💡 Usa try/except para validar entradas numéricas y para controlar si el producto no existe.

# Ejercicio 5: Generador de alias seguro
# ---------------------------------------
# Pide al usuario nombre y apellido, y genera un alias así:
# - 3 letras del apellido (mayúsculas)
# - 2 letras del nombre (minúsculas)
# - número aleatorio del 10 al 99
# - símbolo especial aleatorio
# 💡 Valida que el nombre y apellido tengan longitud suficiente (ValueError)

import random, string

def generar_alias():
    try:
        nombre = str(input("Introduce un nombre: "))
        apellido = str(input("Introduce un apellido: "))

        if type(nombre) or type(apellido) != type(str):
            raise ValueError("No es el tipo que se espera")
        if len(nombre) < 2:
            raise ValueError("El nombre debe tener al menos 2 letras.")
        if len(apellido) < 3:
            raise ValueError("El apellido debe tener al menos 3 letras.")

        nombre_modificado = nombre[0] + nombre[1] 
        apellido_modificado = apellido[0] + apellido[1] + apellido[2]
        numero = str(random.choice(range(10, 100)))
        simbolo = str(random.choice(list('!@#$%&*')))

        alias = nombre_modificado + apellido_modificado + numero + simbolo
        print("Tu alias es: ", alias)

    except ValueError as e:
         print(f"Error: {e}")

generar_alias()

# Ejercicio 6: Comprobador de contraseñas seguras
# ------------------------------------------------
# Pide una contraseña al usuario.
# Valida que:
# - Tiene al menos 8 caracteres
# - Contiene mayúsculas, minúsculas y números
# 💡 Usa raise y excepciones personalizadas con mensajes explicativos.

def comprobar_contrasena():
    try:
        contrasena = input("Introduce la contraseña: ")

        if len(contrasena) < 8:
            raise ValueError("La contraseña debe tener al menos 8 caracteres")
        if not any(c.isupper() for c in contrasena):
            raise ValueError("La contraseña debe tener al menos una mayúscula")
        if not any(c.islower() for c in contrasena):
            raise ValueError("La contraseña debe tener al menos una minúscula")
        if not any(c.isdigit() for c in contrasena):
            raise ValueError("La contraseña debe tener al menos un número")

    except ValueError as e:
         print(f"Error: {e}")

comprobar_contrasena()

# 🌟 Reto Extra: Simulador de reservas de hotel
# ----------------------------------------------
# Habitaciones del 101 al 110. El usuario puede:
# 1. Ver habitaciones disponibles
# 2. Reservar habitación (introduciendo su nombre)
# 3. Cancelar reserva
# 4. Ver reservas confirmadas
# 5. Salir
# Las reservas se almacenan en un diccionario {habitacion: nombre}
# Usa funciones y control de errores con KeyError si la habitación no existe.
# (Bonus: mostrar mapa visual, reservas múltiples, carga inicial aleatoria)
