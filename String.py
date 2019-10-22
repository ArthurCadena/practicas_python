my_string="Hola Mundo!" #Un string es una lista de caracteres
my_string="""Este es un string que contiene saltos
de linea como se puede ver."""
course="Python 3"
name="Eduardo"
final_message="Nuevo curso de "+course+" por "+name#1
final_message="Nuevo curso de %s por %s"%(course,name)#2
final_message="Nuevo curso de {} por {}".format(course,name)#3
print(my_string)
print(final_message)
