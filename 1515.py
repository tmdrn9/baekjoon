import sys

n=sys.stdin.readline().rstrip()
cnt=0

while len(n)>0:
    cnt+=1
    result=str(cnt)
    while result and n:
        if result[0]==n[0]:
            n=n[1:]
        result=result[1:]
print(cnt)