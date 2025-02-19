n=int(input())
score1,score2=0,0
record=[]
for i in range(n):
    t,time=input().split()
    mm,ss=map(int,time.split(':'))
    time=mm*60+ss
    if t=='1':
        score1+=1
    else:
        score2+=1

    if score1>score2:
        record.append((time,1))
    elif score2>score1:
        record.append((time,2))
    else:
        record.append((time,0))

winTime={1:0,2:0}
for i,(s,t) in enumerate(record):
    if t==0:
        continue
    if i==n-1 and s!=0:
        winTime[t]+=(48*60)-s
    else:
        winTime[t]+=record[i+1][0]-s

mm1,ss1=divmod(winTime[1], 60)
mm2,ss2=divmod(winTime[2], 60)

# mm1= '0'+str(mm1) if mm1<=9 else mm1
# ss1= '0'+str(ss1) if ss1<=9 else ss1
# mm2= '0'+str(mm2) if mm2<=9 else mm2
# ss2= '0'+str(ss2) if ss2<=9 else ss2

print(f'{mm1:02d}:{ss1:02d}')
print(f'{mm2:02d}:{ss2:02d}')