def triangle(size, symb):
    for i in range(1, size + 1):
        print(symb * min(i, size - i + 1))
size, symb = int(input()),input()
triangle(size, symb) 
