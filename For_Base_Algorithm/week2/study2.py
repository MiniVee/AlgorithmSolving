#컴퓨터랑 가위바위보해서 결과 출력 (내가 이기면 승리, 지면 패배, 비기면 무승부)

import random

while True:
    ans = int(input("입력: "))
    j = random.randint(1, 3)

    orgList = [1, 2, 3]
    mostLeft = orgList[0]
    mostRight = orgList[len(orgList)-1]

    lst = []
    lst.append(mostRight)
    for value in orgList:
        lst.append(value)
    lst.append(mostLeft)

    print(lst)

   # lst = [3, 1, 2, 3, 1]


    win = lst[ans-1]
    lose = lst[ans+1]

    if win == j:
        print("win")
    elif lose == j:
        print("lose")
    else:
        print("draw")

    print(j)


