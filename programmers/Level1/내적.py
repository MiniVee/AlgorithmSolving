# https://school.programmers.co.kr/learn/courses/30/lessons/70128

def solution(a, b):
    answer = []
    for i in range(len(a)):
        for j in range(len(b)):
            j = i
            answer.append(a[i] * b[j])
            break

    return sum(answer)

def solution2(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i] * b[i]

    return answer

print(solution([1, 2, 3, 4],
               [-3, -1, 0, 2]))