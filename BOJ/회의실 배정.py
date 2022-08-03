# https://www.acmicpc.net/problem/1931

# 내 풀이
import sys
input = sys.stdin.readline
N = int(input())
room = []
cnt = 1
for i in range(N):
    a, b = map(int, input().split())
    room.append([a, b])

sortRoom = sorted(room, key = lambda x : (x[1], x[0]))

end = sortRoom[0][1]
print(sortRoom)

for i in range(1, len(sortRoom)):
    if end <= sortRoom[i][0]:
        end = sortRoom[i][1]
        cnt += 1

print(cnt)

# 다른 풀이
# import sys
# input = sys.stdin.readline
#
# N = int(input().strip())
# meetings = [list(map(int, input().strip().split())) for _ in range(N)]
#
# meetings.sort(key=lambda x: (x[1], x[0]))
#
# endtime = 0
# res = 0
# for s,e in meetings:
#     if s >= endtime:
#         endtime = e
#         res += 1
#
# print(res)