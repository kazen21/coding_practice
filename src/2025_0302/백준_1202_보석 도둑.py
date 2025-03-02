
import sys
import heapq

input = sys.stdin.readline

def solve():

    n, k = map(int, input().split())

    jewels = []
    for _ in range(n):
        m, v = map(int, input().split())
        jewels.append((m,v))

    bags = []
    for _ in range(k):
        bag_weight = int(input())
        bags.append(bag_weight)

    jewels.sort(key=lambda x: x[0])
    bags.sort()

    answer = 0
    heap = []

    pos = 0

    for bag in bags:
        # 현재 가방에 담을 수 있는 보석들을 최대 힙에 추가
        while pos < n and jewels[pos][0] <= bag:
            # heapq는 최소 힙이므로, 최대값을 사용하기 위해 가격의 음수를 넣음
            heapq.heappush(heap, -jewels[pos][1])
            pos += 1
        # 현재 가방에 담을 수 있는 보석 중 가장 높은 가격의 보석을 선택
        if heap:
            answer -= heapq.heappop(heap)

    print(answer)


if __name__ == '__main__':
    solve()