#Lo que hace diferente a una lista o de una tupla un diccionario,el diccionario no se rige por un indice
diccionario={ "a":True,5:"Estos es un string",(1,2):False,"a":False}#diccionario clave a con valor de 55
diccionario["c"]="Nuevo string"#podemos expandir o disminuir las claves de diccionario
diccionario["a"]=False
valor=diccionario.get("z","No se encontro valor")
#del diccionario[5]#del nos ayuda a eliminar
#print(diccionario)#las claves deben ser inmutables,si existen 2 llaves iguales y va a tomar el valor de la ultima llave
#print(valor)

llaves=list(diccionario.keys())#objeto iterable
valores=list(diccionario.values())
diccionario_dos={"z":23,"w":88}
#diccionario["z"]=diccionario_dos
#diccionario["w"]=diccionario_dos
diccionario.update(diccionario_dos)
print(llaves)
print(valores)
print(diccionario)