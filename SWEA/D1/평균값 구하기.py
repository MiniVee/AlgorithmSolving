# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do

T = int(input())
for test_case in range(1, T + 1):
    S = input()
    S_list = S.split()
    #print(S_list)
    cnt = 0
    for num in S_list:
        cnt += int(num)
        divCnt = cnt / 10
    print("#" + str(test_case) + " " + str(round(divCnt)))
