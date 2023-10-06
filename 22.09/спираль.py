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

count=0
i=0
j=0
j1=M
i1=N
i0=0
j0=0

while count != M*N:

    for j in range(j0,j1):
        count+=1
        B[i][j]=count
    i0+=1
    if count != M*N:
        for i in range(i0,i1):
            count+=1
            B[i][j]=count

        j1=j1-1
        
        if count !=M*N:
            for j in reversed( range (j0,j1)):

                
                
                count+=1
                B[i][j]=count
            i1-=1
            if count != M*N:
                
                for i in reversed(range (i0,i1)):

                    count+=1
                    B[i][j]=count
                j0+=1
for i in range(N):
    for j in range(M):
        B[i][j]=B[i][j]*(i+1)
print(*B, sep = '\n')
