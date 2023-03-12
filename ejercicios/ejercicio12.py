#Ejercicio 1

#Imprimir por pantalla los numeros del 1 al 10, luego, pedir al usuario dos numeros y mostrar el rango de numeros entre ambas cifras
'''
i=0

while i < 10:
    print(i)
    i += 1


print('Choose the two number that you want')
number1= int(input('Small number is?'))
number2= int(input('Biggest Number is?'))

while number1 < number2:
    number1 += 1
    print(number1)
    if number1 == (number2-1):
        break
'''
#Ejercicio 2

#Pedir al usuario que ingrese 2 numeros, después, se debe mostrar el rango de esos 2 números, pero, solo imprimiendo los números que sean impares

print('tell me two words and i say the range between odd numbers')

num1= int(input('First Number'))
num2= int(input('Second Number'))


for i in range(num1,num2+1):
    if(i%2 != 0):
        print(i)
    else:
        continue
        
        
        
