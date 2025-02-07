N,M=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
at,bt=0,0
result=[]
while at!=N and bt!=M:
    if A[at]<=B[bt]:
        result.append(A[at])
        at+=1
    else:
        result.append(B[bt])
        bt+=1

if at==N:
    result.extend(B[bt:])
else:
    result.extend(A[at:])

for i in result:
    print(i, end=' ')