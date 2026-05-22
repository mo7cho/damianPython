# Las excepciones más comunes son:
# 1. Divisiones por cero (10/0). -> ZeroDivisionError
# 2. Tipos de datos incorrectos (Aparece cuando intentas concatenar una cadena con un número). -> TypeError
# 3. Error de valores (Se genera cuando hay un problema con el tipo o valor de los
# datos que estás manipulando, como convertir una cadena no numérica a un número). - > ValueError
# 4. Archivos no encontrados (Dar ubicaciones de archivo no existentes). -> FileNotFoundError
# 5. Error de sintaxis (Se genera cuando hay un error de sintaxis en tu código). -> SyntaxError# Usos y ejemplos del try

# Primer ejercicio
# while True:
#     try:
#         num = int(input("Ingrese un número"))
#         break
#     except:
#         print("El numero debe ser entero")

# Segundo ejercicio
# code = 6767

# while True:
#     try:
#         passw = int(input("Ingrese su clave: "))
#         if code == passw:
#             print("Ingreso correcto")
#             break
#         else:
#             print("Clave inválida")
#     except ValueError as er:
#         print("Sólo números enteros")
#         print(er)

# Tercer ejercicio
# op=0
# total=0

# while op!=4:
#     try:
#         print("1.- PC $500.000")
#         print("2.- LGTV 55 pulgadas $450.000")
#         print("3.- Microondas Mademsa $100.000")
#         print("4.- Salir")

#         op = int(input("Seleccione una opción: "))

#         match op:
#             case 1:
#                 print(f"El total a pagar es {total:,.0f}")
#                 total+=500000*1.19
#             case 2:
#                 print(f"El total a pagar es {total:,.0f}")
#                 total+=450000*1.19
#             case 3:
#                 print(f"El total a pagar es {total:,.0f}")
#                 total+=100000*1.19
#             case 4:
#                 print("Saliendo")
#                 print(f"El total a pagar es {total:,.0f}")
#             case _:
#                 print("Opción inválida")

#     except ValueError as er:
#         print("Error, sólo números enteros.")

# Cuarto ejercicio
while True:
    try:
        num = int(input("Ingrese la cantidad de pasajes a vender: "))
        break
    except ValueError:
        print("El numero debe ser entero.")

totalIngresos = 0
for i in range(num):
    while True:
        try:
            precio = int(input(f"Ingrese el valor del {i + 1}° pasaje: "))
            totalIngresos += precio
            break
        except ValueError as e:
            print("Necesitas números enteros.")
            print(f"Error: {e}")
print(f"El precio total a pagar es ${totalIngresos}")

# Quinto ejercicio
bultos = int(input("Ingresa la cantidad de bultos: "))
valLiv = 0
cantLiv = 0
valNor = 0
cantNor = 0
total = 0

for i in range(bultos):
    peso = float(input(f"Ingresa el peso del {bultos}° bulto (1 - 10kg): "))
    if peso > 0:
        valLiv += 1000
        cantLiv += 1
    elif peso >= 6:
        valNor += 2000
        cantNor += 1
    else:
        print("Peso ingresado incorrecto (1-10kg)")

total += valLiv + valNor

print(f"{cantLiv} bultos livianos ${valLiv}")
print(f"{cantNor} bultos livianos ${valNor}")
print(f"Valor total a pagar: {total}")