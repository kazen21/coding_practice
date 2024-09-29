

from collections import deque
import sys
input = sys.stdin.readline

def solve(n, k):
    ans = 0
    MAX = 10**5 + 1
    visited = [0] * (MAX)

    def bfs(x):
        q = deque()
        q.append(x)

        while q:
            cur = q.popleft()
            if cur == k:
                return visited[cur]

            for next in [cur+1, cur-1, cur*2]:
                if 0<= next <MAX and visited[next] == 0:
                    visited[next] = visited[cur] + 1
                    q.append(next)

    ans = bfs(n)
    return ans


n, k = map(int, input().strip().split())
# n = 5
# k = 17

print(solve(n, k))