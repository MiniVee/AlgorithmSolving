# https://www.acmicpc.net/problem/1920

from sys import stdin
input = stdin.readline

N = int(input())
nList = sorted(list(map(int, input().split())))
M = int(input())
mList = list(map(int, input().split()))

for i in mList:
    left = 0
    right = N - 1
    while left <= right:
        mid = (left + right) // 2
        if i == nList[mid]:
            print("1")
            break
        elif i > nList[mid]:
            left = mid + 1
        elif i < nList[mid]:
            right = mid - 1

    if left > right:
        print("0")