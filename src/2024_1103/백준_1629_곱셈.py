
#코데풀님 코드 참고했습니다.
import sys
input = sys.stdin.readline

def solve():
    A, B, C = map(int, input().strip().split())
    # A, B, C = 10, 11, 12
    v = mypower(A, B, C)
    answer = v % C
    return answer

def mypower(A, b, C):
    if b == 1:
        return A % C

    quotient = b // 2
    v = mypower(A, quotient, C)

    if b % 2 == 0:
        v = (v * v) % C
    else:
        v = (v * v * A) % C

    return v

print(solve())