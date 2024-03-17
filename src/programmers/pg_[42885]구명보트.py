
# people = [70, 50, 80, 50]
people = [70, 80, 50]
limit = 100

def solution(people, limit):
    """
    하나의 보트에는 2명까지 탈수 있고
    가장 무거운 사람 + 가장 가벼운 사람 이 limit를 초과하면
    가장 무거운 사람 혼자 타야 한다

    1. 무게로 정렬
    2. 가장 가벼운 사람 + 가장 무거운 사람
    3. limit 를 초과하면 가장 무거운 사람을 보트에 태운다.
    """

    answer = 0
    people.sort()

    lt = 0
    rt = len(people) - 1

    while lt < rt:
        if people[lt] + people[rt] > limit:
            rt -= 1
            answer += 1
        else:
            lt += 1
            rt -= 1
            answer += 1

    if lt == rt:
        answer += 1

    return answer

print(solution(people, limit))