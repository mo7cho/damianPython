# ## DICCIONARIO

# alumno={
#     "nombre":  "Wanda Maximoff",
#     "carrera": "Informatica",
#     "edad":    24
# }

# # # recorrer cada elemento de un diccionario
# # print(alumno)
# for key, value in alumno.items():
#     print(key, value)
# #buscar
# print(alumno["edad"])

# # insersion 
# alumno["email"]="wanda@gamail.com"

# # actualizacion
# alumno["edad"]=26

# # Eliminacion
# del alumno["carrera"]


# for key, value in alumno.items():
#     print(key, value)

# Ejercicio: Hacer un diccionario con los elementos a elección propia (al menos 4 propiedades)
# Debe hacer: inserción, borrado, actualización y muestra de los mismos
print("Información de película")
pelicula = {
    "nombre": "Blade Runner 2049",
    "año": 2017,
    "genero": "Sci-fi",
    "protagonista": "Replicante K" 
}

for key, value in pelicula.items():
    print(f"- {key.title()}: {str(value).title()}")
#buscar
# Inserción
pelicula["direccion"] = "Denis Vileneuve"

calificacion = input("Ingrese una calificación para la pelicula (0 a 10): ")
pelicula["calificacion"] = calificacion

# Borrado
del pelicula["protagonista"]

# Actualización
pelicula["genero"]= "Neo-Noir"

print("\nInformación de película (actualizada)")
for key, value in pelicula.items():
    print(f"- {key.title()}: {str(value).title()}")


## Cree un diccionario de 3 productos, cada uno 
# con nombre, categoria, precio.

# productos={
#     1:{"nombre": "Laptop",
#        "categoria": "Electronica",
#        "precio": 400000},

#     2:{"nombre": "Chaqueta",
#        "categoria": "Vestuario",
#        "precio": 40000},

#     3:{"nombre": "Caable HDMI",
#        "categoria": "Accesorios",
#        "precio": 5000},

# }

# #print(productos[3]["categoria"])
# print(productos)
# nom=input("Ingrese el nombre del productos: ")
# cat=input("Ingrese la categoria del productos: ")
# precio=int(input("Ingrese el precio del productos: "))

# productos[4]={"nombre": nom,
#        "categoria": cat,
#        "precio": precio}

# print(productos)

# temperaturas={
#     "lunes": 15,
#     "martes": 18,
#     "miercoles":14,
#     "jueves":9,
#     "viernes":19
# }

# print(temperaturas)
# maximos=[]
# for dia, maxi in temperaturas.items():
#    print(dia, maxi)
#    maximos.append(maxi)
# print(max(maximos))