def solution(people, limit):
    answer = 0
    people.sort()
    left, right = 0, len(people) - 1
    
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1  # 가장 가벼운 사람도 보트에 태운다
        right -= 1  # 가장 무거운 사람을 태운다
        answer += 1  # 한 명 혹은 두 명을 태운다
    return answer