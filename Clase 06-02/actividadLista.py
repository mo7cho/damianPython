# # Ejercicio 1
# def validar_lista_numeros():
#     while True:
        
#         entrada = input("Ingresa una lista de números separados por espacios: ")
        
#         try:
#             numeros = []

#             for elemento in entrada.split():
#                 numeros.append(int(elemento))

#             return numeros
        
#         except ValueError:
#             print("Error: Debe ingresar únicamente números enteros. Intente nuevamente.\n")

# lista_numeros = validar_lista_numeros()

# pares = []
# impares = []

# for numero in lista_numeros:
#     if numero % 2 == 0:
#         pares.append(numero)
#     else:
#         impares.append(numero)

# print(f"Números pares: {pares}")
# print(f"Números impares: {impares}")

# Ejercicio 2
# def sumar_lista(numeros):
#     total = 0
#     for numero in numeros:
#         total += numero
#     return total


# # Ejemplo de uso
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# resultado = sumar_lista(numeros)
# print(f"Suma total: {resultado}")

# Ejercicio 3
# texto = "programacion"

# frecuencia = {}

# for letra in texto:
#     frecuencia[letra] = frecuencia.get(letra, 0) + 1

# for letra, cantidad in frecuencia.items():
#     print(f"- {letra}: {cantidad}")

# Ejercicio 4
alumnos = {"Ana": 7.5, "Luis": 5.0, "Pedro": 6.0, "María": 4.5, "Carlos": 8.2}
aprobados = []

for alumno, nota in alumnos.items():
    if nota >= 6.0:
        aprobados.append(alumno)

print("Lista de alumnos aprobados:")

for aprobado in aprobados:
    print(f"- {aprobado}")