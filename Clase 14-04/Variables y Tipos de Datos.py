# Variables y Tipos de Datos
variable_entera = 42 # Entero (int)
variable_decimal = 3.14 # Decimal (float)
variable_texto = "Hola, mundo!" # Cadena de texto (string)
variable_booleana = True # Valor booleano (true, false, 0-1)

# Operadores
# "resultado_suma" almacena el resultado de ambas variables
# "comparacion" almacena el resultado de comparar si "variable_entera" es mayor a "variable_decimal"
resultado_suma = variable_entera + variable_decimal
comparacion = (variable_entera > variable_decimal)

# Entrada y Salida
nombre_usuario = input("Por favor, ingresa tu nombre: ")
print("Hola, " + nombre_usuario + "! Este es tu primer programa en Python.") # Alternativa: print(f"Hola, {nombre_usuario}! Este es tu primer programa en Python.")

# Estructuras de Control de decisiones
# Se utiliza una estructura if-elif-else para tomar decisiones basadas en condiciones
if variable_booleana:
    print("La variable booleana es verdadera.")
elif resultado_suma < 10:
    print("La suma es menor que 10.")
else:
    print("Ninguna de las condiciones anteriores se cumple.")

# Colecciones de Datos
# Se crean listas, tuplas, diccionarios y conjuntos para almacenar datos
lista_numeros = [1, 2, 3, 4, 5]
# - Se puede acceder a los elementos mediante índices (ejemplo: lista_numeros[0] devuelve 1).
# - Permite agregar, eliminar y modificar elementos.
# - Para datos ordenados que pueden cambiar y permitir duplicados.

tupla_colores = ("rojo", "verde", "azul")
# - Se puede acceder a los elementos mediante índices.
# - Una vez creada, no se puede modificar.
# - Para datos ordenados que no deben cambiar (inmutables).

diccionario_edades = {"Juan": 25, "María": 30, "Carlos": 22}
# - Los elementos se acceden por claves, no por índices.
# - Las claves deben ser únicas, pero los valores pueden repetirse.
# - Para asociar claves únicas a valores, útil para búsquedas rápidas.

conjunto_elementos = {1, 2, 3, 4, 5}
# - No se puede acceder por índice y no garantiza el orden de los elementos.
# - Elimina elementos duplicados automáticamente.
# - Para almacenar elementos únicos y realizar operaciones de conjunto (sin duplicados y desordenado).

# Funciones
# Se define una función saludar() y se le utiliza para crear un mensaje de saludo personalizado
def saludar(nombre):
    return "¡Hola, " + nombre + "!"
mensaje_saludo = saludar("Estudiante")

# Manejo de Errores
try:
    resultado_division = 0 / 0
except ZeroDivisionError:
    print("¡Error! No se puede dividir por zero.")
finally:
    print("Bloque 'finally' Este código se ejecuta siempre, haya o no haya errores.")
    
# Trabajo con Archivos
with open("archivo.txt", "w") as archivo:
    archivo.write("¡Hola desde un archivo!")

# Módulos y Bibliotecas
import math
raiz_cuadrada = math.sqrt(16)
# Programación Orientada a Objetos
class MiClase:
    def __init__(self, atributo):
        self.atributo = atributo
    def mostrar_atributo(self):
        print("El valor del atributo es:", self.atributo)

# Manejo de Cadenas (Strings)
longitud_cadena = len("Python")
mayusculas = "hola".upper()
minusculas = "HOLA".lower()
reemplazo = "python es divertido".replace("divertido", "increíble")