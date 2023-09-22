x=input()
y=x.split(" ")
l=len(y)
b=1
for i in range(l):
    b=b*int(y[i])
b=b**(1/l)
print(round(b,8))
