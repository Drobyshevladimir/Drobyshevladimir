x=input()
y=x.split(" ")
a=int(y[0])
b=int(y[1])
for i in range((abs(a-b)),22500):
    if (a + i)%b==0 and (b+i)%a==0:
        break
print(i)
