# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do

T = int(input())
for i in range(1, T + 1):
    num = int(input())
    res = 1
    for j in range(2, num+1):
        if j % 2 == 0:
            res -= j
        else:
            res +=j
    print("#" + str(i) + " " + str(res))