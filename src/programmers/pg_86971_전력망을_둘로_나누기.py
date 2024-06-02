from collections import defaultdict
def solution(n, wires):
    answer = float('inf')
    graph = defaultdict(list)

    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)

    print(graph)
    L_cnt = 0
    def dfs(v):
        nonlocal L_cnt
        visited[v] = 1
        L_cnt += 1
        for v2 in graph[v]:
            if visited[v2] == 0:
                dfs(v2)
    for v1, v2 in wires:

        visited = [0]*(n+1)
        visited[v2] = 1
        L_cnt = 0
        dfs(v1)

        # print(L_cnt)
        answer = min(answer, abs(L_cnt - (n-L_cnt)))
    return answer

n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]

print(solution(n, wires))