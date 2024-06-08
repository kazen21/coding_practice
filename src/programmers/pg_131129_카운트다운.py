
import sys

INF = sys.maxsize

def solution(target):
    # answer = []
    table = create_table() # 다트로 쏠수 있는 점수를 미리 기록

    #dp[target][0] : target을 맞추기 위해 던진 최소의 다트 수
    #dp[target][1] : target을 맞추기 위해 맞춘 싱글 or 불 맞춘 횟수

    dp = [ [INF, 0] for _ in range(target+1)]

    dp[0][0] = 0
    dp[0][1] = 0

    for cur_target in range(1, target+1):
        for kind in range(2):
            for idx in range(len(table[kind])):
                prev_target = cur_target - table[kind][idx]
                if prev_target < 0:
                    continue
                # 이전 타켓에서 횟수 1증가, kind 0(싱글,불) 일때 1증가, kind 1 일때(더블,트리블) 증가 없음
                total_count, single_bull = dp[prev_target][0] + 1, dp[prev_target][1] + 1 - kind

                # 최소 던진 횟수
                if total_count < dp[cur_target][0]:
                    dp[cur_target] = [total_count, single_bull]

                # 던진 횟수가 같다면 싱글, 불을 최대한 많이 던지는 방법
                elif total_count == dp[cur_target][0]:
                    dp[cur_target] = [total_count, max(dp[cur_target][1], single_bull)]

    # print(dp)
    return dp[target]

def create_table():
    # 다트로 쏠수 있는 점수를 미리 기록
    total = []

    #싱글, 불
    arr1 = []
    #싱글
    for i in range(1, 21):
        arr1.append(i)

    #불
    arr1.append(50)

    # 더블, 트리블
    arr2 = []
    for i in range(1, 21):
        for j in range(2, 4):
            ret = i*j
            if ret > 20:
                arr2.append(ret)

    # 중복점수가 있으면 제거
    arr1 = list(set(arr1))
    arr2 = list(set(arr2))

    #싱글, 불의 횟수의 합을 구해야 하므로 싱글 불 과, 더블 트리플을 따로 저장한다.
    total.append(arr1)
    total.append(arr2)

    return total

target = 21
print(solution(target))