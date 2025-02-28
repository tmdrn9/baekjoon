import math
from itertools import combinations
def distance(i,j):
    return abs(i[0]-j[0])+abs(i[1]-j[1])

n,k=map(int,input().split()) #n개 집, k개 대피소
homes=[]
for _ in range(n):
    x,y=map(int,input().split())
    homes.append((x,y))

answer=math.inf
for daepis in combinations(homes, k): #대피소 지정
    max_d=-1
    for other in homes:
        min_d=math.inf
        if other in daepis:
            continue
        for daepi in daepis:
            dist=distance(daepi,other)
            if min_d>dist:
                min_d=dist
        if max_d<min_d:
            max_d=min_d
    answer=min(answer,max_d)
print(answer)