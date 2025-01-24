N,M= map(int,input().split())
no_see=set()
no_listen=set()
for i in range(N):
    no_listen.add(input())
for i in range(M):
    no_see.add(input())

result=sorted(list(no_see & no_listen))
print(len(result))
for i in result:
    print(i)