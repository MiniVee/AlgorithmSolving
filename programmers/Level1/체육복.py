# https://school.programmers.co.kr/learn/courses/30/lessons/42862

# 첫번째 풀이
def solution(n, lost, reserve):
    nList = [1 for i in range(n + 2)]
    for i in reserve:
        nList[i] += 1
    for i in lost:
        nList[i] -= 1

    kList = [1 for i in range(n + 2)]
    for i in reserve:
        kList[i] += 1
    for i in lost:
        kList[i] -= 1

    ans1 = 0
    ans2 = 0

    for i in range(1, len(nList) - 1):
        if nList[i] == 2 and nList[i - 1] == 0:
            nList[i] -= 1
            nList[i - 1] += 1
    for j in range(1, len(nList) - 1):
        if nList[j] > 0:
            ans1 += 1

    for k in range(1, len(kList) - 1):
        if kList[k] == 2 and kList[k + 1] == 0:
            kList[k] -= 1
            kList[k + 1] += 1

    for m in range(1, len(kList) - 1):
        if kList[m] > 0:
            ans2 += 1

    answer = max(ans1, ans2)

    return answer
