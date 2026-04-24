# print("Ingrese su nombre")
# nombre = input()    # string / str
# edad = int(input("Ingrese su edad: "))  # integer / int

# print("Hola", nombre, "su edad en 5 años será", edad + 5)

# titulo = "Clima de hoy"
# diaDelMes = 17
# mes = 4
# tem = 25.7    # float (decimal)
# llueve = False    # boolean (true/false)
# print(titulo, "temperatura:", tem, diaDelMes, mes, "/", mes)
# print(f"{titulo} temperatura: {tem} {diaDelMes}/{mes}")

# Mostrar la suma de 2 números ingresados
# por el usuario, mostrar también la resta

# n1 = int(input("Ingrese el primer número: "))
# n2 = int(input("Ingrese el segundo número: "))
# print(f"La suma de ambos números es {n1 + n2}")
# print(f"La resta de ambos números es {n1- n2}")

# Pedir al usuario 3 números y mostrar su promedio
# n1 = float(input("Ingrese la primera nota: "))
# n2 = float(input("Ingrese la segunda nota: "))
# n3 = float(input("Ingrese la tercera nota: "))
# prom = (n1 + n2 + +n3) / 3
# print(f"La promedio de las 3 notas es {round(prom, 1)}") # Redondea la nota, dependiendo de cuantos decimales necesites

# if prom >= 4:
#     print("El alumno aprobó")
# else:
#     print("El alumno reprobó")

print('''
1.- Cereal 2000
2.- Lechuga 1808
3.- Leche 1000
Seleccione su producto:''')
sel = int(input())
if sel == 1:
    print("El valor a pagar es", 2000*1.19)
elif sel == 2:
    print("El valor a pagar es", 1800*1.19)
elif sel == 3:
    print("El valor a pagar es", 1000*1.19)
else:
    print("Opción inválida")