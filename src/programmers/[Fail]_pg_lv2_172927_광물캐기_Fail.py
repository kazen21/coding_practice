
from collections import defaultdict
from itertools import permutations
import sys
import copy

INF = sys.maxsize
def solution(picks, minerals):
    answer = INF
    #도구 : dia_tool, iron_tool, stone_tool
    pirodo = defaultdict(dict)

    pirodo['dia_tool'] = {'diamond':1, 'iron':1, 'stone':1}
    pirodo['iron_tool'] = {'diamond':5, 'iron':1, 'stone':1}
    pirodo['stone_tool'] = {'diamond': 25, 'iron': 5, 'stone': 1}
    # print(pirodo)
    tools = defaultdict(int)

    #각 도구의 갯수
    tools['dia_tool'] = picks[0]
    tools['iron_tool'] = picks[1]
    tools['stone_tool'] = picks[2]

    full_remove = [] # 도구의 경우의 수 중 모든 광물을 캐었을 때 저장
    part_remove = [] # 도구의 경우의 수 중 도구을 모두 사용한 경우

    #순열의 통해 임의의 도구를 선택(완전탐색)
    for perm in permutations(['dia_tool', 'iron_tool', 'stone_tool']):
        # print(perm)
        sum_piro = 0
        copy_minerals = copy.deepcopy(minerals)


        for tool in perm:
            if tools[tool] == 0:
                continue
            for _ in range(tools[tool]):
                for _ in range(5): #하나의 도구로 5번 광물 캐기
                    if len(copy_minerals) > 0:
                        piro = pirodo[tool][copy_minerals.pop(0)] #하나의 도구를 사용해서 광물을 캘때 피로도
                        sum_piro += piro
                        # remove_cnt += 1
                    else:
                        break
        # print(f"sum_piro={sum_piro}")
        if len(copy_minerals) == 0:
            full_remove.append(sum_piro)
        else:
            part_remove.append(sum_piro)

    #모든 광물을 캐는 경우 와 그렇지 못한 경우를 구분
    if len(full_remove) > 0:
        answer = min(full_remove)
    else:
        answer = min(part_remove)

    return answer

picks = [1, 3, 2]
minerals = ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]
# result = 12

# picks = [0, 1, 1]
# minerals = ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]
# result = 50

print(solution(picks, minerals))
