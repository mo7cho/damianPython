# titulo="Clima actual" #tipo string
# temp=18.6 #float
# diaDelMes=16 #int
# mes=4 #int
# llueve=True

# print(f"{titulo}")
# print(f"Fecha de hoy: {diaDelMes}-{mes}")
# print(f"Tempreatura actual {temp} grados")

# if llueve :
#     print("Saco el paraguas")
# else:
#     print("No saco el paraguas")

# num=10

# 7>num --->False
# "blue"=="blue"--->True

# num=int(input("Ingrese un numero: "))

# for i in range(num):

#     print(f"{i+1} Hola Camello")

# nombre=input("Ingrese su nombre: ")
# vocales=0
# cons=0
# for i in nombre:
#     print(i)
#     # vocales=vocales+1
#     if i in "aeiou":
#         vocales+=1
#     elif i==" ":
#         print()
#     else:
#         cons+=1
# print(f"La cant de vocales es {vocales}")
# print(f"La cant de consonantes es {cons}")

#Uso de f string

# titulo="Clima de hoy"  # String
# diaDelMes=13  # int
# mes=4       #int

# temperatura=22.3 # float

# llueve=False # boolean

# print(titulo,"temperatura actual:", temperatura, "al dia",diaDelMes, "/", mes )
# print(f"{titulo} temperatura actual: {temperatura} al dia {diaDelMes}/{mes}")
# print(titulo +"temperatura actual:" )


# print("Hola Daniel "*3)
# n="daniel"
# print(n[-12])


# name1="Catalina Pinochet"
# print(len(name1))
# name2=" Vicente "

# print(name2.strip())
# print(name1.lower())
# print(name1.upper())
# print(name1.replace("Pinochet", "Frei"))
# print(name1.find("Pinochet"))



'''Pedir a la clave al usuario y verificar 
que sea SHAZAM independiente de su case
(sin inporta si son mayusculas o minusculas)'''

# clave="SHAZAM"

# nom=input("Ingresá la clave: ")

# if nom.upper() == clave:
#     print("Clave correcta")
# else:
#     print("Clave invalida")

'''Crear un nombre de usuario y verificar su que 
su largo esté entre 4 y 10 caracteres
'''
# def nombreUsuario():
#     nombre=input("Ingrese su nombre de usuario: ")

#     if 4<=len(nombre)<=10 :
#         print("Usuario correcto")
#     else:
#         print("Usuario fuera de rango")

# '''Cear un pin y que este tenga exactamente
# 4 digitos'''

# pin=int(input("Ingrese un pin de 4 digitos"))
# 542452345234532532
# if len(str(pin))==4:
#     print("Pin creado")
# else:
#     print("Pin NO creado")

# if 1000<=pin<=9999:
#     print("Pin creado")
# else:
#     print("Pin NO creado")

