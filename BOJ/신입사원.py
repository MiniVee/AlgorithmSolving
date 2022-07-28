# https://www.acmicpc.net/problem/1946

# 내 풀이
from sys import stdin
input = stdin.readline

T = int(input())                                                # 테스트 케이스 개수

for _ in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]   # 2차원 배열
    sortArr = sorted(arr)                                       # 2차원 배열 정렬
    cnt = 1                                                     # cnt 초기값 1
    now = sortArr[0][1]                                         # 현재 2차원 배열 값

    for j in range(N):                                          # 현재랑 다음 것의 두번째 점수를 계속 비교
        if now > sortArr[j][1]:
            now = sortArr[j][1]
            cnt +=1

    print(cnt)

# 다른 풀이
import sys
input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    N = int(input().strip())
    apply = [list(map(int, input().strip().split())) for _ in range(N)]

    apply.sort(key=lambda x: x[0])

    res = 0
    piv = 100001
    for score in apply:
        if piv > score[1]:
            piv = score[1]
            res += 1
    print(res)