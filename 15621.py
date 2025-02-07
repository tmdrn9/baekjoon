A=int(input())
T=int(input())
C=int(input())
#T번쩨로 C를 외치는 사람

song=[0,1,0,1,0,0,1,1]

tt=0 #C가 외쳐진 횟수
a=0 #몇번째 사람 턴인지
n=0 #몇회차 노래인지

while True:
    for ss in song:
        a+=1
        if a>A:
            a=1
        if ss==C:
            tt+=1
            if tt==T:
                break
    n+=1
    if tt==T:
        break
    song.insert(-(n+1),0)
    song.insert(-(n+1),1)   

print(a-1)