def fac(n, depth=0):
    if n==1:
        return 1
    res = n*fac(n-1, depth+1)
    print( f' on step {depth} fac = {res}')
    return res
    
print(fac(int(input())))
