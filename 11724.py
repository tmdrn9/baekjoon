import sys
from collections import deque
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

# def bfs(start):
#     q=deque([start])
#     visited[start]=1
#     while q:
#         node=q.popleft()
#         for new in graph[node]:
#             if not visited[new]:
#                 q.append(new)
#                 visited[new]=1

cnt=0
for i in range(1,N+1):
    if not visited[i]:
        bfs(i)
        #dfs(i)
        cnt+=1
print(cnt)