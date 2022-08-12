# https://www.acmicpc.net/problem/2512

from sys import stdin
input = stdin.readline

N = int(input())                        # 지방 수
req = list(map(int, input().split()))   # 예산 요청
M = int(input())                        # 총 예산

if sum(req) <= M:                       # 총합이 예산액 보다 작으면 req의 max값 호출
    print(max(req))

else:
    left = 0                            # 시작
    right = max(req)                    # 끝
    while left <= right:
        mid = (left + right) // 2       # 중간 값 찾기
        cnt = 0                         # 총액
        for i in req:
            if i >= mid:
                cnt += mid
            else:
                cnt += i

        if cnt <= M:
            left = mid + 1
        else:
            right = mid - 1

    print(right)


