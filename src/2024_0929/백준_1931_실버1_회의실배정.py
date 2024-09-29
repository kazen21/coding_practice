
import sys

input = sys.stdin.readline

def solve(n, data):

    sort_data = sorted(data, key=lambda x : (x[1], x[0]))
    last_time = 0
    count = 0
    for start, end in sort_data:
        if start >= last_time:
            last_time = end
            count += 1

    return count

# 11
# 1 4
# 3 5
# 0 6
# 5 7
# 3 8
# 5 9
# 6 10
# 8 11
# 8 12
# 2 13
# 12 14

n = int(input().strip())
data = []
for _ in range(n):
    s, e = map(int, input().strip().split())
    data.append((s,e))

print(solve(n, data))