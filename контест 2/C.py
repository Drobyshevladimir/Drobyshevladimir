N=int(input())
for i in range(N):
    a=input().split(" ")
    K=int(a[0])
    T=int(a[1])

    x=[]
    y=[]
    l=[]
    L=0
    for j in range(K):
        a=input().split(" ")
        x.append(float(a[0]))
        y.append(float(a[1]))
        
        if j!=0 :
    
            l.append(float(L))
            L=L+((x[j]-x[j-1])**2+(y[j]-y[j-1])**2)**0.5
            

    l.append(L)
    
    dist=L/(T-1)
    
    treesx=[0]*T
    treesy=[0]*T
    treesx[0]=x[0]
    treesy[0]=y[0]
    for j in range(1,T-1):
        b=1
        while(j*dist>l[b]):
            b+=1
        treesx[j]=(j*dist-l[b-1])/(l[b]-l[b-1])*(x[b]-x[b-1])+x[b-1]
        
        treesy[j]=(j*dist-l[b-1])/(l[b]-l[b-1])*(y[b]-y[b-1])+y[b-1]
    treesx[-1]=x[-1]
    treesy[-1]=y[-1]
    print(f'Road #{i+1}:')
    for j in range(T):
        a[0]=str('{:.2f}'.format(treesx[j]))
        a[1]=str('{:.2f}'.format(treesy[j]))
        print(a[0],a[1])

