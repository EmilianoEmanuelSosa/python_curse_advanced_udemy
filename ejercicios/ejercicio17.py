#Ejercicio 1

#Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. Calcular después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora.

class Calc():
    def __init__(self):
        self._num1 = int(input('Introduce the first Number: ')) 
        self._num2 = int(input('Introduce the second Number: '))
    def addtion(self):
        return print('the adition of {} and {} is: '.format(self._num1,self._num2), self._num1+self._num2)
    def subtration(self):
        return print('The subtration of {} and {} is: '.format(self._num1, self._num2),self._num1-self._num2)
    def multiplication(self):
        return print('The Multiplication of {} and {} is: '.format(self._num1,self._num2),self._num1*self._num2)
    def division(self):
        return print('The Division of {} and {} is: '.format(self._num1,self._num2),self._num1/self._num2)
    
operation = Calc()

operation.addtion()
operation.subtration()
operation.multiplication()
operation.division()