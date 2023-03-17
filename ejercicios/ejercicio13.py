# #Ejercicio 1

# #Crear un programa que tenga una lista, luego crear una funcion con la cual se van a pedir numeros al usuario para agregar a la lista. Debes crear una segunda funcion en donde se ordenen los numeros pares e impares dentro de dos listas nuevas


# print('tell me numbers and I order them')

# list = []
# def introdatos():
#     can = int(input('how many numbers do you want to order?'))
#     for i in range(0,can):
#         element = int(input('Introduce your number:'))
#         list.append(element)

# introdatos()

# def orderdatos():
#     oddnumbers = [i for i in list if i%2!=0]
#     evennumbers = [i for i in list if i%2 == 0]
#     print(' Even Numbers:',evennumbers,'\n','Odd Numbers:',oddnumbers)

# orderdatos()



# #Ejercicio 2

# #Escribir una función que reciba un número entero positivo y devuelva su factorial

# def funcionfac():
#     from math import factorial

#     firstfactorial = int(input('introduce the number that you want to make its factorial'))
#     if firstfactorial > 0:
#         print(factorial(firstfactorial))
#     else:
#         print('This is a negative number')
# funcionfac()



# i = 1
# j = 2
# firstfactorial = 7
# variablecontadora=1
# while variablecontadora< firstfactorial+1:
#     i*=j
#     j+=1
#     variablecontadora+=1
#     if variablecontadora == firstfactorial:
#         print(i)
#     else:
#         continue

#other way to do it

# firstfactorial = 7
# factor = 1
# for i in range(1,firstfactorial+1):
#     factor = factor*i
# print(factor)