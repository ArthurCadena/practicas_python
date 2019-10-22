#condicionales
fruta="kiwi"
if fruta!="kiwi":#Si y solo si la condicional se cumple
	print("El valor es kiwi")
elif fruta=="manzana":
	print("Es una manzana")
elif fruta=="platano":
	pass

elif fruta=="sandia":
	print("Es una sandia")
else:
	print("No son iguales")

#True=1
#False=0
valor=0
valor_dos=2
if valor or valor_dos > 20:
	print("Es verdad")
else:
	print("No es verdad")
#mensaje="El valor es kiwi" if fruta=="kiwi"else "No son iguales"
#print(mensaje)

