import sys

S=sys.stdin.readline().rstrip()
a_cnt=S.count('a')
S+=S[0:a_cnt-1]
result=100000000

for i in range(len(S)-a_cnt+1):
    result=min(result,S[i:i+a_cnt].count('b'))
print(result)