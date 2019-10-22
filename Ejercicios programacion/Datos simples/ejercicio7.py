peso= input("Cual es tu peso en KG ")
altura= input("Cual es tu estatura en metros ")
bmi=round(float(peso)/float(altura)**2,2)
print("Tu indice de masa es: "+ str(bmi))
