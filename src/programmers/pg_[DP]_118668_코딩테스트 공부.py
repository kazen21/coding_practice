def solution(alp, cop, problems):
    answer = 0
    max_alp, max_cop = 0, 0

    #모든 문제를 풀어야 하므로, 문제풀이에 필요한 최대 알고력과 코딩력을 알아야 한다.
    for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
        max_alp = max(max_alp, alp_req)
        max_cop = max(max_cop, cop_req)

    if max_alp < alp and max_cop < cop:
        return 0

    # times[알고력][코딩력] : 알고력 과 코딩력을 획득하는데 필요한 최단시간
    # 공부하면 1 높이는데 1시간 소요, 문제를 풀면 주어진 알고력, 코딩역을 올릴 수 있고, cost 만큼 시간 소요
    times = [[float('inf') for _ in range(max_cop + 1)] for _ in range(max_alp + 1)]
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)

    times[alp][cop] = 0

    for a in range(alp, max_alp + 1):
        for c in range(cop, max_cop + 1):
            # 공부해서 알고력과 코딩력을 높이는 방법 : 1을 높이기 위해 1시간 공부
            if a <= max_alp:
                times[a][c] = min(times[a][c], times[a - 1][c] + 1)
            if c <= max_cop:
                times[a][c] = min(times[a][c], times[a][c - 1] + 1)

            # 문제를 풀어서, 알고력과 코딩력을 높이는 방법
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if a >= alp_req and c >= cop_req:
                    na, nc = min(a + alp_rwd, max_alp), min(c + cop_rwd, max_cop)
                    times[na][nc] = min(times[na][nc], times[a][c] + cost)

    answer = times[-1][-1]
    return answer

alp = 10
cop = 10
problems = [[10,15,2,1,2],[20,20,3,3,4]]
# result = 15
print(solution(alp, cop, problems))