import heapq,math
from itertools import combinations
def distance(i,j):
    return abs(i[0]-j[0])+abs(i[1]-j[1])

n,k=map(int,input().split()) #n개 집, k개 대피소
home=[]
for _ in range(n):
    x,y=map(int,input().split())
    home.append((x,y))
    
nCr = combinations(home, k)
answer=[]
for daepi in nCr: #대피소 지정
    result=0
    for other in home:
        if other not in daepi: #대피소가 아닌 집들
            min_d=math.inf
            for i in daepi: #대피소가 아닌 집들과 대피소인 집 거리 계산해서
                min_d=min(min_d,distance(i,other))
            result=max(min_d,result)
    answer.append(result)
print(min(answer))