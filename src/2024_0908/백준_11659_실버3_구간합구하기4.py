
# import sys
# input = sys.stdin.readline
# n, m = map(int, input().strip().split())
# data = list(map(int, input().strip().split()))
# # n, m=(5, 3)
# # data = [5, 4, 3, 2, 1]
#
# # print(f"n, m={n, m}")
# # print(f"data = {data}")
#
# for _ in range(m):
#     i, j = map(int, input().strip().split())
#     answer = sum(data[i-1:j])
#     print(answer)
#####################################################

# 누적합 문제
import sys
input = sys.stdin.readline
n, m = map(int, input().strip().split())
data = list(map(int, input().strip().split()))
# n, m=(5, 3)
# data = [5, 4, 3, 2, 1]

# print(f"n, m={n, m}")
# print(f"data = {data}")

prefixSum = [0]
sum = 0

for i in range(n):
    sum += data[i]
    prefixSum.append(sum)


for _ in range(m):
    i, j = map(int, input().strip().split())
    answer = prefixSum[j] - prefixSum[i-1]
    print(answer)


# input
# 5 3
# 5 4 3 2 1
# 1 3
# 2 4
# 5 5

# output
# 12
# 9
# 1