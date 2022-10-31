# https://school.programmers.co.kr/learn/courses/30/lessons/133502

def solution(ingredient):
    answer = 0
    stack = []

    for i in range(len(ingredient)):
        stack.append(ingredient[i])

        if len(stack) >= 4:
            bread1 = stack[-4]
            veg = stack[-3]
            meat = stack[-2]
            bread2 = stack[-1]

            if bread1 == 1 and veg == 2 and meat == 3 and bread2 == 1:
                stack.pop()
                stack.pop()
                stack.pop()
                stack.pop()
                answer +=1
    return answer

print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))