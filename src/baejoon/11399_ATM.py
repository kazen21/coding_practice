

# from itertools import permutations
import sys

input = sys.stdin.readline

n = int(input().strip())
p = list(map(int, input().strip().split()))


# INF = 1e9
# ans = INF
# for perm in permutations(range(n)):
#     # print(perm)
#     ret = 0
#     total = 0
#     for i in perm:
#         ret += p[i]
#         total += ret
#
#     ans = min(ans, total)

p.sort()
time = 0
total = 0
for i in range(n):
    time += p[i]
    total += time

print(total)



