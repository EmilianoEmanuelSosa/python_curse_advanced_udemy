
from math import sqrt

A = int(input('Ingrese el coeficiente A:'))
B = int(input('Ingrese el coeficiente B:'))
C = int(input('Ingrese el coeficiente C:'))

if ((B**2)-(4*A*C) < 0):
    print('No es posible realizar esta operacion')
else:
    x1 = (-B + sqrt((B**2)-(4*A*C)))/(2*A)
    x2 = (-B - sqrt((B**2)-(4*A*C)))/(2*A)
    print("la Solucion es:\nx1=",x1,"\nx2=",x2)