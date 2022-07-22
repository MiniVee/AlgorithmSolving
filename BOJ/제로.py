# https://www.acmicpc.net/problem/10773
from sys import stdin
input = stdin.readline

N = int(input())
NList = []

for _ in range(N):
    ans1 = int(input())
    if ans1 == 0:
        NList.pop()
    else:
        NList.append(ans1)

answer = sum(NList)
print(answer)