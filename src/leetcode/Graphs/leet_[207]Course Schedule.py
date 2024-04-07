
from typing import List

OUTGOING = 0
INCOMING = 1

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        vertexes = {}

        #그래프의 들어오는 간선과, 나가는 간선을 기록한다.
        for [fr, to] in prerequisites:
            if fr not in vertexes.keys():
                vertexes[fr] = [[], []]

            if to not in vertexes.keys():
                vertexes[to] = [[], []]

            vertexes[fr][OUTGOING].append(to)
            vertexes[to][INCOMING].append(fr)

        queue = []


        # 진입차수 0 인 노드를 찾아 큐에 넣는다
        for key in vertexes.keys():
            if len(vertexes[key][INCOMING]) == 0:
                queue.append([key, vertexes[key]])

        while len(queue) > 0:
            fr, vertex = queue.pop(0)
            #진입차수가 0을 노드를 제거한다.
            del vertexes[fr]

            for to in vertex[OUTGOING]:
                # 간선을 제거
                vertexes[to][INCOMING].remove(fr)

                #진입차수가 0이면 큐에 넣는다
                if len(vertexes[to][INCOMING]) == 0:
                    queue.append([to, vertexes[to]])

        return len(vertexes.keys()) == 0