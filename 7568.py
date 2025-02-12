import sys
from collections import deque
N=int(input())
people=deque([tuple(map(int,input().split())) for _ in range(N)])
result=[1]*N
for i in range(N):
    x,y=people.popleft()
    for nx,ny in people:
        if x<nx and y<ny:
            result[i]+=1
    people.append((x,y))

for r in result:
    print(r, end=' ')