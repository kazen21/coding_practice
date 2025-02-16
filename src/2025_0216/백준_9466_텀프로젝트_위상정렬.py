import sys
from collections import deque
from collections import defaultdict

input = sys.stdin.readline
def solve():
    T = int(input().strip())
    # T = 1
    for _ in range(T):
        N = int(input().strip())
        # N= 7
        arr = [0] + list(map(int, input().strip().split()))
        # arr = [0, 3, 1, 3, 7, 3, 4, 6]
        # print(f"arr={arr}")

        edges = defaultdict(list)
        in_degree = [0] * (N+1) #진입차수

        for i in range(1, N+1):
            edges[i].append(arr[i])
            in_degree[arr[i]] += 1

        queue = deque()

        for i in range(1, N + 1):
            if in_degree[i] == 0:
                queue.append(i)

        while queue:
            fr = queue.popleft()

            for to in edges[fr]:
                in_degree[to] -= 1
                if in_degree[to] == 0:
                    queue.append(to)

        cycle_count = sum(1 for i in range(1, N+1) if in_degree[i] > 0) #사이클이 남아있는 노드는 1로 설정

        print(N - cycle_count) # 프로젝트 팀에 속하지 못한 학생 : 전체노드 - 사이클노드

if __name__ == '__main__':
    solve()

