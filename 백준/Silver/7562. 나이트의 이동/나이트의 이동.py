from collections import deque
dxs,dys=[1,2,2,1,-1,-2,-2,-1],[-2,-1,1,2,-2,-1,1,2]

def in_range(x,y):
    return 0<=x<l and 0<=y<l

def bfs(l,startx,starty,endx,endy):
    visited=[[0]*l for _ in range(l)]
    dq=deque([(startx,starty)])
    visited[startx][starty]=1
    while dq:
        x,y=dq.popleft()
        for dx,dy in zip(dxs,dys):
            nx,ny=x+dx,y+dy
            if in_range(nx,ny) and visited[nx][ny]==0:
                dq.append((nx,ny))
                visited[nx][ny]=visited[x][y]+1
                if (nx,ny)==(endx,endy):
                    return visited[nx][ny]-1

n_test=int(input())
for test in range(n_test):
    l=int(input())
    startx,starty=map(int,input().split())
    endx,endy=map(int,input().split())
    if (startx,starty)==(endx,endy):
        print('0')
    else:
        print(bfs(l,startx,starty,endx,endy))
