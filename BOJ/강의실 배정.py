# https://www.acmicpc.net/problem/11000

# 내 풀이
import heapq
from sys import stdin
input = stdin.readline

B = int(input())
h = []

arr = [list(map(int, input().split())) for _ in range(B)]
sortArr = sorted(arr)
# print(sortArr)
heapq.heappush(h, sortArr[0][1])

for j in range(1, len(sortArr)):
    if h[0] > sortArr[j][0]:
        heapq.heappush(h, sortArr[j][1])
    else:
        heapq.heappop(h)
        heapq.heappush(h, sortArr[j][1])

print(len(h))

# 인덱스 오류난 오답 (2차원 배열 만들때 잘못 만들었다.)
import heapq
from sys import stdin
input = stdin.readline

B = int(input())
h = []
for i in range(B):
    arr = [list(map(int, input().split())) for _ in range(B)]
    sortArr = sorted(arr)

    heapq.heappush(h, sortArr[0][1])

    for j in range(1, len(sortArr)):
        if h[0] > sortArr[j][0]:
            heapq.heappush(h, sortArr[j][1])
        else:
            heapq.heappop(h)
            heapq.heappush(h, sortArr[j][1])

    print(len(h))