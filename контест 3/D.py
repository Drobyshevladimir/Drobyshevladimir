import random

def quicksort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
        s_nums = []
        m_nums = []
        e_nums = []
        for n in nums:
            if n < q:
                s_nums.append(n)
            elif n > q:
                m_nums.append(n)
            else:
                e_nums.append(n)
        return quicksort(s_nums) + e_nums + quicksort(m_nums)


a=input().split(' ')
N=int(a[0])
R=int(a[1])
a=(input().split(' '))
#for i in range(len(a)-1):
    #a[i]=int(a[i])
a=quicksort(a)
for i in range(N):
    a[i]=int(a[i])
yestwifi=0
skokavyshek=0
for i in range(N):
    if yestwifi<a[i]:
        yestwifi=a[i]+2*R
        skokavyshek+=1
print(skokavyshek)
