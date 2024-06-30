
import sys
sys.setrecursionlimit(10**6)
INF = sys.maxsize
from collections import defaultdict
def solution(n, lighthouse):
    answer = INF
    #dp[v][0] : 노드 v가 off 인 경우에 등대 갯수의 최소값
    #dp[v][1] : 노드 v가 on 인 경우에 등대 갯수의 갯소값

    #노드 번호가 1부터 시작이므로 0 부터 시작으로 변경
    dp = [[INF,INF] for _ in range(n)]
    graph = defaultdict(list)

    #노드 번호가 1부터 시작이므로 0 부터 시작으로 변경
    for v1, v2 in lighthouse:
        graph[v1-1].append(v2-1)
        graph[v2-1].append(v1-1)

    visited = [False] * (n)

    def dfs(v):
        visited[v] = True
        dp[v][0] = 0 #노드 v가 off이므로 등대갯수는 0부터 시작
        dp[v][1] = 1 #노드 v가 on이므로 등대갯수는 1부터 시작

        for node in graph[v]:
            if visited[node] == False:
                dfs(node)
                dp[v][0] += dp[node][1]
                dp[v][1] += min(dp[node][0], dp[node][1])
        return dp[v]
    ret = dfs(0) # 노드 번호 0 부터 시작
    answer = min(answer, ret[0], ret[1])
    return answer

n = 8
lighthouse = [[1, 2], [1, 3], [1, 4], [1, 5], [5, 6], [5, 7], [5, 8]]
# result = 2
print(solution(n, lighthouse))