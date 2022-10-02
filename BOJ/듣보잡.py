# https://www.acmicpc.net/problem/1764

# 1번 풀이 - 시간초과
# N, M = map(int, input().split())
#
# NList = []
# Mlist = []
# for i in range(N):
#     NList.append(input())
#
# for i in range(M):
#     Mlist.append(input())
#
# res = []
# for k in range(len(NList)):
#     for j in range(len(Mlist)):
#         if NList[k] == Mlist[j]:
#             res.append(NList[k])
# print(sorted(res))

from sys import stdin
input = stdin.readline

N, M = map(int, input().split())

NList = set()
Mlist = set()
for i in range(N):
    NList.add(input().strip())

for i in range(M):
    Mlist.add(input().strip())

res = sorted(list(NList & Mlist))

print(len(res))
for i in range(len(res)):
    print(res[i])
