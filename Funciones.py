#Funciones sirven para no estar copiando y pegando una serie de codigo repetido numero de veces si no simplemente podriamos  
#mandar a llamar la funcion :D
def factorial_numero(numero):
	factorial=1
	while numero>0:
		factorial=factorial*numero
		numero-=1
	return factorial

resultado=factorial_numero(6)
print(resultado)
#vamos a trabajar con argumentos para que
#nos permita obtener el factorial de cualquier numero 