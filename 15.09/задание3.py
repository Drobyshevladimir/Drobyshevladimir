st=input()
L=len(st)
num_steps = L//2
flag=True
for i in range(num_steps):
    if st[i] != st[-(i+1)]:
        flag = False
        break
print(flag)
res=f'{st} palindrome = {flag}'
print(res)
