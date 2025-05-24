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

    
#if __name__ == "__main__":
    menu()



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

        
# Ejercicio 3: Analizador de texto
# --------------------------------
# Pide al usuario un párrafo.
# Luego:
# - Cuenta cuántas palabras contiene
# - Muestra cuántas veces aparece cada palabra
# - Muestra la palabra más repetida
# 💡 Controla que el texto no esté vacío. Usa ValueError.

import string
from collections import Counter

def contar_palabras():
    parrafo = input("Introduce un párrafo: ").strip()
    
    # Validar que no esté vacío
    if not parrafo:
        raise ValueError("El texto no puede estar vacío.")
    
    # Quitar puntuación y pasar a minúsculas
    tabla = str.maketrans("", "", string.punctuation)
    parrafo_limpio = parrafo.translate(tabla).lower()
    
    # Separar palabras
    palabras = parrafo_limpio.split()
    
    # Contar palabras
    total_palabras = len(palabras)
    contador = Counter(palabras)
    palabra_mas_repetida = contador.most_common(1)[0]  # (palabra, cantidad)
    
    # Mostrar resultados
    print(f"\nNúmero total de palabras: {total_palabras}")
    print("\nFrecuencia de cada palabra:")
    for palabra, cantidad in contador.items():
        print(f"  {palabra}: {cantidad}")
    
    print(f"\nPalabra más repetida: '{palabra_mas_repetida[0]}' ({palabra_mas_repetida[1]} veces)")


    
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

inventario = {}

def mostrar_menu():
    print("1. Añadir producto")
    print("2. Actualizar stock")
    print("3. Eliminar producto")
    print("4. Ver inventario")
    print("5- Salir")


def añadir_producto():
    nombre_producto = input("Introduce el nombre del producto: ").strip().lower()
    if nombre_producto not in inventario:
        try:
            stock = int(input("stock: "))
            precio = float(input("precio: "))
            inventario[nombre_producto] = {"stock": stock, "precio": precio}
            print(f"El producto {nombre_producto} se ha añadido con éxito")
        except ValueError:
            print("Ingresa un número válido para stock y precio")
    else:
        print(f"El producto {nombre_producto} ya existe")

def actualizar_stock():
    nombre_producto = input("Introduce el nombre del producto del que quieras actualizar stock: ").strip().lower()   
    if nombre_producto in inventario:
        try:
            nuevo_stock = int(input("nuevo stock: "))
            inventario[nombre_producto] ["stock"] = nuevo_stock
            print(f"El stock de {nombre_producto} se ha actualizado")
        except ValueError:
            print("El valor debe de ser un número entero")
    else:
        print("El producto no se encuentra en el inventario")

def eliminar_producto():
    nombre_producto = input("Introduce el nombre del producto a eliminar: ").strip().lower()
    if nombre_producto in inventario:
        del inventario[nombre_producto]
        print(f"{nombre_producto} ha sido eliminado")
    else:
        print("El producto no existe")

def ver_inventario():
    if not inventario:
        print("El inventario está vacío")
    else:
        for nombre_producto, datos in inventario.items():
            print(f"{nombre_producto} | stock: {datos['stock']} | precio: {datos['precio']:.2f}€")



while True:
    
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        añadir_producto()
    elif opcion == "2":
        actualizar_stock()
    elif opcion == "3":
        eliminar_producto()
    elif opcion == "4":
        ver_inventario()
    elif opcion == "5":
        print("Saliendo del sistema de inventario...")
        break
    else:
        print("Opción inválida. Intenta de nuevo.")



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

        nombre_modificado = nombre[0].lower() + nombre[1].lower() 
        apellido_modificado = apellido[0].upper() + apellido[1].upper() + apellido[2].upper()
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


def mostrar_menu_reserva():
    print("1. Ver habitaciones disponibles")
    print("2. Reservar habitación")
    print("3. Cancelar reserva")
    print("4. Ver reservas confirmadas")
    print("5. Salir")
    
Reservas = {101: "Free", 
            102: "Free", 
            103: "Free",
            104: "Free",
            105: "Free",
            106: "Free",
            107: "Free",
            108: "Free",
            109: "Free",
            110: "Free"
            }

import random

nombres_ficticios = ["ana", "luis", "marta", "pedro", "laura", "carlos"]
habitaciones_ocupadas = random.sample(list(Reservas.keys()), random.randint(2, 5))
for hab in habitaciones_ocupadas:
    Reservas[hab] = random.choice(nombres_ficticios)
    

def habitaciones_disponibles():
    for numero, estado in Reservas.items():
        simbolo = "🟩" if estado == "Free" else "🟥"
        print(f"{numero}: {simbolo}")

def reservar_habitacion():
    try:
        numero = int(input("Introduce el número de habitación que quieres reservar: "))
    
        if numero not in Reservas:
            raise KeyError ("La habitación no existe")
        if Reservas[numero] != "Free":
           print("La habitación ya está reservada")
        else:
            nombre = input("Introduce el nombre al que quieres hacer la reserva: ").strip().lower()
            Reservas[numero] = nombre
            print(f"la habitación {numero} se ha reservado a nombre de {nombre}.")

    except ValueError:
        print("Debes introducir un número válido.")
    except KeyError as e:
        print(f" {e}")

def cancelar_reserva():
    try:
        numero = int(input("Para cancelar introduce el numero de habitacion: "))
        if numero not in Reservas:
            raise KeyError ("La habitación no existe")
        if Reservas[numero] == "Free":
            print(f"La habitación número {numero} no está reservada")
        else:
            Reservas[numero] = "Free"
            print(f"la reserva de la habitación número {numero}, se ha cancelado")
    except ValueError:
        print("Debes inroducir un número de habitación válido")
    except KeyError as e:
        print(f" {e}")

def ver_reservas_confirmadas():
        tiene_reservas = False
        for numero, estado in Reservas.items():
            if estado != "Free":    
                print(f" {numero}: {estado}")
                tiene_reservas = True
        if not tiene_reservas:
                print("No hay ninguna habitación reservada")


while True:
    mostrar_menu_reserva()
    option = input("Introduce una opción: ")
    if option == "1":
        print("\n🟩 = Libre | 🟥 = Reservada\n")
        habitaciones_disponibles()
    elif option == "2":
         reservar_habitacion()
    elif option == "3":
        cancelar_reserva()
    elif option == "4":
        ver_reservas_confirmadas()
    elif option == "5":
        print("Salir")
        break
    else:
        print("Opción inválida: inténtalo de nuevo")

        

    
    
                





