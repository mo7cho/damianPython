from random import randint

inf = int(input("Ingrese un límite inferior: "))
sup = int(input("Ingrese un límite superior: "))

num = randint(inf, sup)

if num % 2 != 0:
    num += 1
    if num >= sup:
        num -= 1

int1 = int(input("Intente adivinar: "))

if int1 != num:
    if int1 < num:
        print("El número es mayor.")
    elif int1 > num:
        print("El número es menor")

    int2 = int(input("Intente de nuevo: "))

    if int2 > num:
        print("El número es mayor.")
        if num < int1:
            print(f"Te daré una pista: El número que buscas está más cerca de {int2} que de {int1}")
        else:
            print(f"Te daré una pista: El número que buscas está más cerca de {int1} que de {int2}")
    elif int2 < num:
        print("El número es menor")
        if num > int1:
            print(f"Te daré una pista: El número que buscas está más cerca de {int2} que de {int1}")
        else:
            print(f"Te daré una pista: El número que buscas está más cerca de {int1} que de {int2}")
    
    if int2 != num:
        int3 = int(input("Intente una última vez: "))

        if int3 != num:
            print("Perdiste.")
            print(f"El número era: {num}")
        else:
            print("Felicitaciones, adivinó en su último intento.")
    else:
        print("Felicitaciones, adivinó en su segundo intento.")
else:
    print("Felicitaciones, adivinó en su primer intento.")

# Ejercicio corregido
from random import randint

# Ingreso de límites
inf = int(input("Ingrese un límite inferior: "))
sup = int(input("Ingrese un límite superior: "))

# Generar número aleatorio PAR
num = randint(inf, sup)

while num % 2 != 0:
    num = randint(inf, sup)

# -------------------------
# PRIMER INTENTO
# -------------------------

intento1 = int(input("Primer intento: "))

if intento1 == num:
    print("¡Felicitaciones! Adivinó en su primer intento.")

else:

    if intento1 < num:
        print("El número es mayor.")
    else:
        print("El número es menor.")

    # -------------------------
    # SEGUNDO INTENTO
    # -------------------------

    intento2 = int(input("Segundo intento: "))

    if intento2 == num:
        print("¡Felicitaciones! Adivinó en su segundo intento.")

    else:

        if intento2 < num:
            print("El número es mayor.")
        else:
            print("El número es menor.")

        # Pista de cercanía
        distancia1 = abs(num - intento1)
        distancia2 = abs(num - intento2)

        if distancia1 < distancia2:
            print(f"Pista: Estabas más cerca con {intento1}.")
        elif distancia2 < distancia1:
            print(f"Pista: Estabas más cerca con {intento2}.")
        else:
            print("Pista: Ambos intentos estuvieron igual de cerca.")

        # -------------------------
        # TERCER INTENTO
        # -------------------------

        intento3 = int(input("Último intento: "))

        if intento3 == num:
            print("¡Felicitaciones! Adivinó en su último intento.")
        else:
            print("Perdiste.")
            print(f"El número era: {num}")