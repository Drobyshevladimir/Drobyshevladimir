n, k = map(int, input().split())
a = input().split(" ")
maks=0
for i in range (2**n):
    if (int(a[(i)^k])+int(a[i]))>maks:
        maks = (int(a[(i)^k])+int(a[i]))    
print(maks)
