def dumbgen(n):
    for i in range(1, n+1):
        if (n % i == 0) and (i % 2 != 0):
            yield i
            

for e in dumbgen(9):
    print(e)