# https://www.acmicpc.net/problem/1541

from sys import stdin
input = stdin.readline

myInput = input().strip().split("-")
num = []

for i in myInput:
    cnt = 0
    addSplit = i.split("+")
    # print(addSplit)
    for j in addSplit:
        cnt += int(j)
    num.append(cnt)
#     print(cnt)
# print(num)
first = num[0]

for k in range(1, len(num)):
    first -= num[k]

print(first)

