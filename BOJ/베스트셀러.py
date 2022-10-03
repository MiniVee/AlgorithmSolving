# https://www.acmicpc.net/problem/1302

# 내 풀이
import collections
from sys import stdin
input = stdin.readline

N = int(input())
NList = []
for _ in range(N):
    NList.append(input().strip())

NList_dict = collections.Counter(NList)
NList_dict_max = max(NList_dict.values())

res = []
for key, value in NList_dict.items():
    if value == NList_dict_max:
       res.append(key)

print(sorted(res)[0])

# 다른 풀이
n = int(input())
dic={}
for i in range(n):
    book = input()
    if book in dic:
        dic[book] += 1
    else:
        dic[book] = 1
res = []

best = max(dic.values())

for i in dic:
    if best == dic[i]:
        res.append(i)

print(sorted(res)[0])