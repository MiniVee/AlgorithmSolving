# https://www.acmicpc.net/problem/11399

# 1번 풀이
N = int(input())
NList = list(map(int, input().strip().split()))
sortNList = sorted(NList)
answer = []
for i in range(N):
    sumAns = sortNList[:i+1]
    answer.append(sum(sumAns))

print(sum(answer))

# 2번 풀이
import sys
input = sys.stdin.readline

N = int(input().strip())
line = list(map(int, input().strip().split()))

line.sort()

res = 0
acc = 0
for i in line:
    acc += i
    res += acc

print(res)
