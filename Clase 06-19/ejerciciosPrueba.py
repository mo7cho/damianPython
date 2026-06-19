pacientes = [
    {"nombre": "Aquiles Baeza", "prevision": "Fonasa",
     "temperatura": 39.6, "grave": True}, # 0
    {"nombre": "dON rAMON Baeza", "prevision": "Fodesa",
     "temperatura": 34.6, "grave": False}, # 1
    {"nombre": "Señor Barriga", "prevision": "Fonasa",
     "temperatura": 35.6, "grave": False}, # 2
]

def mostrarPacientes():
    if len(pacientes) == 0:
        print("No hay pacientes.")

    for d, p in enumerate(pacientes, 1):
        print(f"{d}.- Nombre: {p["nombre"]} | Prevision: {p["prevision"]} | Temperatura: {p["temperatura"]} | Gravedad: {p["grave"]}")

def ingresarPaciente():
    while True:
        try:
            nombre = input("Ingrese el nombre del paciente: ")

            if len(nombre) == 0:
                print("Error: El campo no puede estar vacío")
            elif len(nombre.strip()) < 9:
                print("Error: El nombre debe contener más 8 caracteres.")
            else:
                while True:
                    try:
                        sel = int(input("1.- Fonasa | 2.- Isapre | 3.- Fodesa: \nIngrese la previsión del paciente: "))

                        match sel:
                            case 1:
                                prevision = "Fonasa"
                                break
                            case 2:
                                prevision = "Isapre"
                                break
                            case 3:
                                prevision = "Fodesa"
                                break
                            case _:
                                print("Ingrese una opcion valida.")

                    except ValueError:
                        print("Error: Debe ingresar un número entero.")

                while True:
                    try:
                        temperatura = float(input("Ingrese la temperatura del paciente:\n"))
                        break

                    except ValueError:
                        print("Error: Debe ingresar un número.")


                pacientes.append({
                    "nombre": nombre, "prevision": prevision,
                "temperatura": temperatura, "grave": validarEstado(temperatura)
                })

                print("Se agregó un nuevo paciente.")
                break

        except ValueError:
            print("Error: El dato ingresado no es válido.")

def quitarPaciente():
    try:
        mostrarPacientes()

        eliminar = int(input("¿Qué paciente quiere borrar? "))

        pacientes.pop(eliminar - 1)
        print("Se ha quitado al paciente")

    except ValueError:
        print("Error: Elija una opción numérica.")

def tomarTemperatura():
    select = int(input("Ingrese al paciente que le tomará la temperatura: "))
    reg = float(input("Ingrese la temperatura del paciente: "))

    pacientes[select - 1]["temperatura"] = reg
    pacientes[select - 1]["grave"] = validarEstado(reg)

def cobrarAtencion():
    eli = int(input("¿Qué paciente va a pagar?: "))
    prev = pacientes[eli - 1]["prevision"]
    if prev == "Fonasa":
        total = 25000 * 0.46
    elif prev == "Isapre":
        total = 25000 * 0.73
    elif prev == "Fonasa":
        total = 25000 * 0.875

    print(f"El total a pagar es ${total}")

def validarEstado(t):
    if t > 39:
        return True
    else:
        return False

def menuPacientes():
    while True:
        print("""
1.- Ingresar paciente
2.- Quitar paciente
3.- Tomar temperatura
4.- Cobrar atención
5.- Mostrar pacientes
9.- Salir
    """)
        print("="*100)

        op=int(input("Seleccione una opcion: "))

        match op:
            case 1:
                ingresarPaciente()

            case 2:
                quitarPaciente()

            case 3:
                mostrarPacientes()
                tomarTemperatura()

            case 4:
                mostrarPacientes()

            case 5:
                mostrarPacientes()

            case 9:
                print("¡Hasta pronto!")
                break  

            case _:
                print("Ingrese una opcion valida.")

menuPacientes()