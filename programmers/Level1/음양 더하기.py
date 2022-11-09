# https://school.programmers.co.kr/learn/courses/30/lessons/76501

def solution(absolutes, signs):
    answer = []

    for i in range(len(absolutes)):
        if signs[i] == False:
            absolutes[i] = absolutes[i] * -1
            answer.append(absolutes[i])
        else:
            answer.append(absolutes[i])

    print(answer)
    return sum(answer)

print(solution([1,2,3], ["false", "false", "true"]))
