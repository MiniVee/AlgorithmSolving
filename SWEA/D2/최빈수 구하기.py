# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&problemLevel=3&contestProbId=AV13_BWKACUCFAYh&categoryId=AV13_BWKACUCFAYh&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=2

T = int(input())
for test_case in range(1, T + 1):
    tNum = int(input())
    num = list(map(int, input().split()))
    dict_num = {}
    for i in num:
        if i not in dict_num:
            dict_num[i] = 1
        else:
            dict_num[i] += 1

    keyvalue = []
    for key, value in dict_num.items():
        if value == max(dict_num.values()):
            keyvalue.append(key)
            sorted(keyvalue)
            # print(keyvalue)

    print("#",tNum, " ",keyvalue[0],sep="")