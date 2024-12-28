# def migratoryBirds(arr):
# Write your code here
# min=0
arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]
num = len(arr)
nummax=0 
rep1 =  0

for y in arr:

    if y>nummax:
        num = y

print (nummax)

for x in arr:
    rep = arr.count(x)

    if (x<= num and (rep>=rep1)) or ((x>num)and(rep>rep1)):
        num= x
        rep1= rep
        

    
    print(f"El {x} se repite {rep} veces")
    print(f"asigna {num}")
    print(rep1)
