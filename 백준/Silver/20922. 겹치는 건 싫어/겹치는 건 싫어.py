n,k=map(int,input().split())
a=list(map(int,input().split()))

n_ai=[k]*100001
result=1

start,now=0,0
while now!=n:
    temp=a[now]
    n_ai[temp]-=1
    if n_ai[temp]<0:
        result=max(result,now-start)
        n_ai[a[start]]+=1
        n_ai[temp]+=1
        start+=1
        # now=start
    else:
        now+=1
print(max(result,now-start))