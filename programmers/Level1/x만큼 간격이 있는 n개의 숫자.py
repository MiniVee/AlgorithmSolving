# https://school.programmers.co.kr/learn/courses/30/lessons/12954

def solution(x, n):
    answer = []
    for i in range(1, n + 1): # 1부터 시작해야 자기 자신부터 시작한다.
        answer.append(x * i)
    return answer

print(solution(2,5))