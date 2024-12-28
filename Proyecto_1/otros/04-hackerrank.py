def catAndMouse(x, y, z):
    catA=z-x
    catB=z-y
    resp=""

    if catA<0 :
        catA = catA * -1
    
    if catB<0 :
        catB = catB * -1

    if catA == catB:
        resp="Mouse C"
    if catA>catB:
        resp="Cat B"
    if catA<catB:
        resp="Cat A"
    return resp


catAndMouse(1,7,2)