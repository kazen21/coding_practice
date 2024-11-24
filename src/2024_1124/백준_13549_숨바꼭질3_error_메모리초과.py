
from collections import deque
import sys

input = sys.stdin.readline

MAX = 100000+1

visited = [True]*(MAX+1)

def solve():

    N, K = map(int, input().strip().split())

    q = deque()
    q.append([N, 0]) #수빈 현재위치, 시간


    maps = [sys.maxsize for _ in range(MAX)]

    while q:

        cur, time = q.popleft()

        if time < maps[cur]:
            maps[cur] = time
            if cur == K :
                print(time)
                return

        for next in [cur*2, cur-1, cur+1]:
            if 0<= next <= MAX :#and visited[next] == False:
                if next == cur*2:
                    q.append([next, time])
                else:
                    q.append([next, time+1])

solve()
