lista1 = [1,2,3,4,5,6,7]

print(lista1) #imprime la lista talcual

print(*lista1)

lista2= [8,9,10,11,12]

combinada1=lista1+lista2

print(combinada1[5])

combinada2=["hola", lista1, "mundo" , lista2]  #no se unen las listas

print(combinada2)

combinada3=["hola", *lista1, "mundo" , *lista2]  #Se unen los valores de las listas en una sola lista añ desempaquetarlo
print(combinada3)


#DICCIONARIOS:

punto1={"x":25, "y":111}

punto2={"y": 150}

puntot= {**punto1,**punto2} #Se reemplaza la y ya que sobreescribe los valores que esten a la derecha, sobre el de la izquierda
print(puntot)

puntot2= {**punto1,"nombre":"FRESA2", **punto2,"z":40,"c":320}

print(puntot2)