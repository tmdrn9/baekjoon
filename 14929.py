n=int(input())
xi=list(map(int,input().split()))
prefixSum =[0]*(n-1)
prefixSum[n-1]=xi[n-1]
for i in range(n-2,-1,-1):
    prefixSum[i]=prefixSum[i+1]+(xi[i]*xi[i+1])
print(prefixSum[0])