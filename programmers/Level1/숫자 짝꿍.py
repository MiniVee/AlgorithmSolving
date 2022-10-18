# https://school.programmers.co.kr/learn/courses/30/lessons/131128

def solution(X, Y):
    answer = []

    for i in set(X)&set(Y):
        for j in range(min(X.count(i), Y.count(i))):
            answer.append(i)
    answer.sort(reverse=True)
    if len(answer) == 0:
        return "-1"
    if answer[0] == "0":
        return "0"
    answer = "".join(answer)

    return answer


print(solution("100", "123450"))
#print(solution("12321", "42531"))