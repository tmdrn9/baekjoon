N,K= map(int,input().split())
value=[]
for i in range(N):
    w,v=map(int,input().split())
    vw=v/w
    value.append((vw,v,w))
value.sort()
print(value)
result=0
now=K
for j in range(N-1,-1):
    vw,v,w=value.pop(j)
    if now<=0:
        break
    if now>=w:
        result+=v
        now-=w
print(result)