f = open('input.txt', 'r')
a=f.read()
f.close()
x=a.split("\n")
print(x)
y = x[0].split(" ")
print(y)
z=[]
y[0]=int(y[0])
y[1]=int(y[1])
for i in range(1,y[1]+1):
    z.append(x[i].split(" "))
    z[i-1].sort()
temp = []
for x in z:
    if x not in temp:
        temp.append(x)
z = temp
print(z)
print(len(z))
otvet=y[0]*(y[0]-1)*(y[0]-2)/6
print(otvet)
otvet-=len(z)*(y[0]-2)
b = []
from itertools import chain
b = list(chain.from_iterable(z))
print(b)
temp = []
x=0
y=[0]*(y[0]+100)
for x in b:
    if x not in temp:
        temp.append(x)
    else:
        r=int(x)
        y[r]+=1
        otvet+=y[r]
print(int(otvet))
