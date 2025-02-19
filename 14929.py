n=int(input())
xi=list(map(int,input().split()))
prefixSum =0
result=0
for i in range(n-1,0,-1):
    prefixSum += xi[i]
    result+=prefixSum*xi[i-1]
print(result)