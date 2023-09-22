with open("input.txt", "r") as f:
    text = f.read()
a=[]*1
b=0
for i in range(2,len(text)):
    if text[i]==text[i-1]==text[i-2]=='.':
        a.append(i)
        b+=1

for i in range(len(text)):
    if ((text[i]=='.')and(not((i in a)or(i+1 in a)or(i+2 in a)))):
        b+=1
for i in range(len(text)):
    if text[i]=='?':
        a.append(i)
        b+=1
for i in range(len(text)):
    if ((text[i]=='!')and(not((i in a)or(i-1 in a)))):
        b+=1
print(b)
