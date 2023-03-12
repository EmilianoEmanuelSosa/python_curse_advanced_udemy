voto = input('A,B,C? Por cual votas?')

if voto.upper == 'A':
    print('Usted ha votado por el partido Rojo, Felicidades.')
elif voto.upper == 'B':
    print('Usted ha votado por el partido Verde, Felicidades.')
elif voto.upper == 'C':
    print('Usted ha votado por el partido Azul, Felicidades.')
else:
    print('respuesta no valida, asegurese de elegir A,B,C')