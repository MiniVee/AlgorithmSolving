# https://www.acmicpc.net/problem/1316

from sys import stdin
input = stdin.readline

N = int(input())
cnt = N
for i in range(N):
    word = input()
    for j in range(len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            cnt-=1
            break

print(cnt)