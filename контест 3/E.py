a,b=input().split(' ')
a=int(a)
b=int(b)
c=input().split(' ')
for i in range(a):
    c[i]=int(c[i])
h=0
kolva=[0]*a
for i in range(a):
    for j in range(a):
        if c[j]>i:
            kolva[i]+=1
print(kolva)
while(kolva[h-1]+min((kolva[h-2]-kolva[h-1]),b)>=h):
    h+=1

print(h-1)



"""k=True
while k=True:
    for i in range(h):
    d=b    
    if c[i]>h:
        d+=1"""
        
    

