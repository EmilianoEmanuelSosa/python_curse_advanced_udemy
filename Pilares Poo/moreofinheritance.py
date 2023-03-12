class Animals:
    def __init__(self,name):
        self.name = name
    
class Dog(Animals):
    def __init__(self,name,sound):
        super().__init__(name)
        self.sound = sound

dog = Dog('Firulais','guaaoo')
print(dog.name)