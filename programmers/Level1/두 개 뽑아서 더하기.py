# https://school.programmers.co.kr/learn/courses/30/lessons/68644

def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(1, len(numbers)):
            if i !=j:
                answer.append(numbers[i]+numbers[j])
    answer = list(set(answer))
    answer.sort(reverse=False)
    return answer

print(solution([2,1,3,4,1]))