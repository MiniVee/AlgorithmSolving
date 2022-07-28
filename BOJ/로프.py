# https://www.acmicpc.net/problem/2217

from sys import stdin
input = stdin.readline

N = int(input())
NList = []
for i in range(N):
    NList.append(int(input()))
sortNList = sorted(NList, reverse=True)
# print(sortNList)
answer = []
j = 1
for i in range(N):
    answer.append(sortNList[i] * j)
    j+=1

print(max(answer))