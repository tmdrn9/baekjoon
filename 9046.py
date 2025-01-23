n=int(input())
for i in range(n):
    cnt=[]
    s=input()
    alpha=set(s)
    if ' ' in alpha:
        alpha.remove(' ')
    for aa in alpha:
        cnt.append((aa,s.count(aa)))
    cnt.sort(key=lambda x:-x[1])
    if len(cnt)>=2 and cnt[0][1]==cnt[1][1]:
        print('?')
    else:
        print(cnt[0][0])