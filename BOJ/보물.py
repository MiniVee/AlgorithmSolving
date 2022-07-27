# https://www.acmicpc.net/problem/1026

import sys
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().strip().split()))
B = list(map(int, input().strip().split()))

S = 0
for _ in range(N):
    S += min(A) * max(B)
    A.pop(A.index(min(A)))
    B.pop(B.index(max(B)))
print(S)

