from collections import deque
dxs,dys=[-1,0,1,0],[0,1,0,-1]
n,m=map(int,input().split())

grid=[[0]*m for _ in range(n)]
for i in range(n):
    for j,k in enumerate(input()):
        grid[i][j]=int(k)

def can_go(x,y):
    return 0<=x<n and 0<=y<m and grid[x][y]==1

distance=[[0]*m for _ in range(n)]

def bfs():
    q=deque([(0,0)])
    distance[0][0]=1
    while q: #deque는 비어있을 때 False로 평가
        x,y=q.popleft()
        for dx,dy in zip(dxs,dys):
            nx,ny=x+dx,y+dy
            if can_go(nx,ny) and distance[nx][ny]==0:
                q.append((nx,ny))
                distance[nx][ny]=distance[x][y] + 1
    return distance[n-1][m-1]  # 도착 지점의 최단 거리 반환

print(bfs())