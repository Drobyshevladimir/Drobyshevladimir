def prmn(n):
   i = 2
   mn = []
   while i * i <= n:
       while n % i == 0:
           mn.append(i)
           n = n / i
       i = i + 1
   if n > 1:
       mn.append(n)
   return mn

a=int(input())
print(prmn(a))
