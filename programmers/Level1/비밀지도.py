# https://school.programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    answer = []
    binArr1 = []
    binArr2 = []
    for i in range(n):
        res1 = format(arr1[i], "b")
        res1 = str(res1).zfill(n)
        binArr1.append(res1)
        res2 = format(arr2[i], "b")
        res2 = str(res2).zfill(n)
        binArr2.append(res2)

        temp = ""
        for j in range(n):
            if binArr1[i][j] == "0" and binArr2[i][j] == "0":
                temp += " "
            else:
                temp += "#"
        answer.append(temp)

    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))