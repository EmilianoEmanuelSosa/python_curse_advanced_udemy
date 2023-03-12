class A:
    def primera(self):
        return 'Esta es la clase A'
    
class B(A):
    def segunda(self):
        
        return 'Esta es la clase B'
    
class C(B):
    def tercera(self):
        return 'water'

c = C()


print(c.primera())
print(c.segunda())
print(c.tercera())