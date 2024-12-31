posicion= {
    "x": 25,
    "y": 50
}
print(posicion["x"])
print(posicion["y"])

posicion["z"] = 150  #agregamos una llave al diccionario

print(posicion)

print(posicion.get("x")) #solicitamos el valor de la llave 

print(posicion.get("noadd",97)) #como no add no existe se le puede dar un valor por defecto

del posicion["y"] #borramos y

print(posicion) #ya no existe y

posicion["y"] = 550

for valor in posicion:
    print(valor)            #imprime solo las llaves 


for valor in posicion:
    print(valor, posicion[valor])   #imprime las llaves con sus valores

for valor in posicion.items():     #metodo que llama el diccionario y entrega los valores en tuplas
    print(valor)


for llave,valor in posicion.items():     
    print(llave, valor)                #forma de desempaquetar las tuplas


usuarios=[
    {"id":1,
     "nombre": "Andres",
     "apellido":"Medina"
    },
    {"id":2,
     "nombre": "Carolina",
     "apellido":"Diosa"
    },
    {"id":3,
     "nombre": "Daniela",
     "apellido":"Jurado"
    },
]

for usuario in usuarios:
    print(usuario["apellido"])