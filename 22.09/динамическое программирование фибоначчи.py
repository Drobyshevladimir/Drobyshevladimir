N=int((input()))
fibs = [0 for i in range(N)]


fibs[0]=0
fibs[1]=1
for i in range(2,N):
    fibs[i]=fibs[i-1]+fibs[i-2]

print(fibs[N-1])
