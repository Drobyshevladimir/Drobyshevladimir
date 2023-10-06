a, b = map(int, input().split())
a1=a
b1=b
while a != b:
    if a>b:
        a -=b
    else:
        b -=a
i = 0
while (a - i*a1) % b1 != 0:
    i+=1
j = 0
while (a - j*b1) % a1 != 0:
    j+=1
if (abs(i)+abs((a - i*a1) // b1) )<(abs(j)+abs((a - j*b1) // a1)):
    print(i,(a - i*a1) // b1,a)

elif (abs(i)+abs((a - i*a1) // b1) )==(abs(j)+abs((a - j*b1) // a1)):
    if(i<(a - j*b1) // a1):
        print(i,(a - i*a1) // b1,a)

    else:
        print ((a - j*a1) // b1,j,a)

else:
    print((a - j*b1) // a1,j,a)

