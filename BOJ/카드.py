# 카드: https://www.acmicpc.net/problem/11652

# 내 풀이
from collections import Counter
from sys import stdin
input = stdin.readline

N = int(input())
card = []
for i in range(N):
    card.append(int(input()))
sortCard = sorted(card)
counterCard = Counter(sortCard)
# print(counterCard[1])
compare = [0, 0]                        # dictionary 이용해서 비교하기 위한 compare[]
for i in counterCard:
    if compare[0] < counterCard[i]:
        compare[0] = counterCard[i]
        compare[1] = i

print(compare[1])

# 다른 풀이
import sys
input = sys.stdin.readline

N = int(input().strip())
card = [int(input().strip()) for _ in range(N)]

card.sort(reverse=True)

res = card[0]
prev = 2**62+1
max = 1
cnt = 0
for i in card:
    if i == prev:
        cnt += 1
    else:
        cnt = 1

    if cnt >= max:
            res = i
            max = cnt
    prev = i

print(res)