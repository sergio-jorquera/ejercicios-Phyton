# 🧪 Fundamentos Python I – Enunciados

# ------------------------------
# TIPOS DE DATOS
# ------------------------------

# ✨ Ejercicio 1: ¿Qué tipo es?
# Declara las siguientes variables y usa type() para imprimir qué tipo de dato es cada una:
# a = "Hola"
# b = 25
# c = 3.14
# d = True
# e = None

# Declaración de variables
a = "Hola"
b = 25
c = 3.14
d = True
e = None

# Imprimir el tipo de cada variable
print("El tipo de a es:", type(a))  
print("El tipo de b es:", type(b)) 
print("El tipo de c es:", type(c))  
print("El tipo de d es:", type(d))  
print("El tipo de e es:", type(e)) 



# ✨ Ejercicio 2: Conversión rápida
# Convierte la cadena "42" en número, súmale 8 y muestra el resultado.
# Luego convierte el número 100 en texto y muestra la frase:
# "Tu puntuación final es: 100"
# Parte 1: Convertir cadena "42" en número, sumar 8

cadena = "42"
numero = int(cadena)  # Convertimos de str a int
resultado = numero + 8
print("El resultado es:", resultado)  # Muestra: 50

# Parte 2: Convertir número 100 en texto y mostrar mensaje
puntaje = 100
mensaje = "Tu puntuación final es: " + str(puntaje)  # Convertimos int a str
print(mensaje)

# ------------------------------
# VARIABLES
# ------------------------------

# ✨ Ejercicio 3: Nombres y saludos
# Crea una variable nombre y una variable edad.
# Imprime una frase como:
# Hola, me llamo X y tengo Y años.

nombre = "Marta"
edad = 30
print(f"Hola, me llamo {nombre} y tengo {edad} años")


# ✨ Ejercicio 4: Intercambio simple
# Tienes dos variables:
# x = "gato"
# y = "perro"
# Intercambia sus valores para que x valga "perro" y y valga "gato".

x = "gato"
y = "perro"
x, y = y, x
print("x: " + x)
print("y: " + y)

# ------------------------------
# OPERADORES
# ------------------------------

# ✨ Ejercicio 5: Suma de la compra
# Declara tres precios:
# pan = 1.50
# leche = 1.24
# huevos = 2.70
# Calcula el total y muestra: “El total de tu compra es de: 4,25€”

pan = 1.20
leche = 0.95
huevos = 2.10
total = pan + leche + huevos
print(f"El total de tu compra es: {total}")

# ✨ Ejercicio 6: ¿Par o impar?
# Pide al usuario un número con input() y di si es par o impar.


numero = int(input("Introduce un número: ")) #también se podria hacer en dos pasos "entrada=input("introduce un numero")" y luego cambiar entrada a "numero=int(entrada)" 
if(numero % 2 == 0):
    print(f"El número {numero} es par")
else:
    print(f"el número {numero} es impar")


# ------------------------------
# ESTRUCTURAS DE CONTROL
# ------------------------------

# ✨ Ejercicio 7: ¿Mayor de edad?
# Pide la edad al usuario. Si tiene 18 o más, muestra “Puedes entrar”.
# Si no, muestra “Acceso denegado”.


edad = int(input("introduce tu edad: "))
if(edad >= 18):
    print("puedes entrar")
else:
    print("Acceso denegado")

# ✨ Ejercicio 8: Elige una opción
# Pide al usuario que elija una opción:
# 1. Ver perfil
# 2. Editar perfil
# 3. Cerrar sesión
# Y muestra un mensaje distinto para cada caso.

def menu():
    print("Elige una opción")
    print("1- Ver perfil")
    print("2- Editar perfil")
    print("3- Cerrar sesión")
    
    opcion = input("Elige el número de tu elección: ")
    if opcion == "1":
     print("Aquí está su perfil")
    elif opcion == "2":
        print("Edite su perfil")
    elif opcion =="3":
        print("cierre de sesión")
    else:
        print("opción no valida")

menu()


# ------------------------------
# EXTRA: TIPOS + CONDICIONAL
# ------------------------------

# ✨ Ejercicio 9: Detector de tipos raros
# Pide al usuario que escriba cualquier cosa.
# Muestra:
# - Si es un número entero: “Has escrito un número entero”
# - Si es un número decimal: “Has escrito un número decimal”
# - Si es un texto: “Parece que es una cadena de texto”
# - Si no puedes adivinar el tipo: “No sé qué es esto 😵‍💫”
# Usa try/except para intentar convertir a int() o float().

mensaje = input("escribe lo que te apetezca: ")

try:
    int(mensaje)
    print("Has escrito un número entero")
except ValueError:
    try:
        float(mensaje)
        print("Has escrito un número decimal")
    except ValueError:
        if mensaje.strip() != "":
            print("Parece que es una cadena de texto")
        else:
            print("No sé qué es esto")

# ------------------------------
# OPERADORES + CONDICIONALES + VARIABLES
# ------------------------------

# ✨ Ejercicio 10: Calculadora con menú
# Pide dos números y muestra este menú:
# 1. Sumar
# 2. Restar
# 3. Multiplicar
# 4. Dividir
# Según la opción elegida, haz la operación y muestra el resultado.
# Bonus: si elige dividir y el segundo número es 0, muestra “No se puede dividir por cero”.

a = float(input("Introduce el primer número: "))
b = float(input("Introduce el segundo número: "))

print("1-Sumar")
print("2-Restar")
print("3-Multiplicar")
print("4-Dividir")
    
operacion = input("Introduce una operación: Suma 1 / Resta 2 / Multiplicación 3 / División 4: ")
if operacion == "1":
    print(f"el resultado de la suma es {a + b}: ")
elif operacion == "2":
    print(f"el resultado de la resta es {a - b}: ")
elif operacion == "3":
    print(f"El resultado de la multiplicación es: {a * b}")
elif operacion == "4":
    if b == 0:
        print("No se puede dividir por cero")
    else:
        print(f"El resultado de la división es: {a / b}")
else:
    print("Opción no válida")

# ------------------------------
# ESTRUCTURA DE CONTROL CON RANGOS
# ------------------------------

# ✨ Ejercicio 11: Clasificador de edad
# Pide al usuario su edad y clasifícalo:
# - Menor de 3: “Bebé”
# - Entre 3 y 12: “Infancia”
# - Entre 13 y 17: “Adolescencia”
# - Entre 18 y 64: “Adulto”
# - 100 o más: “Senior”

edad = int(input("Introduce tu edad: "))

if edad < 3:
    print("Eres un bebé")
elif 3 <=edad <= 12:
    print("Estás en la infancia")
elif 13 <= edad <= 17:
    print("Eres un adolescente")
elif 17 <= edad < 64:
    print("Eres adulto")
elif edad >= 100:
    print("Eres senior")
else:
    print("Edad no válida")