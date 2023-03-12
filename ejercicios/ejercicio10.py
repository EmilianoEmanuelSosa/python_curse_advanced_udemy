#En el siguiente diccionario se encuentran capitales de los paises en el mundo, debes realizar un programa que pida un pais al usuario, y muestre la capital de ese pais, en dado caso el pais no este en el diccionario, se debe mostrar un mensaje diciendo que ese pais no se encuentra.

#{"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}


import string

print('I say you the capital of your country')


countrys={
    'Guatemala':'Ciudad de Guatemala',
    'El Salvador':'San Salvador',
    'Honduras':'Tegucigalpa',
    'Nicaragua':'Managua',
    'Costa Rica':'San Jose',
    'Panama':'Panama',
    'Argentina':'Buenos Aires',
    'Colombia':'Bogota',
    'Venezuela':'Caracas',
    'Espana':'Madrid'
    }


pais= input('And you country is?:')
pais2 = string.capwords(pais,sep = None)
letter= pais2 in countrys
if letter == True:
    print('The capital of {} is {}'.format(pais2,countrys[pais2]))
else:
    print('{} is not included in this program'.format(pais2))



#Ejercicio 2

#Con el siguiente diccionario, debes crear un programa que pregunte al usuario por un número; el programa debe imprimir el jugador al que hace referencia ese número

'''{

    1 : "Casillas", 15 : "Ramos",

    3 : "Pique", 5 : "Puyol",

    11 : "Capdevila", 14 : "Xabi Alonso",

    16 : "Busquets", 8 : "Xavi Hernandez",

    18 : "Pedrito", 6 : "Iniesta",

    7 : "Villa"
}
'''
number = int(input('give me a number'))

diccionario = {

    1 : "Casillas", 15 : "Ramos",

    3 : "Pique", 5 : "Puyol",

    11 : "Capdevila", 14 : "Xabi Alonso",

    16 : "Busquets", 8 : "Xavi Hernandez",

    18 : "Pedrito", 6 : "Iniesta",

    7 : "Villa"
}

if number in diccionario:
    print('Your player is: ',diccionario[number])
else:
    print('the {} dont stay in the list'.format(number))