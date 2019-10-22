course="Curso"
my_string="Codigo Facilito!"
"""Metodos de formato"""
result="{a} de {b}".format(a=course,b=my_string)
result=result.lower()#va a estandarizar el string y volvera todo minusculas
result=result.upper()#todo lo pone en mayuscula
result=result.title()
"""Metodos de busqueda"""
pos=result.find("Codigo")#busca la posicion en la que se encuentra una palabra
count=result.count("c")#busca cuantas veces se repite una letra o palabra
new_string=result.replace("c","x")
new_string=result.split(" ")#toma el string y cada que se encuentra con un espacio nos devolvera una lista
print(pos)#imprimimos el resultado
print(result[9])#con esto confirmamos
print(count)
print(new_string)