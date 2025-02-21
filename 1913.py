n = int(input())
k = int(input())
grid =[[0]*n for _ in range(n)]
dx,dy=[-1,0,1,0],[0,1,0,-1]

cnt=1 #grid 채워넣는 값
i,j=n//2,n//2 #시작 위치
grid[i][j]=cnt #시작 위치에 1삽입
d=0 #방향 인덱스
twice=0 #2가 되면 loop+1(방향을 두번 바꿨을때마다 동일한 방향으로 나아가는 길이가 +1됨)
loop=1 #같은 방향으로 이동하는 거리
answeri,answerj=(n//2)+1,(n//2)+1 #k==1일때로 초기화
end=True
while end:
    for _ in range(loop):
        ni,nj=i+dx[d],j+dy[d]
        if ni<0 or nj<0:
            end=False
            break
        cnt+=1
        grid[ni][nj]=cnt
        i,j=ni,nj
        if cnt==k:
            answeri,answerj=i+1,j+1
    d=(d+1)%4
    twice+=1
    if twice==2:
        loop+=1
        twice=0

for row in grid:
    for a in row:
        print(a, end=' ')
    print()
print(answeri, answerj)