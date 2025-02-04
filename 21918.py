N,M=map(int,input().split())
bulb=list(map(int,input().split()))

for i in range(M):
    m,l,r=map(int,input().split())
    if m==2:
        for j in range(l-1,r):
            bulb[j]= 1 if bulb[j]==0 else 0
    elif m==3:
        for j in range(l-1,r):
            bulb[j]= 0

    elif m==4:
        for j in range(l-1,r):
            bulb[j]= 1
    else:
        bulb[l-1]=r

for b in bulb:
    print(b,end=' ')