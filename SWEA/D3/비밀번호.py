

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



