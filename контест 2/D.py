a=input()
flag=True
s=list(a)
prefix=[]
for i in range (len(s)):
    if s[i]=='(' or s[i]=='{' or s[i]=='[':
        prefix.append(s[i])
    elif (s[i]==')' and prefix[-1]=='(')or (s[i]==']' and prefix[-1]=='[') or (s[i]=='}' and prefix[-1] == '{'):
        prefix.pop(-1)
    else:
        flag=False
if prefix==[] and flag:
    print('Yes')
else:
    print('No')
