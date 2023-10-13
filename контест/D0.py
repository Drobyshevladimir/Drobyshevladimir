c=int(input())
x=input()
y=x.split(" ")
y.pop (len(y)-1)
n=0
k=0
for i in range (c):
    y[i]=int(y[i])
for i in range(c-1):
    if(max(y[(i+1):])>y[i]):
        k-=y[i]
        n+=1
    else:
        k+=y[i]*n
        n=0
k+=y[c-1]*n
n=0
print(k)
