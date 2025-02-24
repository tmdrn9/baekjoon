from collections import deque
p,m=map(int, input().split())
room=[]
for i in range(p):
    level,name=input().split()
    level=int(level)
    if i==0:
        room.append([(level,name)])
    else:
        roomIn=False
        for i,r in enumerate(room): # 매칭 가능한 방 탐색
            if len(r)==m: #정원이 다 찬 방이면 패스
                continue
            first_l,_=r[0]
            if first_l-10<=level<=first_l+10: #처음 입장 플레이어의 레벨을 기준으로 -10부터 +10까지 입장 가능
                room[i].append((level,name))
                roomIn=True
                break
        if roomIn==False: ## 방 없다면 새로운 방을 생성하고 입장
            room.append([(level,name)])

for r in room:
    if len(r)==m:
        print('Started!')
    else:
        print('Waiting!')
    r.sort(key=lambda x:x[1])
    for level,name in r:
        print(level,name)