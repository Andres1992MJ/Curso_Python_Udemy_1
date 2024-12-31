from collections import deque


lista = [1,2,3,4]

fila=deque([1,2,3])

fila.append(4)
fila.append(5)
fila.append(6)

print(fila)


fila.popleft()  #Borra uno a la izquierda

print(fila)

fila.popleft()
fila.popleft()
fila.popleft()
fila.popleft()
fila.popleft()

print(fila)

if not fila:
    print("Lista vacia")