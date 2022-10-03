# https://www.acmicpc.net/problem/1427

from sys import stdin
input = stdin.readline

N = int(input())
NList = list(map(int, str(N)))

sort = sorted(NList, reverse=True)

res = "".join(map(str, sort))
print(res)