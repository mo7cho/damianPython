indies = 0
estudio = 0
e = 0
a = 0
m = 0
juegos = []

while True:
    try:
        cantidad = int(input("Ingrese la cantidad de juegos: "))
        if cantidad > 0:
            break
        else:
            print("El número debe ser mayor a 0")
    except ValueError:
        print("El número debe ser entero")

for i in range(cantidad):
    while True:
        nombre = input(f"Ingrese el nombre del {i + 1}° juego: ").upper()

        juego = nombre.replace(" ", "")

        if len(juego) < 5:
            print("Error: el nombre del juego debe tener al menos 5 caracteres")
        else:
            juegos.append(juego)
            break

    while True:
        try:
            valor = int(input("Ingrese el precio del juego: "))
            if 20000 <= valor < 40000:
                indies += 1
                break
            elif valor >= 40000:
                estudio += 1
                break
            else:
                print("El precio no debe ser menor a 20.000")
        except ValueError:
            print("El número debe ser entero")
    
    while True:
        try:
            clas = int(input("""
1.- E para todos (<12)
2.- +12 para adolescentes (12 y 17)
3.- M para adultos (+18)
Ingrese la clasificación de edad: """))

            match clas:
                case 1:
                    e += 1
                    break
                case 2:
                    a += 1
                    break
                case 3: 
                    m += 1
                    break
                case _:
                    print("Error: elección no válida")

        except ValueError:
            print("Error: debe ingresar un número entero")

print(f"""
Hay {indies} indies, y {estudio} de estudio.
- E para todos: {e}
- +12 para adolescentes: {a}
- M para adultos: {m}
""")

print("Lista de juegos ingresados:")

for juego in juegos:
    print("- ", juego)