#11:30 시작
def solution(people, limit):
    answer = 0
    people=sorted(people)
    while people:
        one=people.pop(-1)
        remain=limit-one
        temp=[two for two in people if two<=remain]
        if temp:
            people.remove(max(temp))
        answer+=1
    return answer