
routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]

# result = 2

def solution(routes):
    answer = 1 #pos 첫번째 값을 넣었으므로 카메라 한대는 이미 설치됨

    routes.sort(key=lambda x:x[1]) # 진출 지점 기준으로 정렬

    pos = routes[0]

    for r in routes:
        if pos[1] < r[0]: #이전 진출지점보다 다음 전입지점이 더 크면 카메라 설치가 필요하다
            answer += 1
            pos[1] = r[1]

    return answer

print(solution(routes))
