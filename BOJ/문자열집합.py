# https://www.acmicpc.net/problem/14425

# 1번 풀이 - 시간초과
# from sys import stdin
# input = stdin.readline
#
# N, M = map(int, input().split())
# NList = []
# MList = []
# for i in range(N):
#     NList.append(input())
# for i in range(M):
#     MList.append(input())
# cnt = 0
# for k in range(len(MList)):
#     for j in range(len(NList)):
#         if MList[k] == NList[j]:
#             cnt +=1
#             break
#
# print(cnt)

# from sys import stdin
# input = stdin.readline
#
# N, M = map(int, input().split())
# NList = []
# cnt = 0
# for i in range(N):
#     NList.append(input().strip())
# for _ in range(M):
#     word = input().strip()
#     if word in NList:
#         cnt+=1
# print(cnt)

from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
NList = []
cnt = 0
for i in range(N):
    NList.append(input().strip())
for i in range(M):
    Mword = input().strip()
    if Mword in NList:
        cnt +=1

print(cnt)