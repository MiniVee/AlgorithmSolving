# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&problemLevel=3&contestProbId=AV13_BWKACUCFAYh&categoryId=AV13_BWKACUCFAYh&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=2


for test_case in range(1, 11):
    allNum, Num = map(str, input().split())

    # print(allNum, Num)
    res = []
    for i in Num:
        if len(res) != 0 and i == res[-1]:
            res.pop()
        else:
            res.append(i)
    # print(res)
    # res = list(map(int, res))
    res = "".join(res)
    print("#", test_case, " ", res, sep="")



