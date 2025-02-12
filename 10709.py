
r,c=map(int,input().split())
joi=[list(input()) for _ in range(r)]
result=[[-1]*c for _ in range(r)]

for i,rr in enumerate(joi):
    time=0
    on=0
    for j, cc in enumerate(rr):
        if cc=='c':
            on=1
            result[i][j]=0
            time=1
        elif on and cc=='.':
            result[i][j]=time
            time+=1

for rr in result:
    for cc in rr:
        print(cc, end=' ')
    print()