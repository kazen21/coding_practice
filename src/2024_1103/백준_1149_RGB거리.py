
INF = 1e9
def solve():

    num = int(input())
    # num = 3
    # print(f"num={num}")

    in_data = []
    for _ in range(num):
        a = list(map(int, input().split()))
        in_data.append(a)

    # in_data = [[26, 40, 83], [49, 60, 57], [13, 89, 99]]
    # print(in_data)

    n = len(in_data)
    m = len(in_data[0])

    #dp[i][j] : i번째 집까지 j색(빨강,초록,파랑)을 칠하는 비용의 최소값의 합
    dp = [[INF]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            dp[i][j] = in_data[i][j]

    for i in range(1, n):
        for j in range(m):
            # 이전 집 과 현재 집의 색이 같지 않아야 하므로, 동일한 색상의 값은 제외하고 계산한다.
            dp[i][j] += min(dp[i-1][:j] + dp[i-1][j+1:])

    # print(dp)
    answer = min(dp[-1])
    return answer

print(solve())



