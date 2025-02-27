n=int(input())
dp=[0]*(1000001)
dp[2]=1
dp[3]=1
dp[4]=2
dp[5]=3
#dp[6]=dp[6//2=2]+1=2
#dp[7]=dp[7-1]+1=3
#dp[8]=dp[8//2]+1=3
#dp[9]=dp[9//3]+1=2
#dp[10]=dp[6//2=2]+1=2

for i in range(6,n+1):
    if i%3==0 and i%2!=0:
        dp[i]=min(dp[i-1]+1,dp[i//3]+1)
    elif i%3 !=0 and i%2==0:
        dp[i]=min(dp[i-1]+1,dp[i//2]+1)
    elif i%3==0 and i%2==0:
        dp[i]=min(dp[i-1]+1,dp[i//2]+1,dp[i//3]+1)
    else:
        dp[i]=dp[i-1]+1
print(dp[n])