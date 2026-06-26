# ==========================================
# 1. MÓDULO DE VALIDACIONES
# ==========================================

def validar_texto(texto):
    # Primero nos aseguramos de que el dato se trate como un texto (string)
    texto_str = str(texto) 
    
    # Ahora aplicamos la misma lógica sin miedo a que el programa se caiga
    if texto_str and texto_str.strip():
        return True
    return False

def validar_año(anio):
    # Condición: El año debe ser un número entero estrictamente mayor que cero.
    if anio > 0:
        return True # Retorna True si cumple la condición.
    return False # Retorna False si es cero o un número negativo.

def validar_ranking(ranking):
    # Condición: El ranking (decimal) debe estar contenido entre 1.0 y 7.0 inclusive.
    if 1.0 <= ranking <= 7.0:
        return True # Retorna True si se encuentra dentro del rango permitido.
    return False # Retorna False si está fuera de los límites.


# ==========================================
# 2. MÓDULO DE INTERFAZ Y MENÚ PRINCIPAL
# ==========================================

def mostrar_menu():
    # Esta función no recibe parámetros y solo imprime las opciones en pantalla.
    print("\n" + "="*30)
    print("      MENÚ DE AUTOMÓVILES")
    print("="*30)
    print("1. Agregar automóvil")
    print("2. Buscar automóvil")
    print("3. Eliminar automóvil")
    print("4. Actualizar estado automóvil")
    print("5. Mostrar automóviles")
    print("6. Salir")
    print("="*30)

def leer_opcion():
    # Intentamos capturar la opción del usuario controlando posibles errores de tipeo.
    try:
        # Convertimos la entrada directamente a un número entero.
        opcion = int(input("Seleccione una opción (1-6): "))
        # Verificamos si el número ingresado pertenece a las opciones del menú.
        if 1 <= opcion <= 6:
            return opcion # Retorna el número si es totalmente válido.
        else:
            print("Error: Opción fuera de rango (debe ser de 1 a 6).")
            return -1 # Retorna -1 indicando un error de rango.
    except ValueError:
        # Se ejecuta si el usuario introduce letras en lugar de números.
        print("Error: Por favor, ingrese un número entero válido.")
        return -1 # Retorna -1 indicando un error de tipo de dato.


# ==========================================
# 3. MÓDULO DE REGISTRO DE AUTOMÓVILES
# ==========================================

def agregar_automovil(lista_autos):
    # 1. SOLICITAR Y VALIDAR MARCA
    marca = input("Ingrese la marca del automóvil: ")
    if not validar_texto(marca):
        print("Error de validación: La marca no puede estar vacía.")
        input("Presione Enter para continuar...")
        return # Detiene la función aquí si está mal

    # 2. SOLICITAR Y VALIDAR MODELO
    modelo = input("Ingrese el modelo del automóvil: ")
    if not validar_texto(modelo):
        print("Error de validación: El modelo no puede estar vacío.")
        input("Presione Enter para continuar...")
        return # Detiene la función aquí si está mal
    
    # 3. SOLICITAR Y VALIDAR AÑO
    try:
        anio = int(input("Ingrese el año del automóvil: "))
    except ValueError:
        print("Error: El año debe ser un número entero válido.")
        input("Presione Enter para continuar...")
        return
        
    if not validar_año(anio):
        print("Error de validación: El año debe ser un valor mayor a 0.")
        input("Presione Enter para continuar...")
        return 

    # 4. SOLICITAR Y VALIDAR RANKING
    try:
        ranking = float(input("Ingrese el ranking del automóvil (1.0 a 7.0): "))
    except ValueError:
        print("Error: El ranking debe ser un número decimal válido.")
        input("Presione Enter para continuar...")
        return

    if not validar_ranking(ranking):
        print("Error de validación: El ranking debe estar entre 1.0 y 7.0.")
        input("Presione Enter para continuar...")
        return 

    # 5. REGISTRO (Si todos los pasos anteriores fueron exitosos)
    nuevo_auto = {
        "marca": marca,
        "modelo": modelo,
        "anio": anio,
        "ranking": ranking,
        "recomendado": False 
    }
    
    lista_autos.append(nuevo_auto)
    print(f"\n¡Éxito! El automóvil '{marca} {modelo}' ha sido registrado correctamente.")
    input("Presione Enter para continuar...")

# ==========================================
# 4. MÓDULO DE BÚSQUEDA Y ELIMINACIÓN
# ==========================================

def buscar_automovil(lista_autos, modelo_buscado):
    # Usamos un ciclo basado en índices (posiciones numéricas) para recorrer la lista de autos.
    for i in range(len(lista_autos)):
        # Accedemos al diccionario en la posición 'i' y extraemos el valor de la clave 'modelo'.
        # Usamos .lower() en ambos lados para que la búsqueda no falle por mayúsculas/minúsculas.
        if lista_autos[i]["modelo"].lower() == modelo_buscado.lower():
            return i # Si hay coincidencia exacta, devolvemos el índice actual.
    return -1 # Si termina el ciclo y no encontró nada, devolvemos -1.

def eliminar_automovil(lista_autos):
    # Solicitamos el nombre del modelo que se desea remover del inventario.
    modelo_a_eliminar = input("Ingrese el modelo del automóvil que desea eliminar: ")
    
    # Invocamos a la función de búsqueda para obtener el índice o el código -1.
    posicion = buscar_automovil(lista_autos, modelo_a_eliminar)
    
    # Evaluamos el resultado de la búsqueda.
    if posicion != -1:
        # Si la posición es válida, extraemos y removemos el elemento con la función pop().
        auto_removido = lista_autos.pop(posicion)
        # Confirmamos al usuario mostrando los datos del auto que acabamos de borrar.
        print(f"El automóvil '{auto_removido['marca']} {auto_removido['modelo']}' fue eliminado con éxito.")
    else:
        # Mensaje de error obligatorio si el índice devuelto fue -1.
        print(f"El automóvil '{modelo_a_eliminar}' no se encuentra registrado.")


# ==========================================
# FUNCIONES AUXILIARES (Para completar el Menú)
# ==========================================

def mostrar_lista_automoviles(lista_autos):
    # Función de utilidad para ver el estado actual de nuestra lista de diccionarios.
    if not lista_autos:
        print("El inventario está vacío actualmente.")
        return
    print("\n--- INVENTARIO DE AUTOMÓVILES ---")
    for idx, auto in enumerate(lista_autos, start=1):
        print(f"{idx}. {auto['marca']} {auto['modelo']} ({auto['anio']}) - Ranking: {auto['ranking']} | Recomendado: {auto['recomendado']}")


# ==========================================
# 5. CICLO PRINCIPAL DE EJECUCIÓN
# ==========================================

def iniciar_programa():
    # Inicializamos la lista que contendrá todos nuestros autos. Vivirá durante toda la ejecución.
    inventario_global = []
    
    # Iniciamos un bucle infinito que controlará la interacción continua.
    while True:
        mostrar_menu() # Desplegamos visualmente el menú.
        opcion_elegida = leer_opcion() # Solicitamos y validamos la opción.
        
        # Evaluamos qué acción ejecutar según la opción obtenida.
        if opcion_elegida == 1:
            agregar_automovil(inventario_global) # Llama al módulo de registro.
        elif opcion_elegida == 2:
            modelo_buscar = input("Ingrese el modelo a buscar: ")
            resultado = buscar_automovil(inventario_global, modelo_buscar)
            if resultado != -1:
                print(f"Automóvil encontrado en el índice {resultado}: {inventario_global[resultado]}")
            else:
                print(f"El automóvil '{modelo_buscar}' no está registrado.")
        elif opcion_elegida == 3:
            eliminar_automovil(inventario_global) # Llama al módulo de eliminación.
        elif opcion_elegida == 4:
            print("Aviso: La opción 'Actualizar estado' no está requerida en la guía lógica actual.")
        elif opcion_elegida == 5:
            mostrar_lista_automoviles(inventario_global) # Muestra los autos en pantalla.
        elif opcion_elegida == 6:
            # Mensaje limpio de despedida antes de romper el flujo.
            print("\n¡Gracias por utilizar el sistema de gestión! Finalizando ejecución limpia...")
            break # Rompe el ciclo while, terminando el programa de forma controlada.


# Este bloque asegura que el programa comience automáticamente al ejecutar el archivo.
if __name__ == "__main__":
    iniciar_programa()