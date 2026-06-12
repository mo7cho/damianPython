productos = {
    1: {"nombre": "leche", "precio": 1200 },
    2: {"nombre": "mani", "precio": 1600},
    3: {"nombre": "cereal", "precio": 3200}
}

def agregar():
    # Convertimos a minúsculas para mantener la consistencia con el resto de funciones
    index = int(input(""))
    key = input("¿Qué dato desea agregar?: ").strip().lower()
    value = input("Ingrese su valor: ")
    if value.isdigit():
        value = int(value)
    else:
        value = value.title()

    productos[key] = value
    print(f"\{key.title()} agregado con éxito.")

def eliminar():
    elim = input("Escriba el nombre del dato que desea eliminar: ").strip().lower()
    if elim in productos:
        del productos[elim]
        print(f"\n{elim.title()} eliminado con éxito.")
    else:
        print(f"\n{elim} no existe en el registro.")

def actualizar():
    act = input("Escriba el nombre del dato que desea actualizar: ").strip().lower()
    if act in productos:
        nuevo = input(f"Ingrese el nuevo valor para '{act.title()}': ")
        productos[act] = nuevo
        print(f"\n{act.title()} actualizado con éxito.")
    else:
        print(f"\n{act} no existe en el registro.")

def mostrar():
    print("\n=== Información de los productos ===")
    for key, value in productos.items():
        print(f"{key}.- {value["nombre"]}: ${value["precio"]}")
    print("-" * 30)

while True:
        print("""
    === Menú de Productos ===
    1.- Agregar producto
    2.- Borrar producto
    3.- Actualizar producto
    4.- Mostrar productos
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