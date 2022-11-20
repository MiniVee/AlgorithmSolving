# 1209
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&problemLevel=3&contestProbId=AV13_BWKACUCFAYh&categoryId=AV13_BWKACUCFAYh&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=2

T = 10
for test_case in range(1, T + 1):
    testNum = int(input())

    numList = []
    for i in range(100):
        numList.append(list(map(int, input().split())))

    rowNum = 0
    for j in range(len(numList)):
        sumRowNum = 0
        for k in range(len(numList)):
             sumRowNum += numList[j][k]
        if sumRowNum > rowNum:
            rowNum = sumRowNum

    columnNum = 0
    for j in range(len(numList)):
        sumcolumnNum = 0
        for k in range(len(numList)):
             sumcolumnNum += numList[k][j]
        if sumcolumnNum > columnNum:
            columnNum = sumcolumnNum

    crossNum = 0
    for j in range(len(numList)):
        right = 0
        left = 0
        right += numList[j][j]
        left += numList[j][99-j]
        if max(right, left) > crossNum:
            crossNum = max(right, left)

    print("#",test_case," " ,max(rowNum, columnNum, crossNum), sep="")
