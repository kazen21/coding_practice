

def solve():

    N = int(input())

    answer = 0

    v1 = [0] * N
    v2 = [0] * (2 * N)
    v3 = [0] * (2 * N)

    def dfs(L):
        nonlocal answer
        if L == N:
            answer += 1
            return
        for j in range(N):
            if v1[j] == v2[L - j] == v3[L + j] == 0:
                v1[j] = v2[L - j] = v3[L + j] = 1
                dfs(L + 1)
                v1[j] = v2[L - j] = v3[L + j] = 0

    dfs(0)

    print(answer)

solve()