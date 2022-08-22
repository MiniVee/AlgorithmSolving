# https://school.programmers.co.kr/learn/courses/30/lessons/43164

def solution(tickets):
    answer = []

    stack = []
    for i in range(len(tickets)):
        if len(stack) == 0:
            stack.append()
    return answer

# sortRoom = sorted(room, key = lambda x : (x[1], x[0]))
solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])