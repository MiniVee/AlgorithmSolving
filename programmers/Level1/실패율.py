# https://school.programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    answer = []
    stages.sort()
    dict_stage = {}
    dict_fail = {}

    for x in stages:
        dict_stage[x] = dict_stage.get(x, 0) + 1
    all = len(stages)
    for i in range(1, N+1):
        if all != 0:
            num = stages.count(i)
            dict_fail[i] = num/all
            all -=num
        else:
            dict_fail[i] = 0

    dict_fail = sorted(dict_fail, key = lambda x:dict_fail[x], reverse=True)

    return dict_fail

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print("-------")
print(solution(4, [4, 4, 4, 4, 4]))