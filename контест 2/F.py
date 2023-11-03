kostbiLb=1
e=0
while kostbiLb==1:
    a,b=input().split(' ')

    a=int(a)
    b=int(b)
    if a==0 and b==0:
        break
    else:

        st=input()
        s=list(st)
        #print(s)
        maks=[-1]*(a-b)
        c=0
        d=0
        for i in range(a-b):
            for j in range((c),(b+d+1)):
                
                #print(j)
                if maks[d]<int(s[j]):
                    maks[d]=int(s[j])
                    e=j
                    #print(maks)
            c=e+1
            if d+1!=len(maks):
                d+=1
    for i in range(len(maks)):
        print(maks[i], end ="")
    print('')
        
