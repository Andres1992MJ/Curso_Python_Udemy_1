def suma(a, b):
    print(a + b)


suma(5,3)

def suma1(*numeros):
    resultado =0 
    for num in numeros:
        resultado += num
    print(resultado)

suma1(1,53,20)