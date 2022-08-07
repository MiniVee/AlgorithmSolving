# https://www.acmicpc.net/problem/1789

from sys import stdin
input = stdin.readline

S = int(input())
n = 1

while n * (n+1)/2 <= S:
    n += 1

print(n-1)