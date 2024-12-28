#Aca son listas con orden FIFO

pila=[]

pila.append(1)
pila.append(2)
pila.append(3)

print(pila)

ultimoElemento=  pila.pop()   #Borro el 3

print(ultimoElemento)  

print(pila[-1])  # de esta manera siempre muestra el valor en la ultima poscicion de la fila

pila.pop()
pila.pop()

print(pila)

if not pila:
    print("cola vacia")