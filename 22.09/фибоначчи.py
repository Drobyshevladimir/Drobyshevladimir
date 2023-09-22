def fib(n,fibs):
    if n==1:
        fibs[0]=0
        return 0
    elif n==2:
        fibs[1]=1
        return 1
    if fibs[n-1] != 0:
        return fibs[n-1]
    fibs[n-1]=fib(n-1,fibs)+fib(n-2,fibs)
    return fibs[n-1]
    #print( f' on step {depth} fib = {res}')
n=int(input())
fibs = [0 for i in range(n+1)]
for i in range(n):    
    print(fib(i,fibs))
print(fibs)
