# https://www.acmicpc.net/problem/1978

from sys import stdin
input = stdin.readline

N = int(input())
NList = list(map(int, input().split()))

cnt = 0
for i in NList:
    if i != 1:
        for j in range(2, i):
            if i%j ==0:
                break
        else:
            cnt +=1

print(cnt)