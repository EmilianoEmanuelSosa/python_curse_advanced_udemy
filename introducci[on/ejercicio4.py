# Este programa, Realiza el promedio entre el promedio de 3 practicas, el examen parcial y el examen final

p1 = int(input("Ingrese la nota de la primer practica"))
p2 = int(input("Ingrese la nota de la segunda practica"))
p3 = int(input("Ingrese la nota de la tercer practica"))
ep = int(input("Ingrese la nota del examen parcial"))
ef = int(input("Ingrese la nota del examen final"))


promedio3 = (p1+p2+p3)/3
pf = (promedio3+ep+ef)/3

print("Tu promedio final es de:",pf) 
