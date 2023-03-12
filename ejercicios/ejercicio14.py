#Ejercicio 1

#Crear una funcion que pida dos numeros. Si el primero es mayor al segundo, el programa debe retornar el valor 1; si el segundo es mayor al primero, debe retornar -1; si ambos son iguales, debe retornar 0


def introducedates():
    numberone = int(input('first number'))
    numbersecond = int(input('second number'))

    if numberone > numbersecond:
        return 1
    elif numbersecond > numberone:
        return -1
    else:
        return 0
    
print(introducedates())




#Ejercicio 2

#Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

def facturaconiva():
    factura=int(input('the total value of your invoice is?'))
    iva = float(input('How much is your vat percentage'))
    facturatotal = ((factura*iva)/100)+factura
    return 'The total value of your invoice is',facturatotal

print(facturaconiva())