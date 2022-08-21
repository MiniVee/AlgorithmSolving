# https://www.acmicpc.net/problem/2178

from collections import deque
from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().strip())) for _ in range(N)]
# print(matrix)

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

n = len(matrix)
m = len(matrix[0])
# print(n, m)

queue = deque()
queue.append((0,0))

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if matrix[nx][ny] == 1:
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append((nx, ny))

answer = matrix[-1][-1]
print(answer)


