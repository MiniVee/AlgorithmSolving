# acmicpc.net/problem/19238

N, M, fuel = map(int, input().split())
matrix = [list(map(int, input().strip())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

