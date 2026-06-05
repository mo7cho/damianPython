# ¡ACLARACIÓN! No estoy seguro si lo llegamos a usar en clases, pero agregar obj a las listas con ".append" lo conozco desde antes.
# Así tambien el listar con "for x in y", que agarra un objeto de la lista e imprime el siguiente por cada iteracion.

sen = []
jun = []

while True:
    try:
        c = int(input("Ingrese la cantidad de médicos que desea registrar: "))
        if c > 0:
            break
        else:
            print("¡Registro médico inválido! Ingrese un entero positivo para continuar.")
    except ValueError:
        print("Error, tipo de dato inválido.")


for i in range(c):
    while True:
        med = input(f"Ingrese el nombre del {i + 1}° profesional: ").replace(" ", "")
        if len(med) >= 6:
            break
        else:
            print("El nombre debe tener al menos 6 caracteres.")

    while True:
        try:
            exp = int(input("Ingrese los años de experiencia del médico: "))
            if exp > 0:
                break
            else:
                print("¡Error clínico! Ingrese un número entero positivo para la experiencia.")
        except ValueError:
            print("Error, tipo de dato inválido")

    if exp > 5:
        sen.append(med)
    else:
        jun.append(med)

print(f"\n¡El hospital cuenta con {len(sen)} Especialista(s) Senior y {len(jun)} Residente(s) Junior!\n¡Sistema listo para operar!")

print("\nLista de médicos Senior:")
for med in sen:
    print(f"- {med}")

print("\nLista de médicos Junior:")
for med in jun:
    print(f"- {med}")

# Ejercicio corregido
sen = 0
jun = 0

while True:
    try:
        c = int(input("Ingrese la cantidad de médicos que desea registrar: "))
        if c > 0:
            break
        else:
            print("¡Registro médico inválido! Ingresa un entero positivo para continuar.")
    except ValueError:
        print("¡Registro médico inválido! Ingresa un entero positivo para continuar.")

for i in range(c):

    while True:
        med = input(f"Ingrese el nombre del {i + 1}° profesional: ")

        if len(med) >= 6 and " " not in med:
            break
        else:
            print("El nombre debe tener al menos 6 caracteres y no contener espacios.")

    while True:
        try:
            exp = int(input("Ingrese los años de experiencia del médico: "))

            if exp > 0:
                break
            else:
                print("¡Error clínico! Ingresa un número entero positivo para la experiencia.")

        except ValueError:
            print("¡Error clínico! Ingresa un número entero positivo para la experiencia.")

    if exp > 5:
        sen += 1
    else:
        jun += 1

print(f"\n¡El hospital cuenta con {sen} Especialistas Senior y {jun} Residentes Junior!")
print("¡Sistema listo para operar!")