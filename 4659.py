#Pass=>True

def aeiou(s):
    return s=='a' or s=='e' or s=='i' or s=='o' or s=='u'

def is_aeiou(st):
    result=st.find('a')!=-1 or st.find('e')!=-1 or st.find('i') !=-1 or st.find('o') !=-1 or st.find('u')!=-1
    return result


def two(st):
    N=len(st)
    if N==1:
        return True
    for i in range(N-1):
        if st[i]==st[i+1] and st[i]!='e' and st[i]!='o':
            return False
    return True

def three_type(st):
    N=len(st)
    if N<3:
        return True
    
    for i in range(N-2):
        if aeiou(st[i]) ==aeiou(st[i+1]) ==aeiou(st[i+2]):
            return False
    return True

while True:
    ss=input()
    if ss=='end':
        break
    if (is_aeiou(ss) and two(ss) and three_type(ss))==True:
        print(f'<{ss}> is acceptable.')
    else:
        print(f'<{ss}> is not acceptable.')