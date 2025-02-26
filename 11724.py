import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
N,M=map(int,input().split())
graph=[[] for _ in range(N+1)]
for _ in range(M):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

visited=[0]*(N+1)

def dfs(start):
    visited[start]=1
    for new in graph[start]:
        if not visited[new]:
            dfs(new)

cnt=0
for i in range(1,N+1):
    if not visited[i]:
        dfs(i)
        cnt+=1
print(cnt)