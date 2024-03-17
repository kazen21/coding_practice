
targets = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]
result = 3

def solution(targets):
    answer = 1 #요격미사일 첫번째 값을 초기값으로 했으므로 1

    targets.sort(key=lambda x:x[1])
    pos = targets[0] #요격 미사일 첫번째

    for t in targets:
        if pos[1] <= t[0]: #요격미사일 위치는 폭격미사일 끝점보다 다음 값 시작값이 크면 새로 추가
            answer += 1
            pos[1] = t[1]

    return answer

print(solution(targets))