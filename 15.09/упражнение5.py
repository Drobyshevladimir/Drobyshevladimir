a=list(map(int,input().split()))
a.insert(0,a[len(a)-1])
a.pop(len(a)-1)
print(a)
