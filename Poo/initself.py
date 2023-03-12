'''class FabricaTelefomos():
    marca='samsung'

    def ElaborarHuawei(self):
        self.marca= 'Huawei'

telefono = FabricaTelefomos()

telefono.ElaborarHuawei()

print(telefono.marca)'''

class FabricaTelefonos():
    def __init__(self,marca,color):
        self.marca = marca
        self.color = color


telefono = FabricaTelefonos('Huawei','Avellana')


print(telefono.marca)
print(telefono.color)



