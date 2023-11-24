def Partition(A,m):
    L = []
    R = []
    for ai in A:
        if ai <= m:
            L.append(ai)
        elif ai > m:
            R.append(ai)
    return L, R

def five_med(B):
    for j in B:
            count_less = 0
            count_more = 0
            count_eq = 0
            for c in B:
                if c < j:
                    count_less += 1
                elif c > j:
                    count_more += 1
                else:
                    count_eq += 1
            if (count_less == count_more):
                b = j
                break
            elif (count_less == 0 and count_eq == 3) or (count_more == 0 and count_eq == 3) \
            or (count_more == 1 and count_eq == 2) or (count_less == 1 and count_eq == 2) \
            or (count_eq == 4):
                b = j
                break
    return b
a=(input().split(' '))
print(a)

print(five_med(a))
