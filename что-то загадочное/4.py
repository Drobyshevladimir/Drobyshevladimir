f = open('input.txt', 'r')
a=f.read()
f.close()
y=a.split(" ")
b=len(y)
z=y[b-1].split("\n")
y[b-1]=z[0]
c=1
if z[1]==('*'):
    for i in range(b):
        c=c*int(y[i])
if z[1]==('+'):
    for i in range(b):
        c=c+int(y[i])
if z[1]==('-'):
    for i in range(b):
        c=c*int(y[i])
print(c)
