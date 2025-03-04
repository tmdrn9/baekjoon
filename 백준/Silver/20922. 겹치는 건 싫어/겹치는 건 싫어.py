n, k = map(int, input().split())
a = list(map(int, input().split()))

count = [0] * 100001  # 숫자의 등장 횟수를 저장할 배열
start = 0
result = 0

for end in range(n):
    count[a[end]] += 1
    
    # k번 초과 등장하면 start 포인터를 이동시켜 해결
    while count[a[end]] > k:
        count[a[start]] -= 1
        start += 1

    result = max(result, end - start + 1)

print(result)