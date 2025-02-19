n=int(input())
n5,res=divmod(n,5)
result=-1
for i in range(n5,-1,-1):
    temp=n-(i*5)
    if temp%2!=0:
        continue
    else:
        result=i+(temp//2)
        break
print(result)