#1/Crear un programa que pida al usuario una letra, y si es vocal, muestre el mensaje "Es vocal". Sino, decirle al usuario que no es vocal

letra = input('Tell me a vocal')

if letra.lower() == 'a':
    print('this letter is a vocal')
elif letra.lower() == 'e':
    print('this letter is a vocal')
elif letra.lower() == 'i':
    print('this letter is a vocal')
elif letra.lower() == 'o':
    print('this letter is a vocal')
elif letra.lower() == 'u':
    print('this letter is a vocal')
else:
    print('this letter is not a vocal')

# Aqui hay otra forma de resolver el problema

if letra.lower in 'aeiou':
    print('This is a vocal')
else:
    print('this is not a vocal')


#2/Escribir un programa que, dado un número entero, muestre su valor absoluto. Nota: para los números positivos su valor absoluto es igual al número (el valor absoluto de 52 es 52), mientras que, para los negativos, su valor absoluto es el número multiplicado por -1 (el valor absoluto de -52 es 52).

number = int(input('tell me a number and i say you the absolute number of that'))

if number < 0:
    newnumber = (number*-1)
    print('this is the absolute number',newnumber)
else:
    print('this is the absolute number',number)


#hay un metodo de python que encuentra el valor absoluto del numero dado, y este es abs

print(abs(-5))