#La funcion nos va a regresar la suma de los valores
def suma(valor_uno,valor_dos,valor_tres):
	return valor_uno+valor_dos+valor_tres

def division(valor_uno,valor_dos):
	return valor_uno/valor_dos

def multiplicacion(valor_uno,valor_dos):
	return valor_uno*valor_dos

resultado=division(valor_uno=10,valor_dos=100)#Segunda forma
resultado=division(100,10)#Primera forma de pasar valores a los parametros
resultado=multiplicacion(6,8)
print(resultado)