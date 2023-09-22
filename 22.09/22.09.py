import numpy as np


N=int(input())

sqr = np.sqrt(N)
print(int(sqr))
dividers= []
i=2
while i<(int(sqr)):
    for i in range(2,int(sqr)):
        if N % i == 0:
            N=N//i
            dividers.append(i)
            i-=1
        i+=1
print(dividers)
