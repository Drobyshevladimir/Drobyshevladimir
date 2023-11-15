a=int(input())
dots=[]
for i in range(a):
    dots.append(input())
ocb=0
k=[0,0]
for i in range(a):
    k=dots[i].split(' ')
    ocb+=int(k[0])
ocb/=a
numdots=0
for i in range(a):
    k1=int((dots[i].split(' '))[0])
    k2=int((dots[i].split(' '))[1])
    if k1!=ocb:
        if k1<ocb:
            for j in reversed(range (a//2,a)):
                k3=int((dots[j].split(' '))[0])
                k4=int((dots[j].split(' '))[1])
                if k2==k4 and (ocb-k1)==(k3-ocb):
                    numdots+=2
                    break
    else:
        numdots+=1
if numdots==a:
    print('Yes')
else:
    print('No')

