# https://school.programmers.co.kr/learn/courses/30/lessons/42883

# 내 풀이
def solution(number, k):
    numList = list(map(int, str(number)))

    ans = []
    for i in numList:
        if not ans:
            ans.append(i)
        else:
            if k > 0:
                while ans and ans[-1] < i:
                    ans.pop()
                    k -= 1
                    if not ans or k == 0:
                        break
            ans.append(i)

    answer = "".join(map(str, ans))
    if k > 0:
        answer = "".join(map(str, ans[:-k]))
    return answer

# 다른 풀이
def solution(number, k):
    stack = []
    number = list(map(int, number))

    stack.append(number[0])
    for num in number[1:]:
        while stack and stack[-1] < num:
            if k > 0:
                stack.pop()
                k -= 1
            else:
                break
        stack.append(num)
    answer = "".join(list(map(str, stack)))
    return answer if k == 0 else answer[:-k]