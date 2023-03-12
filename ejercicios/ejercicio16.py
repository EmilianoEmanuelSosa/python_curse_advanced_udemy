#Ejercicio 1

#Realizar un programa que conste de una clase llamada Estudiante, que tenga como atributos el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Student():
    def __init__(self,name,qualification):
        self._name = name
        self._qualification = qualification
    def showquafication(self):
        if self._qualification >= 7:
            return print('{} you have passed the semester, and your qualification is {}'.format(self._name,self._qualification))
        else:
            return print('{} you dont passed the semester, and your qualificatin is {}'.format(self._name,self._qualification))


Emiliano = Student('Emiliano', 8)

Emiliano.showquafication()