from collections import deque

n,m=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(n)]

dxs,dys=[-1,0,1,0],[0,1,0,-1]
def can_go(x,y):
    return 0<=x<n and 0<=y<m and grid[x][y]!=0

def bfs(startx,starty):
    q=deque([(startx,starty)])
    distance[startx][starty]=0
    while q:
        x,y=q.popleft()
        for dx,dy in zip(dxs,dys):
            nx,ny=x+dx,y+dy
            if can_go(nx,ny) and distance[nx][ny]==-1:
                distance[nx][ny]=distance[x][y]+1
                q.append((nx,ny))
    return distance

distance=[[-1]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if grid[i][j]==1 and distance[i][j]==-1:
            distance[i][j]=-1
        elif grid[i][j]==0:
            distance[i][j]=0
        elif grid[i][j]==2:
            endx,endy=i,j

result= bfs(endx,endy)
for row in result:
    print(*row)