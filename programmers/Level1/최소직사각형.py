# https://school.programmers.co.kr/learn/courses/30/lessons/86491

###시간이 너무 오래걸리는 풀이법###
def solution(sizes):
    max_num = max(map(max, sizes))
    for i in range(len(sizes)):
        if max_num == sizes[i][0]:
            for j in range(len(sizes)):
                if sizes[j][0] < sizes[j][1]:
                    sizes[j][1], sizes[j][0] = sizes[j][0], sizes[j][1]
        else:
            for j in range(len(sizes)):
                if sizes[j][0] < sizes[j][1]:
                    sizes[j][1], sizes[j][0] = sizes[j][0], sizes[j][1]

    secondNum = []
    for k in range(len(sizes)):
        secondNum.append(sizes[k][1])

    return max_num * max(secondNum)

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))

###시간 단축한 풀이법###
def solution(sizes):
    width = []
    height = []

    for i in range(len(sizes)):
        if sizes[i][0] > sizes[i][1]:
            width.append(sizes[i][0])
            height.append(sizes[i][1])
        else:
            width.append(sizes[i][1])
            height.append(sizes[i][0])
    return max(width) * max(height)

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))