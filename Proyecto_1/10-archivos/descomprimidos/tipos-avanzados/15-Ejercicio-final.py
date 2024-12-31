def eliminarEspaciosBlancos(str):
    resp=[]
    for x in str:
        if x != " ":
            resp.append(x.lower())
    return resp


prueba="Este es un string de prueba"

imprime= eliminarEspaciosBlancos(prueba)

print(imprime)

def diccionarioRepeticion(str):
    resp={}
    caracter=str

    for x in caracter:
        resp[x]=resp.get(x,0) + 1
    return resp

#print(diccionarioRepeticion("Hoolaaaaah   a"))

test=diccionarioRepeticion("Hoolaaaaah   a")

# for valor in test:
#     print(valor, test[valor])

def diccionarioATuplas(dic={}):
    listRespuesta=[]
    for valor in dic.items():
        listRespuesta.append(valor)
    return listRespuesta
diccionariodeOPrueba={'h': 2, 'o': 3, 'l': 1, 'a': 3, 't': 3}

test2=diccionarioATuplas(diccionariodeOPrueba)

print(test2)

def mayorRepeticion(list):
    listrespusta=[]
    rep=0
    for valor in list:
        if valor[1]>rep:
            rep=valor[1]
        
    for valor in list:
        if valor[1]==rep:
            listrespusta.append(valor)
    return listrespusta

test3=mayorRepeticion(test2)

print(test3)

def mensajeDeRespuesta(list):
    print(f"Los caracteres que mas se repiten con {list[0][1]} repeticiones son:")
    for valor in list:
        print(f"- {valor[0].upper()}")

mensajeDeRespuesta(test3)



def solucionFinal(str):


    p1= eliminarEspaciosBlancos(str)
    p2= diccionarioRepeticion(p1)
    p3= diccionarioATuplas(p2)
    p4= mayorRepeticion(p3)
    mensajeDeRespuesta(p4)


solucionFinal("AaAdEEEfgGGg")
