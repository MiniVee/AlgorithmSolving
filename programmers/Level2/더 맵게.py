# https://school.programmers.co.kr/learn/courses/9877/lessons/55762

import heapq #heapq 사용

def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)

    while len(scoville):
        firstScoville = heapq.heappop(scoville)
        if firstScoville >= K:
            break
        if len(scoville) == 0:
            answer = -1
            break
        secondeScoville = heapq.heappop(scoville)
        heapq.heappush(scoville, firstScoville + (secondeScoville * 2))
        answer += 1
    return answer

