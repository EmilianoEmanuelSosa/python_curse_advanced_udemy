#Ejercicio 1

#Crear un programa con tres clases Universidad, con atributos nombre (Donde se almacena el nombre de la Universidad). Otra llamada Carerra, con los atributos especialidad (En donde me guarda la especialidad de un estudiante). Una ultima llamada Estudiante, que tenga como atributos su nombre y edad. El programa debe imprimir la especialidad, edad, nombre y universidad de dicho estudiante con un objeto llamado persona.

class university():
    def __init__(self,NombreUni):
        self._NombreUni =  NombreUni
    
class Specialty():
    def specialtymaster(self,Specialty):
        self._Specialty = Specialty

class Student(university,Specialty):
    def data(self,Name,Age):
        self._Name = Name
        self.Age = Age
        print('My name is {},i am {}, i am in specialty {} at the university of {}'.format(self._Name,self.Age,self._Specialty,self._NombreUni))

person = Student('Cambridge')
person.specialtymaster('Software')
person.data('Emiliano','19')