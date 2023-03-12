#Ejercicio 1

#Crear un programa que tenga dos funciones, una que contenga el area de un cuadrado con argumentos de base y altura; y la otra el area de un circulo con argumento de radio


def arearectangle(base,high):
        area= base*high
        return area


print(arearectangle(15,16))


def arecircle(radius):
        PI= 3.14159
        areacircle= PI*pow(radius,2)
        return areacircle

print(arecircle(78))
#Ejercicio 2

def lista(*lista):
    for i in lista:
           print(i)
    return len(lista)

print(lista(1,2,3,4,5,'hola'))      


#Escribir una función que reciba una muestra de números en una lista y devuelva su medida.

