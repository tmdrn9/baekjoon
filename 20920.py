# N,M=map(int,input().split())
# #빈도/단어길이/단어
# dict={}
# for _ in range(N):
#     temp=input()
#     if len(temp)<M:
#         continue
#     if temp in dict.keys():
#         dict[temp]+=1
#     else:
#         dict[temp]=1

# for v,_ in sorted(dict.items(),key=lambda x:(-x[1],-len(x[0]),x[0])):
#     print(v)

# import sys
# from collections import Counter
# N,M=map(int,input().split())
# #빈도/단어길이/단어
# total=[]
# for _ in range(N):
#     temp=sys.stdin.readline().rstrip() #input함수보다 훨씬 빠름
#     if len(temp)>=M:
#         total.append(temp)
# cnt=Counter(total)
# word=sorted(cnt)
# word=sorted(word,key=len,reverse=True)
# word=sorted(word,key=cnt.get,reverse=True)

# for w in word:
#     print(w)

import sys
from collections import Counter
N,M=map(int,input().split())
#빈도/단어길이/단어
total=[]
for _ in range(N):
    temp=sys.stdin.readline().rstrip()
    if len(temp)<M:
        continue
    total.append(temp)
cnt=Counter(total)
for word,_ in sorted(cnt.items(),key=lambda x:(-x[1],-len(x[0]),x[0])):
    print(word)