original=input()
polyomino=original.split('.')
A='AAAA'
B='BB'
def replace_polyomino():
    result=[]
    for i,p in enumerate(polyomino):
        if 'X' in p:
            length=len(p)
            if length%2==1:
                return -1
            else:
                a,b=divmod(length,4)
                b=b//2
                result.append(A * a + B * b)
        result+='.'
    return result[:-1]

if 'X' not in original:
    print(original)
else:
    result=replace_polyomino()
    print(''.join(result) if result != -1 else -1)