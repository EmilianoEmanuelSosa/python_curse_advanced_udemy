diccionario={1:2,3:4,5:6,7:8}
diccionario2={9:10,11:12,13:14}
print(diccionario)

print(diccionario.get(7))

diccionario.pop(1)
print(diccionario)

diccionario#clear()
print(diccionario)

diccionario.setdefault(4,5)
print(diccionario)

diccionario.update(diccionario2)

print(diccionario)

diccionario.copy()
print(diccionario)