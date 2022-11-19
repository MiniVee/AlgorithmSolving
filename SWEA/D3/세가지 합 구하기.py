#

T = int(input())

for test_case in range(1, T + 1):
    num = int(input())

    numList = []
    s1Num = 0
    s2Num = 0
    s3Num = 0

    s1Num += (num * (num+1))//2
    s2Num += num ** 2
    s3Num += (num+1) * num


    print("#" + str(test_case) + " " + str(s1Num) + " " + str(s2Num) + " " + str(s3Num) + " ")