# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do


T = int(input())
for test_case in range(1, T+1):
    S = input()
    num_list = S.split()
    cnt = 0
    for num in num_list:
        if int(num) % 2 == 1:
            cnt += int(num)
    print("#" + str(test_case) + " " + str(cnt))


# 3
# 3 17 1 39 8 41 2 32 99 2
# 22 8 5 123 7 2 63 7 3 46
# 6 63 2 3 58 76 21 33 8 1