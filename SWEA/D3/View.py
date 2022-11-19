#

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    height = list(map(int, input().split()))

    answer = 0

    for i in range(2, N-2):
        left1 = height[i] - height[i-1]
        left2 = height[i] - height[i-2]
        right1 = height[i+1] - height[i]
        right2 = height[i+2] - height[i]

        if left1 >0 and left2 > 0 and right1 > 0 and right2 > 0:
            answer += min(left1,left2,right1,right2)
    print("#" + str(test_case) + " " + str(answer))

