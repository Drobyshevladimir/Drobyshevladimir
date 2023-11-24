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

a=int(input())
nachalo=[0]*(a+1)
konec=[0]*(a+1)
sortirovkaxd=[0]*a
dp=[0]*a
for i in range(a):
    b=(input().split(' '))
    sortirovkaxd[i]=float(int(b[0])*0.00001+int(b[1]))
c=quicksort(sortirovkaxd)
for i in range(a):
    konec[i+1] = int(c[i]//1)
    nachalo[i+1] = round((c[i]%1)*100000)
#print(nachalo)
#print(konec)
dp[0]=0

dp1=[]  
#print(nachalo.index(max(nachalo)))
#print(nachalo)
for i in range(1,a):
    dp1=[]
    for j in range (i):
        dp1.append(dp[j])
    #print(dp1)
    while konec[dp1.index(max(dp1))]>nachalo[i]:
        dp1[dp1.index(max(dp1))]=-1
    #print(dp[i-1])
    dp[i]=1+max(dp1)

print(max(dp))

    

