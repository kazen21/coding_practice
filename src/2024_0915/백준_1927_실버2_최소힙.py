from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N = int(input().strip())
heap = []
for _ in range(N):
    x = int(input().strip())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            ret = heappop(heap)
            print(ret)
    else:
        heappush(heap, x)