
import sys
input = sys.stdin.readline
def solve():

    n = int(input().strip())
    # n = 6
    a = list(map(int, input().strip().split()))
    # a = [10, 20, 10, 30, 20, 50]
    dp = [0]*n

    for i in range(n):
        dp[i] = 1
        for j in range(i):
            if a[j] < a[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
    # print(dp)
    print(max(dp))

solve()