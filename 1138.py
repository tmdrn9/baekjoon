n=int(input())
tall_i=list(map(int,input().split()))
line=[n+1]*n

for i,t_i in enumerate(tall_i):
    if i==0:
        line[t_i]=i+1
    else:
        turn=0
        low_cnt=0
        k=t_i+1
        while turn<k:
            if line[turn]<i+1:
                low_cnt+=1
                k+=1
            turn+=1
        line[t_i+low_cnt]=i+1

print(*line)