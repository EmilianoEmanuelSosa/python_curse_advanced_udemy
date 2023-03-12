#Ejercicio 1

#Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio; luego crear dos clases mas que hereden de Fabrica, las cuales son Moto y Carro. Crear metodos que muestren la cantidad de llantas, color y precio de ambos transportes. Por ultimo, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno


class Factory:
    def __init__(self):
        self._tires = int(input('How tires have your vehicle?: '))
        self._color = str(input('What color is your car?: ' ))
        self._price = int(input('How much is your car worth?: '))

class Car(Factory):

            def sellmyself(self):
                if self._tires == 4:
                    print('Your Vehicle have {} tires is {} and his value is {}'.format(self._tires,self._color,self._price))

                else:
                     print('This is not a Car')


class Motorcicle(Factory):
    def sellmyself(self):
       if self._tires == 2:
           print('Your vehicle is a motorcicle have {} tires is {} and his value is {}'.format(self._tires,self._color,self._price))
       else:
            print('This is not a motorcicle')


car = Car()
car.sellmyself()

motorcicle = Motorcicle()

motorcicle.sellmyself()



