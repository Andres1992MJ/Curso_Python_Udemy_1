

def designerPdfViewer(h, word):
    # Write your code here
    abecedario_dic = {
    "a": 0,
    "b": 0,
    "c": 0,
    "d": 0,
    "e": 0,
    "f": 0,
    "g": 0,
    "h": 0,
    "i": 0,
    "j": 0,
    "k": 0,
    "l": 0,
    "m": 0,
    "n": 0,
    "o": 0,
    "p": 0,
    "q": 0,
    "r": 0,
    "s": 0,
    "t": 0,
    "u": 0,
    "v": 0,
    "w": 0,
    "x": 0,
    "y": 0,
    "z": 0
    }
    pos=0
    for letra in abecedario_dic:    
        abecedario_dic[letra] = h[pos]
        pos+=1
    mayor=0
    for letra in word:
        if  abecedario_dic[letra]>mayor:
            mayor=abecedario_dic[letra]
    
    respuesta= (len(word)*1)*mayor

    return respuesta


numero_entrada=[1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]


test_1 = designerPdfViewer(numero_entrada, "abc")

print(test_1)



