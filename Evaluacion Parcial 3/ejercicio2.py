stock = 120
hist = 0
total = 0


print("¡Bienvenido al sistema de gestión de préstamos de la Biblioteca Central!")

while True:
    try:
        print("""
=== MENÚ PRINCIPAL ===
1.- Libros disponibles
2.- Realizar préstamo
3.- Devolver préstamo
4.- Historial de préstamos
5.- Salir
""")

        op = int(input("Seleccione una opción: "))

        match op:
            case 1:
                print(f"Cantidad de libros actuales: {stock}")
            
            case 2:
                while True:
                    try:
                        prest = int(input("Ingrese la cantidad de libros a prestar: "))
                        if prest < stock and prest > 0:
                            stock -= prest
                            hist += 1
                            total += 1
                            break
                        else:
                            print(f"La cantidad de libros debe ser mayor a 0 y no sobrepasar el stock de libros ({stock})")
                    except ValueError:
                        print("Error, tipo de dato inválido")
            
            case 3:
                while True:
                    try:
                        if hist <= 0:
                            print("Debes tener préstamos activos.")
                            break

                        else:
                            devol = int(input("Ingrese la cantidad de libros para devolver: "))

                            if devol > 0:
                                stock += devol
                                if stock > 120:
                                    print("No se puede superar la capacidad máxima de la biblioteca (120)")
                                    stock -= devol
                                else:
                                    hist -= 1
                                    break
                            else:
                                print("El número debe ser mayor a 0")
                    
                    except ValueError:
                        print("Error, tipo de dato inválido")
            
            case 4:
                print(f"Historial de prestamos activos de la sesión: {hist}")
                print(f"Historial de prestamos totales de la sesión: {total}")

            case 5:
                print("Gracias por utilizar nuestro software, hasta la próxima.")
                break

            case _:
                print("Error, selección inválida")

    except Exception as e:
        print(f"Error: {e}")