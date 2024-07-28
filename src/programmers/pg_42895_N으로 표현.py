

def solution(N, number):
    dp = [ set() for _ in range(9)] #

    for i in range(1, 9):
        case = dp[i] #N을 i 갯수만큼 사용해 계산한 값을 저장

        case.add(int(str(N)*i))

        # dp[3] :
          # - dp[1] 와 dp[2] 사칙연산 값 저장
          # - dp[2] 와 dp[1] 차사칙연산 값 저장

        for j in range(1, i):
            for k in dp[j]:
                for l in dp[i-j]:
                    case.add(k+l)
                    case.add(k-l)
                    case.add(k*l)
                    if l != 0:
                        case.add(k//l)

        if number in case:
            return i #case 안에 N이 들어있으면 i 가 사용횟수의 최소값이 된다.

    return -1


N = 5
number = 12
# return = 4

print(solution(N, number))