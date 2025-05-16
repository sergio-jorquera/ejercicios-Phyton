# 🧪 Fundamentos Python III – Funciones

# ------------------------------
# ✨ Ejercicio 1: Saludo básico
# Objetivo: Aprender a definir y llamar funciones
# Crea una función llamada saludar() que imprima: "¡Hola, bienvenido/a!"
# Luego llama a la función una vez para comprobar que funciona.

def saludar():
    print("Hola, bienvenido/a")

saludar()


# ------------------------------
# ✨ Ejercicio 2: Saludo personalizado
# Objetivo: Trabajar con parámetros
# Crea una función llamada saludar_persona(nombre) que imprima: "Hola, [nombre]!"
# Llama a la función dos veces con diferentes nombres.

def saludar_persona(nombre):
    print(f"Hola, {nombre}")
saludar_persona("Felipe")
saludar_persona("Andrea")



# ------------------------------
# ✨ Ejercicio 3: Suma fácil
# Objetivo: Usar parámetros y return
# Crea una función llamada sumar(a, b) que devuelva la suma de dos números.
# Guarda el resultado en una variable y muéstralo con print().

def sumar(a, b):
    return a + b
resultado = sumar(5, 3)
print(f"El resultado es {resultado}")


# ------------------------------
# ✨ Ejercicio 4: ¿Par o impar?
# Objetivo: Usar lógica dentro de una función
# Escribe una función es_par(numero) que devuelva True si el número es par y False si es impar.
# Pruébala con varios números y muestra el resultado.

def es_par(numero):
    if numero % 2 ==0:
        print(f"El número{numero}, es par.")
    else:
        print(f"El número {numero}, es impar.")
es_par(7)
es_par(16)

# ------------------------------
# ✨ Ejercicio 5: Mensaje con formato
# Objetivo: Devolver una cadena con formato
# Crea una función llamada mensaje(nombre, edad) que devuelva una frase como:
# "Me llamo Marta y tengo 30 años."
# Usa return y luego muestra el mensaje con print().

def mensaje(nombre, edad):
    return f"Me llamo {nombre} y tengo {edad} años."
resultado = mensaje("Marta", 30)

print(resultado)

# ------------------------------
# ✨ Ejercicio 6: Calculadora simple
# Objetivo: Practicar varias funciones juntas
# Crea 4 funciones: sumar(a, b), restar(a, b), multiplicar(a, b), dividir(a, b)
# Llama a cada una con un par de números y muestra los resultados.
# Bonus: en dividir(), si el segundo número es 0, devuelve "No se puede dividir por cero"

def sumar(a,b):
 return a + b
def restar(a, b):
    return a - b
def multiplicar(a, b):
    return a * b
def dividir(a, b):
    if b == 0:
       return "No se puede dividir por 0"
    else:
        return (a / b)
    
print(f"Suma = {sumar(3,5)}")
print(f"Resta = {restar(3,5)}")
print(f"Multiplicación = {multiplicar(3,5)}")
print(f"División = {dividir(3,0)}")

# ------------------------------
# ✨ Ejercicio 7: Edad en el futuro
# Objetivo: Usar return con operaciones
# Escribe una función llamada edad_futura(edad_actual, años) que calcule la edad que tendrás después de X años.

def edad_futura(edad_actual, años):
    edad = edad_actual + años
    return edad 
mi_edad_futura = edad_futura(43, 26)
print(f" Tu edad dentro de 26 años será {mi_edad_futura}.")
    

# ------------------------------
# ✨ Ejercicio 8: Media de 3 números
# Objetivo: Trabajar con números y return
# Crea una función llamada calcular_media(a, b, c) que devuelva la media de tres números.
# Prueba la función y muestra el resultado con print().

def calcular_media(a, b, c):
     return  (a + b + c) / 3
    
a = 10
b = 15
c = 20
media = calcular_media(a, b, c)
print(f"la media de los tres números es {media}")



# ------------------------------
# ✨ Ejercicio 9: Mostrar menú (sin lógica)
# Objetivo: Separar la presentación de la lógica
# Escribe una función llamada mostrar_menu() que imprima un pequeño menú como:
# 1. Ver perfil
# 2. Editar perfil
# 3. Cerrar sesión

def mostrar_menu():
    print ("1. Ver perfil")
    print ("2. Editar perfil")
    print ("3. Cerrar sesión")
mostrar_menu()

# ------------------------------
# 🌟 Reto Final: Generador de contraseñas

# Crea una función llamada generar_contraseña(longitud)
# que devuelva una contraseña aleatoria con la longitud especificada.

# La contraseña debe contener una mezcla de:
# - letras minúsculas (a-z)
# - letras mayúsculas (A-Z)
# - números (0-9)
# - símbolos como !, @, #, $, %, &, *

# Ejemplo de uso:
# contraseña = generar_contraseña(12)
# print(contraseña)  # -> A2c$e9#Tq&7L

# Bonus:
# - Usa la librería random
# - Controla que la longitud mínima sea 8 caracteres
# - Añade un mensaje de advertencia si se pide menos de 8

import random

def generar_contraseña(longitud):
    if longitud < 8:
        print("⚠️ Advertencia: La longitud mínima recomendada es de 8 caracteres.")
        return None

    letras_mayus = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letras_minus = "abcdefghijklmnopqrstuvwxyz"
    numeros = "0123456789"
    simbolos = "!@#$%&*"

    caracteres = letras_mayus + letras_minus + numeros + simbolos

    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

contraseña = generar_contraseña(12)
if contraseña:
    print("Contraseña generada:", contraseña)


