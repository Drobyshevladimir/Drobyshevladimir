dp=[0]*40

dp[3]=1
dp[4]=3
dp[5]=dp[4]*2+2**1-dp[1]
a=int(input())
high=[]
while not(a==0):
    high.append(a)
    a=int(input())

for i in range(6,max(max(high)+1,7)):
    dp[i]=dp[i-1]*2+2**(i-4)-dp[i-4]
#print(dp)
for i in range(len(high)):
    print(dp[high[i]])
