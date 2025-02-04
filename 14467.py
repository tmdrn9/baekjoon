N=int(input())
result=0
cow={}

for i in range(N):
    cow_n,d=map(int,input().split())
    if cow_n in cow:
        if cow[cow_n]!=d:
            result+=1
            cow[cow_n]=d
    else:
        cow[cow_n]=d
print(result)