# https://school.programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    answer = ''

    ls = list(map(int, s.split()))
    ls.sort()
    answer += str(ls[0]) + " " + str(ls[-1])
    print(ls)
    return  answer

print(solution("11 -1 2 -2 4 -8"))
print(solution("-1 -2 -3 -4"))
print(solution("-1 -1"))