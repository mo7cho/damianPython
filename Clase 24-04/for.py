# Explicación y uso de "for"

# for i in range(5):
#     print(i+1)

# num = int(input("Ingrese un número: "))
# for i in range(num):
#     print(f"Repetición {i + 1}")

# Pedir un numero al usuario y mostrar
# su tabla ed multiplicar

# num = int(input("Ingrese un número para multiplicar: "))
# print (f"Tabla de multiplicar del {num}")
# for i in range(1, 12 + 1):
#     print(f"{num} x {i} = {num * (i)}")

c = int(input("Ingrese una cantidad de notas: "))
sum = 0
for i in range(c):
    n = float(input(f"Ingrese la {i + 1}° nota: "))
    sum = sum + n
prom = sum/c
print(f"El promedio del alumno es {round(prom, 1)}")
if prom > 40:
    print("El alumno aprobó")
else:
    print("El alumno reprobó")