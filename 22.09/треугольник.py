def tri(N,i):
    if N == 0:
        return
    print('.'*i)
    tri(N-1,i+1)
    print('.'*i)



N=int(input())
if N%2 == 1:
    tri(N//2 +1,1)
else:
    tri(N//2,1)
