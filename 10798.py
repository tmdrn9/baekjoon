li=[]
for i in range(5):
    li.append(tuple(input()))
for i in range(15):
    for j in range(5):
        if i>=len(li[j]):
            continue
        else:
            print(li[j][i],end='')