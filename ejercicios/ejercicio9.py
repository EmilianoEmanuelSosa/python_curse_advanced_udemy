#Ejercicio 1

#En la siguiente lista, debes hacer un programa que muestre los valores al usuario, a su vez, debe pedir dos datos y esos que sean ingresados deben ser sustituidos en el primer y segundo lugar:

#[20, 50, "Curso", 'Python', 3.14]

mostrar=[20, 50, "Curso", 'Python', 3.14]

print(mostrar)
print('\n\n\n\nGive me two date and i add to the list\n\n\n\n')
lista1 = input('First date')
lista2 = input('Second date')

mostrar[0] = lista1
mostrar[1] = lista2

print(mostrar)


#Ejercicio 2

#Escribe una lista que tenga los números de 1 al 10. Luego, debes hacer que los datos que están en las posiciones 4, 7 y 9 sean multiplicados por 2; por último, mostrar la lista nueva con los nuevos datos

listanumber = [1,2,3,4,5,6,7,8,9,10]
print(listanumber)
listanumber[4] *= 2
listanumber[7] = listanumber[7]*2
listanumber[9] = listanumber[9]*2
print(listanumber)
