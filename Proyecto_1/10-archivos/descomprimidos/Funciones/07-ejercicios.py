def es_palindromo(texto):
    t1= texto.lower().replace(" ","")
    x= len(t1) -1
    tr=""
    
    while x>= 0:
        tr= tr + t1[x]
        x-=1
    
    if tr == t1:
        print(f"{texto}  True")
    else:
        print(f"{texto}  False")


es_palindromo("Reconocer")
es_palindromo("Hola")
es_palindromo("Abba")
es_palindromo("amo la paloma")