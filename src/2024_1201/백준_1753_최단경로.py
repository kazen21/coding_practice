

from collections import defaultdict
from heapq import heappush, heappop
import sys
input = sys.stdin.readline
INF = sys.maxsize

def solve():
    V, E = map(int, input().strip().split(' '))
    K = int(input().strip())


    distance = [ INF for _ in range(V + 1)]
    graph = defaultdict(list)
    
    for _ in range(E):
        v1, v2, cost = map(int, input().strip().split(' '))
        graph[v1].append([v2, cost])

    distance[K] = 0
    hq = []
    heappush(hq, [0, K])

    while hq:
        cost, cur_v = heappop(hq)

        if distance[cur_v] < cost:
            continue

        for next_v, cost in graph[cur_v]:
            if distance[cur_v] + cost < distance[next_v]:
                distance[next_v] = distance[cur_v] + cost
                heappush(hq, [distance[next_v], next_v])

    for node in range(1, V + 1):
        if distance[node] == INF:
            print('INF')
        else:
            print(distance[node])


solve()