

# https://www.codetree.ai/ko/frequent-problems/all/problems/pirate-captain-coddy/description

import sys
import heapq


def solve():
    input = sys.stdin.readline

    T = int(input())

    power = {}
    reload_time = {}
    is_ready = {}

    heap = []

    wake = {}

    answer = []

    for t in range(1, T + 1):

        if t in wake:
            for ship_id in wake[t]:
                is_ready[ship_id] = True

                heapq.heappush(heap, (-power[ship_id], ship_id))

            del wake[t]


        cmds = list(map(int, input().split()))
        command = cmds[0]

        if command == 100:

            n = cmds[1]
            pos = 2
            for _ in range(n):
                ship_id = cmds[pos]
                p       = cmds[pos + 1]
                r       = cmds[pos + 2]
                pos = pos + 3

                power[ship_id] = p
                reload_time[ship_id] = r
                is_ready[ship_id] = True
                heapq.heappush(heap, (-p, ship_id))

        elif command == 200:
            ship_id = cmds[1]
            p = cmds[2]
            r = cmds[3]
            power[ship_id] = p
            reload_time[ship_id] = r
            is_ready[ship_id] = True
            heapq.heappush(heap, (-p, ship_id))

        elif command == 300:
            ship_id = cmds[1]
            new_power = cmds[2]
            power[ship_id] = new_power
            if is_ready[ship_id] == True:
                heapq.heappush(heap, (-new_power, ship_id))

        else:
            fired = []
            total = 0

            while len(heap) > 0 and len(fired) < 5:
                neg_power, ship_id = heapq.heappop(heap)
                p = -neg_power

                # ===== 지연 삭제 (이 문제의 핵심 발상) =====
                # 힙에는 옛날 정보가 섞여 있을 수 있다(재장전됐거나 공격력이 바뀐 항목).
                # 힙에서 직접 지울 수 없으니, 꺼낼 때마다 "지금도 진짜인지" 검사해 가짜면 버린다.

                if is_ready[ship_id] == False:
                    continue

                if power[ship_id] != p:
                    continue

                fired.append(ship_id)
                total = total + p

                is_ready[ship_id] = False
                back_time = t + reload_time[ship_id]

                if back_time not in wake:
                    wake[back_time] = []
                wake[back_time].append(ship_id)

            line = str(total) + " " + str(len(fired))
            for ship_id in fired:
                line = line + " " + str(ship_id)
            answer.append(line)

    return "\n".join(answer)


def main():
    print(solve())


