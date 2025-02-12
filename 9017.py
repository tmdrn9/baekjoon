from collections import Counter
import heapq

T=int(input())

def find_myteam(t):
    result=0
    five=-1
    n_index=0
    turn=0
    while True:
        turn+=1
        temp=rank.index(t,n_index)
        if turn<=4:
            result+=score[temp]
        elif turn==5:
            five=temp+1
        else:
            return (result,five)
        n_index=temp+1

for test in range(T):
    final_score=[]
    N=int(input())
    score=[-1]*N
    rank=list(map(int,input().split()))
    n_team=Counter(rank)
    valid_team=[]

    for n,n_p in n_team.items():
        if n_p==6:
            valid_team.append(n)
    
    now_score=1
    for i in range(N):
        if rank[i] in valid_team:
            score[i]=now_score
            now_score+=1

    for n in valid_team:
        s,f=find_myteam(n)
        heapq.heappush(final_score,(s,f,n))
    _,_,winner=heapq.heappop(final_score)
    print(winner)