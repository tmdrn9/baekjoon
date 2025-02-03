#팰린드롬이란? 순서를 거꾸로 읽었을 때도 원래의 문자열이나 수열과 동일한 경우를 의미
import sys
from collections import Counter
# name=input()
name=sys.stdin.readline().rstrip()
result=''
cnt=Counter(name)
cnt=sorted(cnt.items())
odd_cnt=0

for x,c in cnt:
    if c%2==1:
        odd_cnt+=1
        odd_type=x

for xx,cc in cnt:
    result+=xx*(cc//2)

if odd_cnt==0:
    print(''.join(result+result[::-1]))
elif odd_cnt==1: 
    print(''.join(result+odd_type+result[::-1]))
else:
    print("I'm Sorry Hansoo")