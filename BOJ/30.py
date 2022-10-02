# https://www.acmicpc.net/problem/10610

N = int(input())
NList = list(map(int, str(N)))
NList = sorted(NList, reverse=True)

cnt = 0
for i in NList:
    cnt += i
if cnt % 3 != 0 or 0 not in NList:
    print(-1)
else:
    print("".join(map(str, NList)))
