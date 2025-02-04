money=int(input())
MD=list(map(int,input().split()))
J,S=[money,0],[money,0]

for day,i in enumerate(MD):

    #준현이 거래
    if J[0]>0:
        n,remain=J[0]//i,J[0]%i
        if n>0:
            J[0]=remain
            J[1]+=n
    
    #성민이 거래
    if day>1:
        if S[1]>0 and i>MD[day-1] and MD[day-1]>MD[day-2] and MD[day-2]>MD[day-3]:#3일째 상승
            S[0]+=S[1]*i
            S[1]=0

        elif S[0]>0 and i<MD[day-1] and MD[day-1]<MD[day-2] and MD[day-2]<MD[day-3]:#3일째 하락
            n,remain=S[0]//i,S[0]%i
            if n>0:
                S[0]=remain
                S[1]+=n

f_S=S[0]+S[1]*MD[-1]
f_J=J[0]+J[1]*MD[-1]

if f_S>f_J:
    print('TIMING')
elif f_S==f_J:
    print('SAMESAME')
else:
    print("BNP")