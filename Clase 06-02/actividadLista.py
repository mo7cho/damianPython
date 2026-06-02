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
def contar_letras(texto):
    conteo = {}

    for letra in texto:
        if letra.isalpha():  # Solo cuenta letras
            letra = letra.lower()  # Convierte a minúscula
            if letra in conteo:
                conteo[letra] += 1
            else:
                conteo[letra] = 1

    return conteo


# Ejemplo de uso
texto = input("Ingrese un texto: ")
resultado = contar_letras(texto)

print("\nCantidad de cada letra:")
for letra, cantidad in resultado.items():
    print(f"{letra}: {cantidad}")