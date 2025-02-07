from collections import deque
dxs,dys=[-1,0,1,0],[0,1,0,-1]

T=int(input())
def in_range(y,x): #행,열 순
    return 0<=x and x<M and 0<=y and y<N

def bfs(si,ei):
    q=deque([(si,ei)])
    grid[si][ei]=0
    while q:
        i,j=q.popleft()
        for dx,dy in zip(dxs,dys):
            ni,nj=i+dx,j+dy
            if in_range(ni,nj) and grid[ni][nj]==1:
                q.append((ni,nj))
                grid[ni][nj]=0

for test in range(T):
    result=0
    M,N,K=map(int,input().split())
    grid=[[0]*M for _ in range(N)]
    for _ in range(K):
        j,i=map(int,input().split())
        grid[i][j]=1

    for i in range(N):
        for j in range(M):
            if grid[i][j]==1:
                result+=1
                bfs(i,j)
    print(result)

