#Se utiliza cuando no sabemos cuantas iteraciones se van a hacer
#ciclo while nos permite iterar sobre ciertas condicionales
contador=0
bandera=True
while bandera:
	print(contador)
	contador+=1 #tambien se puede poner contador=contador+1
	if contador==5:
		continue
	if contador==6:
	    bandera=False#break
else:
	print("El while a terminado!")
