class FabricaTelefonos():
    def __init__(self,marca,color):
        self.marca = marca
        self.color = color
        print('el objeto ha sido creado'.format(self.marca))
    def __str__(self):
        return 'El objeto es {}'.format(self.marca)
    
    def __del__(self):
        print('el objeto{}ha sido destruido'.format(self.marca))

telefono = FabricaTelefonos('Nokia','Rosa')

print(telefono.marca,telefono.color)
print(telefono)