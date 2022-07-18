# 문제설명: 투에-모스 수열 (0과 1로만 이루어진 수열), n번쨰 수열에서 x번 위치부터 y번 위치까지의 값이 무엇인지 출력
# ex) n = 4 , x = 3, y = 7 이면 n번째 수열은 "01101001" 이지만 x번 위치부터 y번 위치까지는 "10100" 이다.

def solution(n, x, y):
    if n == 1:
        return "0"
    else:
        ans1 = "0"

        for j in range(n-1):
            ans2 = ans1[:]
            for i in range(len(ans2)):
                if ans2[i] == '0':
                    ans2 = ans2[:i] + "1" + ans2[i + 1:]
                else:
                    ans2 = ans2[:i] + "0" + ans2[i + 1:]
            ans1 = ans1 + ans2
    print(ans1)
    return ""

print(solution(3,2,3))