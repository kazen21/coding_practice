

import sys
INF = sys.maxsize

def solution(a):
    answer = 0
    n = len(a)

    if n == 1:
        return 1
    if n == 2:
        return 2

    answer = 2 # 0, n-1 은 살아남을 수 있음

    dp_left = [ INF for _ in range(n)]
    dp_right = [INF for _ in range(n)]
    dp_left[0] = a[0]
    dp_right[n-1] = a[-1]

    #왼쪽 최소값 갱신
    for i in range(1, n):
        dp_left[i] = min(dp_left[i - 1], a[i])
    #오른쪽 최소값 갱신
    for i in range(n - 2, -1, -1):
        dp_right[i] = min(dp_right[i + 1], a[i])

    # 1번부터 n-2 까지만 비교, 0 과 n-1 은 생존 가능
    for i in range(1, n - 1):
        # 작은 풍선은 1번만 할 수 있으므로 a[i]가 양쪽 값보다 보다 크다면 살아 남을수 없다
        if a[i] > max(dp_left[i - 1], dp_right[i + 1]):
            continue
        else:
            answer += 1

    return answer


a = [-16,27,65,-2,58,-92,-71,-68,-61,-33]
# result = 6
print(solution(a))



