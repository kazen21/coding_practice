# https://school.programmers.co.kr/learn/courses/30/lessons/42627
from heapq import heappush, heappop
def solution(jobs):
    answer = 0

    cnt = 0
    start = -1
    cur = 0

    hq = []
    total = []

    while cnt < len(jobs):
        for job in jobs:
            req_t, w_t = job
            if start < req_t <= cur:
                heappush(hq, [w_t, req_t])

        if len(hq) > 0:
            w_t, req_t = heappop(hq)
            start = cur
            cur = cur + w_t
            each = cur - req_t
            total.append(each)
            cnt += 1
        else:
            cur += 1

    answer = sum(total)//len(jobs)

    return answer