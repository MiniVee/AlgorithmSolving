# https://www.acmicpc.net/problem/11047

N, K = map(int, input().split())
coin = []
for i in range(N):
    coin.append(int(input()))
coin.sort(reverse=True)
#print(N, K, coin)

cnt = 0
for i in coin:
    cnt += K//i
    K %= i

print(cnt)