# https://school.programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []

    for i in range(len(commands)):
        sliceArray = array[commands[i][0] - 1 : commands[i][1]]   # 2차원배열을 통해 값을 slicing
        sortArray = sorted(sliceArray)                            # 정렬
        answer.append(sortArray[commands[i][2] - 1])              # answer에 원하는 위치의 숫자를 append
    return answer
