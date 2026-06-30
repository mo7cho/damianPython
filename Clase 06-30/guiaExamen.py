autos = {
    "A001": ["Toyota", "Corolla", 2010, 5],
    "A002": ["Ford", "Ranger", 2019, 4],
    "A003": ["Chevrolet", "Spark", 2022, 4],
    "A004": ["Suzuki", "Aerio", 2000, 4],
    "A005": ["Toyota", "Yaris", 2015, 5],
    "A006": ["Chevrolet", "Impala", 1950, 4],
    "A007": ["Ford", "Mustang", 2005, 5]
}

operaciones = {
    "A001": ["01-01-2024", "12-12-2015"],
    "A002": ["07-08-2024", "Pendiente"],
    "A003": ["09-01-2025", "Pendiente"],
    "A004": ["24-03-2025", "Pendiente"],
    "A005": ["24-03-2024", "24-07-2024"],
    "A006": ["24-03-2020", "Pendiente"],
    "A007": ["24-03-2024", "Pendiente"]
}

def autos_vendidos_por_parca(marca):
    total = 0

    for id_auto, datos in autos.items():

        if datos[0].lower() == marca.lower():

            if operaciones[id_auto][1] == "Pendiente":
                total += 1
    
    print(f"EL número total de autos vendidos de la marca {marca} es: {total}")

def busqueda_por_anio(anio_min, anio_max):
    elementos = []

    for id_auto, datos in autos.items():
        marca = datos[0]
        modelo = datos[1]
        anio = datos[2]

        if anio_min <= anio <= anio_max:

            if operaciones[id_auto][1] == "Pendiente":
                elementos.append(f"{marca} {modelo} -- {id_auto}")
    
    if elementos:
        elementos.sort()
        print(elementos)
    else:
        print("No se han encontrado elementos")


## MAIN
while True:
    try:
        anio_inicio = int(input("Ingrese el año de inicio de la búsqueda: "))
        anio_termino = int(input("Ingrese el año de término de la búsqueda: "))

        busqueda_por_anio(anio_inicio, anio_termino)
        break

    except:
        print("Los años ingresados deben ser números enteros.")