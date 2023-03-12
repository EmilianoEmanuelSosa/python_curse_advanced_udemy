class A():
    def __init__(self):
        self._contador = 0
    def incrementar(self):
        self._contador += 1
    def cuenta(self):
        return self._contador
    
# is a bad practice, modify an atributte without the get method.