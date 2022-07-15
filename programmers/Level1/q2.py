# 스킬체크 테스트 Level1
#
def solution(array, commands): #commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    answer = []
    for i in range(len(commands)):
        sliceList = sorted(array[commands[i][0]-1: commands[i][1]])
        pickList = sliceList[commands[i][2]-1]
        answer.append(pickList)
        print(pickList)
    return answer
