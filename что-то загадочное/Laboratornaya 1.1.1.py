f = open('s1.txt', 'r')
a=f.read()
f.close()
y=a.split("	")
b=len(y)
z=y[b-1].split("\n")
y[b-1]=z[0]
print(b)
c=0
d=0.37
if z[1]==('*'):
    for i in range(b):
        c=c+(float(y[i])-d)**2
        print(c)
c=(c)**0.5/10
print(c)    
