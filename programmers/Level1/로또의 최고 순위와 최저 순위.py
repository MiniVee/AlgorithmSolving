# https://school.programmers.co.kr/learn/courses/30/lessons/77484#fn1

def solution(lottos, win_nums):
    answer = []
    equalNum = 0
    lot_cnt = lottos.count(0)
    for i in win_nums:
        if i in lottos:
            equalNum+=1
    minScore = equalNum
    maxScore = equalNum + lot_cnt

    if minScore == 6:
        answer.append(1)
    elif minScore == 5:
        answer.append(2)
    elif minScore == 4:
        answer.append(3)
    elif minScore == 3:
        answer.append(4)
    elif minScore == 2:
        answer.append(5)
    else:
        answer.append(6)

    if maxScore == 6:
        answer.append(1)
    elif maxScore == 5:
        answer.append(2)
    elif maxScore == 4:
        answer.append(3)
    elif maxScore == 3:
        answer.append(4)
    elif maxScore == 2:
        answer.append(5)
    else:
        answer.append(6)

    return sorted(answer)

print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]	))