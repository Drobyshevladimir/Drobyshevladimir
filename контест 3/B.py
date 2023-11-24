a=int(input())
nachalo=[0]*a
konec=[0]*a
for i in range(a):
    b=(input().split(' '))
    nachalo[i] = int(b[0])
    konec[i] = int(b[1])


c=0
nachalo2=[]
konec2=[]
while(len(nachalo)>0):
    nachalo2=[]
    konec2=[]
    granica=min(konec)
    c+=1
    d=[]
    for i in range(len(nachalo)-1):
        if nachalo[i]>granica:
            d.append(i)
    for i in range(len(d)-1):
        nachalo2.append(nachalo[i])
        konec2.append(konec[i])
    nachalo=nachalo2
    konec=konec2
            
print(c)
