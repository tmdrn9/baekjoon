from collections import deque
n=int(input())
x,y=map(int,input().split()) #촌수를 계산해야 하는 서로 다른 두 사람의 번호
chon=[[] for _ in range(n+1)]
m=int(input())
for _ in range(m):
    xx,yy=map(int,input().split())
    chon[xx].append(yy)
    chon[yy].append(xx)
visited=[0]*(n+1)
res=[0]*(n+1)

def bfs():
    q=deque([x])
    visited[x]=1
    while q:
        p=q.popleft() #i가 부모
        for i in chon[p]:
            if visited[i]==0:
                visited[i]=1
                q.append(i)
                res[i]=res[p]+1

bfs()
if res[y]<1:
    print(-1)
else:
    print(res[y])