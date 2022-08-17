# https://www.acmicpc.net/problem/12015
# python3으로 돌렸을 때는 시간초과가 나지만 pypy로 돌리면 정답이다.

from sys import stdin
input = stdin.readline

N = int(input())
numList = list(map(int, input().split()))
# print(numList)

ans = [0]

for i in numList:
    if ans[-1] < i:
        ans.append(i)
    else:
        left = 0
        right = len(ans)-1

        while left <= right:
            mid = (left + right) // 2

            if ans[mid] < i:
                left = mid + 1
            else:
                right = mid - 1

        ans[left] = i

print(ans)
print(len(ans) - 1)



