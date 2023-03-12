
#Ejercicio 1

#Escribir un programa que pida un numero al usuario y muestre las tablas de multiplicar de ese numero


number=int(input('Tell me a number and i say his table: '))
i=0
while i<10:
    i += 1
    result = number*i
    print(number,'x',i,':',result)


#Ejercicio 2

#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).


edad = int(input('Say me your Age: '))
j=1
while j!= edad:
    print(edad)
    j-=1
