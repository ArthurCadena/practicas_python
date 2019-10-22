my_list=["strings",15,15.6,True]
my_list.append(6)#esto envia un valor nuevo al final de la lista
my_list.insert(1,"insert")#insertamos un valor con parametros
my_list.remove(15)#remueve un dato en especifico
last_value=my_list.pop()
print(my_list)
print(last_value)

new_list=[1,4,25,79,9,2,10,12]
new_list2=[22,33]
new_list.sort(reverse=True)#Ordena la lista de menor a mayor y si queremos de mayor a menor usamos reverse=True
#new_list.extend(new_list2)
new_list.append(new_list2)
print(new_list)