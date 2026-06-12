alumno = {
    "nombre": "Wanda Maximoff",
    "carrera": "Informatica",
    "edad": 24
}

def agregar():
    # Convertimos a minúsculas para mantener la consistencia con el resto de funciones
    key = input("¿Qué dato desea agregar?: ").strip().lower()
    value = input("Ingrese su valor: ")
    if value.isdigit():
        value = int(value)
    else:
        value = value.title()

    alumno[key] = value
    print(f"\{key.title()} agregado con éxito.")

def eliminar():
    elim = input("Escriba el nombre del dato que desea eliminar: ").strip().lower()
    if elim in alumno:
        del alumno[elim]
        print(f"\n{elim.title()} eliminado con éxito.")
    else:
        print(f"\n{elim} no existe en el registro.")

def actualizar():
    act = input("Escriba el nombre del dato que desea actualizar: ").strip().lower()
    if act in alumno:
        nuevo = input(f"Ingrese el nuevo valor para '{act.title()}': ")
        alumno[act] = nuevo
        print(f"\n{act.title()} actualizado con éxito.")
    else:
        print(f"\n{act} no existe en el registro.")

def mostrar():
    print("\n=== Información del Alumno ===")
    for i, (key, value) in enumerate(alumno.items(), 1):
        print(f"{i}.- {key.title()}: {value}")
    print("-" * 30)

def menuAlumno():
    while True:
        print("""
    === Menú de Alumnos ===
    1.- Agregar dato
    2.- Borrar dato
    3.- Actualizar dato
    4.- Mostrar datos
    5.- Salir
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
                    print("Opción inválida. Elige un número del 1 al 5.")

        except ValueError:
            print("Error: Por favor, ingrese un número entero válido.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")