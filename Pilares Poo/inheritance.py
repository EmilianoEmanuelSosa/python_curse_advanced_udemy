class Animals():
    def habla(self):
        print('i am a animal')
    def description(self):
        print('Yo soy una {}'.format(self.animal))

class Perro(Animals):
    pass
class Abeja(Animals):
    def __init__(self,animal):
        self.animal = animal


animal = Animals()
animal.habla()

perro = Perro()
perro.habla() 

abeja = Abeja("Abeja")

abeja.description()