cantidad = int(input("Ingrese la cantidad de números a identificar: "))
for i in range(1, cantidad + 1):  # Alternativa: for i in range(cantidad):
    num = int(input(f"Ingrese el {i}° número: "))  # Alternativa: num = int(input(f"Ingrese el {i + 1}° número: "))
    if num % 2 == 0:
        print(f"El número {num} es par")
    else:
        print(f"El número {num} es impar")