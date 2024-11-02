

def solve():
    num = int(input())
    in_data = []
    for i in range(num):
        a = list(map(int, input().split()))
        in_data.append(a)

    # in_data = [[7],[3, 8], [8,1,0],[2,7,4,4],[4,5,2,6,5]]

    n = len(in_data)
    m = len(in_data[-1])

    #dp[i][j] : i행 j열에서 i-1행의 대각선방향의 큰 값과 현재값의 합의 최대값
    dp = [[0]*m for _ in range(n)]

    dp[0][0] = in_data[0][0]

    for i in range(1, n):
        for j in range(i+1):
            #위줄의 대각선 왼쪽, 오른쪽 값중 큰 값 선택)
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + in_data[i][j]

    answer = max(dp[-1])
    return answer

print(solve())