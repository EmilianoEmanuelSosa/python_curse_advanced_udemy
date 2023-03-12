#Ejercicio 1

#Crear una clase llamada Marino(), con un metodo que sea hablar, en donde muestre un mensaje que diga "Hola...". Luego, crear una clase Pulpo() que herede Marino, pero modificar el mensaje de hablar por "Soy un Pulpo". Por ultimo, crear una clase Foca(), heredada de Marino, pero que tenga un atributo nuevo llamado mensaje y que muestre ese mensaje como parametro.


class Marine():
    def talk(self):
        print('Hi')      

class octopus(Marine):
    def talk(self):
        print('I am a Octopus')

class seal(Marine):
    def talk(self,mensagge):
        self._mensagge = mensagge
        print(self._mensagge)
        
marine = Marine()
Octopus = octopus()
Seal = seal()


marine.talk()
Octopus.talk()
Seal.talk('I am a Seal')
