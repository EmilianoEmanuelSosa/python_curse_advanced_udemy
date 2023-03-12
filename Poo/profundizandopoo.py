class FabricaTelefonos():
    def __init__(self,marca,*colores,**modelos):
        self.marca= marca
        self.colores = colores
        self.modelos = modelos

telefono = FabricaTelefonos('Alcatel','Negro','Marron','Azul',m1=500,m2=14)
telefono.memoria =512



print(telefono.marca,telefono.colores,telefono.modelos,telefono.memoria)