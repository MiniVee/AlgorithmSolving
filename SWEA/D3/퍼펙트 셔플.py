#

T = int(input())

for test_case in range(1, T + 1):
    num = int(input())
    alphabet = input().split()
    alphabetList = list(map(str, alphabet))

    if len(alphabetList) % 2 == 0:
        div = len(alphabetList) // 2
        alphabetListA = alphabetList[ : div]
        alphabetListB = alphabetList[div : ]
        stack = []
        for j in range(div):
            stack.append(alphabetListA[j])
            stack.append(alphabetListB[j])
        fstack = " ".join(stack)
        print("#" + str(test_case) + " " + fstack)
    else:
        div = len(alphabetList) // 2
        alphabetListA = alphabetList[: div + 1]
        alphabetListB = alphabetList[div + 1:]
        stack = []
        for j in range(div):
            stack.append(alphabetListA[j])
            stack.append(alphabetListB[j])
        stack.append(alphabetListA[-1])
        fstack = " ".join(stack)
        print("#" + str(test_case) + " " + fstack)

