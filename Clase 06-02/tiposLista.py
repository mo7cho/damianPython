# Tipos de datos de colección en Python
lista = [1, 2, 3, 4, 5]
tupla = (1, 2, 3, 4, 5)
diccionario = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
conjunto = {1, 2, 3, 4, 5}

# Tipos de modificación para cada dato
# lista
# Mutable.
# Se puede modificar un elemento por índice: lista[0] = 10
# Añadir elementos: append(), extend(), insert()
# Eliminar elementos: remove(), pop(), del lista[i], clear()
# Reordenar: sort(), reverse()
# Cortar y concatenar para crear una nueva lista
print("Lista original:", lista)
lista[0] = 10
print("Lista después de lista[0] = 10:", lista)
lista.append(6)
print("Lista después de append(6):", lista)
lista.extend([7, 8])
print("Lista después de extend([7, 8]):", lista)
lista.insert(1, 20)
print("Lista después de insert(1, 20):", lista)
lista.remove(4)
print("Lista después de remove(4):", lista)
valor = lista.pop()
print(f"Lista después de pop() = {valor}:", lista)
del lista[2]
print("Lista después de del lista[2]:", lista)
lista.clear()
print("Lista después de clear():", lista)
lista = [1, 2, 3, 4, 5]
lista.sort(reverse=True)
print("Lista después de sort(reverse=True):", lista)
lista.reverse()
print("Lista después de reverse():", lista)
lista2 = lista[:2] + [9, 10]
print("Nueva lista a partir de cortar y concatenar:", lista2)

# tupla
# Inmutable.
# No se puede cambiar un elemento directo: tupla[0] = 10 da error
# No tiene append(), remove(), ni pop()
# Solo se pueden crear nuevas tuplas a partir de las existentes, por ejemplo:
# tupla2 = tupla + (6,)
# tupla3 = tupla[:2] + (9, 10)
print("\nTupla original:", tupla)
try:
    tupla[0] = 10
except TypeError as e:
    print("Error al modificar tupla directamente:", e)
tupla2 = tupla + (6,)
print("Tupla2 = tupla + (6,):", tupla2)
tupla3 = tupla[:2] + (9, 10)
print("Tupla3 = tupla[:2] + (9, 10):", tupla3)

# diccionario
# Mutable.
# Añadir o modificar un valor con clave: diccionario["f"] = 6
# Eliminar elementos: del diccionario["a"], pop("b")
# Actualizar varios pares: diccionario.update({"a": 10, "f": 6})
# Vaciar todo: diccionario.clear()
print("\nDiccionario original:", diccionario)
diccionario["f"] = 6
print("Después de diccionario['f'] = 6:", diccionario)
diccionario["a"] = 10
print("Después de diccionario['a'] = 10:", diccionario)
diccionario.pop("b")
print("Después de pop('b'):", diccionario)
diccionario.update({"a": 20, "g": 7})
print("Después de update({'a': 20, 'g': 7}):", diccionario)
diccionario.clear()
print("Después de clear():", diccionario)

# conjunto
# Mutable.
# Añadir elementos: conjunto.add(6), conjunto.update({7, 8})
# Eliminar elementos: remove(3), discard(4), pop(), clear()
# Operaciones de conjuntos (no modifican índices porque no tienen orden):
# unión: conjunto | otro_conjunto
# intersección: conjunto & otro_conjunto
# diferencia: conjunto - otro_conjunto
# diferencia simétrica: conjunto ^ otro_conjunto
conjunto = {1, 2, 3, 4, 5}
print("\nConjunto original:", conjunto)
conjunto.add(6)
print("Después de add(6):", conjunto)
conjunto.update({7, 8})
print("Después de update({7, 8}):", conjunto)
conjunto.remove(3)
print("Después de remove(3):", conjunto)
conjunto.discard(4)
print("Después de discard(4):", conjunto)
pop_valor = conjunto.pop()
print(f"Después de pop() = {pop_valor}:", conjunto)
conjunto.clear()
print("Después de clear():", conjunto)
otro_conjunto = {1, 2, 3}
conjunto = {2, 3, 4}
print("Conjunto A:", conjunto)
print("Conjunto B:", otro_conjunto)
print("Unión A | B:", conjunto | otro_conjunto)
print("Intersección A & B:", conjunto & otro_conjunto)
print("Diferencia A - B:", conjunto - otro_conjunto)
print("Diferencia simétrica A ^ B:", conjunto ^ otro_conjunto)

