usuarios =[
    [2,"Andres"],
    [1,"Carolina"],
    [4,"Luz"],
    [3,"Dani"]
]

nombres=[]

for usuario in usuarios:
    nombres.append(usuario[1])

print(nombres)

nombres2=[usuario[1] for usuario in usuarios]

print(nombres2)

nombres3=[usuario for usuario in usuarios if usuario[0]>2]

print(nombres3)


nombresMap=list(map(lambda usuario: usuario[1], usuarios))

print(nombresMap)

nombresFilter=list(filter(lambda usuario: usuario[0]>2, usuarios))

print(nombresFilter)