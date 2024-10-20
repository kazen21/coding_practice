

from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def input_data(n):
    data = []
    for _ in range(n-1):
        a, b = map(int, input().strip().split())
        data.append([a,b])

    return data

def solve():
    n = int(input().strip())
    # n = 7

    in_data = input_data(n)
    # print(in_data)
    # in_data = [[1, 6], [6, 3], [3, 5], [4, 1], [2, 4], [4, 7]]
    graph = defaultdict(list)
    for a, b in in_data:
        graph[a].append(b)
        graph[b].append(a)

    # print(graph)
    parents = [ i for i in range(n+1)]
    visited = defaultdict(int)
    def dfs(v):
        visited[v] = 1
        for next in graph[v]:
            if next not in visited:
                parents[next] = v #루트 노드부터 내려가면서 부모노드를 넣어준다.
                dfs(next)
    dfs(1)
    # print(visited)
    # print(parents)

    for i in range(2, n+1):
        print(parents[i])

solve()