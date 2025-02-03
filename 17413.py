import sys
S=sys.stdin.readline().rstrip()
result=''
start=0
stop=-1
stop_end=-1
temp=False 
for i,a in enumerate(S):
    if a =='<':
        if start<i:
            result+=S[start:i][::-1]
        stop=i    
    elif a=='>':
        result+=S[stop:i+1]
        stop_end=i
        start=i+1
    elif a ==' ':
        if stop>stop_end:
            continue
        else:
            result+=S[start:i][::-1]+' '
            start=i+1

    elif i==len(S)-1:
        result+=S[start:i+1][::-1]+' '
        start=i+1
    else:
        continue
print(result)