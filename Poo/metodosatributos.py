class FabricaTelefonos():
    marca= 'huawei'
    color='negro'
    emoriaRam='8gb'
    almacenamiento=128

    def llamar(self,mensagge):
        return mensagge
    def escucharMusica(self):
        print('you hear music now')




telefono = FabricaTelefonos()

print(telefono.llamar('hola, con quien hablo'))
print(telefono.almacenamiento)
telefono.escucharMusica()