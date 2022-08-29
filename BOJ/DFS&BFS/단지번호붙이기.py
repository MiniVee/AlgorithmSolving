# https://www.acmicpc.net/problem/2667

from sys import stdin
input = stdin.readline
from collections import deque

N = int(input())
matrix = [list(map(int, input())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

def solution(x, y):
    dx = [-1, 1, 0, 0] # 상 하 좌 우 좌표 x, y 반대
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((x, y))

    # matrix[x][y] = 0

    while queue:
        x, y = queue.popleft()
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 < nx < N and 0 < ny < N:
                if matrix[nx][ny] == 1 and visited[nx][ny] == False:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    cnt += 1

# 단지 갯수만 구하면 끝
# for i in range(N):
#     for j in range(N):
#진행중

solution(0, 0)




