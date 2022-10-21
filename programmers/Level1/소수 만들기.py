# https://school.programmers.co.kr/learn/courses/30/lessons/12977

from itertools import *
def solution(nums):
    answer = []
    res = []
    result = 0
    for i in range(len(nums)):
        answer = list(combinations(nums, 3))

    for i in range(len(answer)):
        res.append(sum(answer[i]))
    print(res)

    for k in res:
        for j in range(2, int(k**0.5) + 1):
            if k % j == 0:
                break
        else:
            result+=1

    return result

print(solution([1, 2, 7, 6, 4]))

