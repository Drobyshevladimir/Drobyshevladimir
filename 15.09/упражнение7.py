a=list(map(int,input().split()))
b=0
c=0
for i in range(len(a)):
    if a.count(a[i])>b:
        b=a.count(a[i])
        c=a[i]
print(c)
