with open("input.txt", "r") as f:
    text = f.read()
a=[]*1
gl=['a','e','i','o','u','y']
b=0
for i in range(len(text)):
    if text[i] in gl and not( text[i-1] in gl) :
        a.append(text[i])
        a.append('s')
        a.append(text[i])
    else:
        a.append(text[i])
result = "".join(a)
print(result)
