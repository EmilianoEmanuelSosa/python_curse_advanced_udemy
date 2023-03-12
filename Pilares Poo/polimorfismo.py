class Animales():
    def __init__(self,mensaje):
        self._mensaje=mensaje
    def Hablar(self):
        print(self._mensaje) 

class Perro(Animales):
    def Hablar(self):
        print('i do it guaou')

class Pez(Animales):
    def hablar(self):
        print('Yo no hablo')

perro = Perro('guaou')

perro.Hablar()

animal = Animales('arbol')

animal.Hablar()

pez = Animales('nada')
pez.Hablar()
