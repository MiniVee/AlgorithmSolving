# https://school.programmers.co.kr/learn/courses/30/lessons/12909

##정답##
def solution(s):
    answer = []

    if s[-1] == "(":
        return False
    for i in s:
        if i == "(":
            answer.append(i)
        else:
            if len(answer) == 0:
                return False
            else:
                answer.pop()

    return answer == []

print(solution(	"()()"))
print(solution("()))((()"))

##오답##
def solution(s):
    answer = True

    dict = {"(" : 0, ")" : 0}

    if s[0] == ")":
        return False
    if s[-1] == "(":
        return False
    else:
        for i in range(len(s)):
            if s[i] == "(":
                dict["("] += 1
            else:
                dict[")"] += 1
    if dict["("] == dict[")"]:
        return True
    else:
        return False