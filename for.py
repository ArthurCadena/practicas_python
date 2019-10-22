#El ciclo lo utilizamos cuando tenemos conocimiento de cuantas iteraciones se van a hacer
#nos permite recorrer objetos iterables listas,tuplas,diccionarios,strings
lista=(1,2,3,4,5,6,7,8,9,10,11)
for valor in lista:
	pass
for valor in range(0,20,4):
	pass


for indice,valor in enumerate(lista):
	pass#print(valor,"Tiene el indice: ",indice)

for valor in range(0,len(lista)):
	pass#print(valor)
for valor in "Curso de codigo facilito":
	pass#print(valor)

diccionario={"a":10,"b":20,"c":500}
for llave,valor in diccionario.items():
    print("La llave",llave,"tiene el valor de",valor)
	
