b=int(input())
a=list(map(int,input().split()))

for i in range(len(a)):
    c=0
    for j in range(len(a)):
       if a[i]>a[j]:
           c+=1
    if c==int(b)//2:
        print(a[i])
        
        
