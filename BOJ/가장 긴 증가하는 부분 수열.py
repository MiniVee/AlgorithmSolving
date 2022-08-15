# https://www.acmicpc.net/problem/11053

from sys import stdin
input = stdin.readline

N = int(input())
numList = list(map(int, input().split()))

init = [1] * N

for i in range(1, len(numList)):
    for j in range(i):
        if numList[i] > numList[j]:
            init[i] = max(init[i], init[j] + 1)

print(max(init))