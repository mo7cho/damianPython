# nombres = ["Amaro", "Carlos", "Yoni"]
# apellidos = ["Castillos", "Vargas", "Alvarez"]

# print(nombres)

# print(nombres[0], apellidos[0])

# for n in range(len(nombres)):
#     print(nombres[n], apellidos[n])

# frutas = ["Manzana", "Plátano", "Durazno", "Pera", "Uva"]

# print("Lista de frutas:")
# for f in frutas:
#     print(f"- {f}")

# n = input("Agregue una nueva fruta: ").capitalize()

# frutas.append(n)

# print("Nueva lista de frutas:")
# for f in frutas:
#     print(f"- {f}")

# for f in frutas:
#     if f.endswith("a"):
#         print(f"- {f} termina con a")
#     else:
#         print(f"- {f} NO termina con a")

    # Alternativa:

    # if f[-1].lower() == "a":
    #     print(f"- {f} termina con a")
    # else:
    #     print(f"- {f} NO termina con a")

# vocales = "aeiou"

# for f in frutas:
#     if f[0].lower() in vocales:
#         print(f"La fruta {f} comienza con vocal")
#     else:
#         print(f"La fruta {f} NO comienza con vocal")

juguetes = ["yo-yo", "tetris"]

def agregar():
    agr = input("¿Qué juguete desea agregar?: ")
    juguetes.append(agr)

def eliminar():
    elim = int(input("¿Qué juguete desea eliminar?: "))
    juguetes.pop(elim - 1)

def actualizar():
    act = int(input("¿Qué juguete desea actualizar?: "))
    nuevo = input("Ingrese el nuevo nombre: ")
    juguetes[act - 1] = nuevo 

def mostrar():
    list = 1

    for j in juguetes:
        print(f"{list}.- {j.capitalize()}")
        list += 1

while True:

    print("""
=== MENÚ PRINCIPAL ===
1. Agregar Juguete
2. Eliminar Juguete
3. Actualizar Juguete
4. Mostrar Juguetes
5. Salir
""")

    try:
        op = int(input("Seleccione una opción: "))

        match op:

            case 1:
                agregar()

            case 2:
                mostrar()
                eliminar()
                    
            case 3:
                mostrar()
                actualizar()

            case 4:
                mostrar()

            case 5:
                print("Gracias por utilizar nuestro software, hasta la próxima.")
                break

            case _:
                print("Opción inválida.")

    except Exception as e:
        print(f"Error: {e}")