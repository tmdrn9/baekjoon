N=int(input())
files=[]
for i in range(N):
    files.append(input())

result={}

for i in files:
    temp=i.split('.')[1]
    if temp in result:
        result[temp]+=1
    else:
        result[temp]=1

for i,c in sorted(result.items()):
    print(i, c)