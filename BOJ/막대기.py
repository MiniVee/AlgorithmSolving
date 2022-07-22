# 스택 - 막대기
# https://www.acmicpc.net/problem/17608

from sys import stdin
input = stdin.readline

N = int(input())
NList = []
answer = 1
for i in range(N):
    NList.append(int(input()))

last = NList[-1]
while len(NList):
    now = NList.pop()
    if now > last:
        answer+=1
        last = now
print(answer)