n,m=map(int,input().split())
matrix=[list(map(int,input().split())) for _ in range(n)]
dp=[[0]*m for _ in range(n)]

t=int(input())

for _ in range(t):
    i,j,x,y=map(int,input().split())
    if i==x and j==y:
        print(matrix[i-1][j-1])
    else:
        s=0
        for ii in range(i-1,x):
            s+=sum(matrix[ii][j-1:y])
        print(s)