x=input()
y=x.split(" ")
a=int(y[0])
b=int(y[1])
c=0
while a%2!=0 and b%2 != 0 and (a!=1 or b !=1):
    c+=1
    a=a//2
    b=b//2

d=0
for i in range(c):
    d+=4**i
print(d)
