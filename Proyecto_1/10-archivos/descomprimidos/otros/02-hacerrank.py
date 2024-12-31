

def divisibleSumPairs(n, k, ar):
    # Write your code here

    ind = 1
    ciclo = 1
    n2 = n
    resp = 0

    while (n-1) > 0:
        for x1 in ar:
            ind = ciclo
            while ind < n2:

                if ((x1 + ar[ind]) % k) == 0:
                    resp += 1
                ind += 1

            ciclo += 1

            n -= 1

    return resp


ar = [1, 3, 2, 6, 1, 2]

r= divisibleSumPairs(6, 3, ar)

print(r)