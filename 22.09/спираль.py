import numpy as np

M=int(input())
N=int(input())
A=[0 for i in range(N)]
arr=np.array(A)

arr=np.zeros=(N)
B=[]
for i in range(N):
    A=[0 for j in range(M)]
    B.append(A)
print(*B, sep = '\n')
count = 0
i,j = 0,0
n1=N
m1=M
while count != N*M:
    while i<n1:
        B[i][j] = count
        i+=1
        count+=1
   
    i-=1
    j+=1
    while j<m1:
        B[i][j] = count
        j+=1
        count+=1

    j-=1
    n1-=1
    m1-=1
    i-=1
    while i>-1:
        B[i][j] = count
        i-=1
        count+=1

    i+=1
    j-=1
    while j>-1:
        B[i][j] = count
        j-=1
        count+=1
    
    j+=1    
    n1-=1
    m1-=1
    i+=1
print(B)
