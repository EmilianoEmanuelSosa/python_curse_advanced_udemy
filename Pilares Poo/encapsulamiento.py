class A():
    def __init__(self):
        self.__contador = 0
    def incrementar(self):
        self.__contador +=1
    def cuenta(self):
        return self.__contador
    
class B():
    def __init__(self):
        self.__contador = 0
    def incrementar(self):
        self.__contador +=1
    def cuenta(self):
        return self.__contador


a = A()
print(a.cuenta())
a.incrementar()
print(a.cuenta())
print(a.contador)

