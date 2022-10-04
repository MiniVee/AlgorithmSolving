import heapq
from sys import stdin
import math
input = stdin.readline

node, edge = map(int, input().split())
start = int(input())
INF = float(math.inf)
distance = [INF] * (node + 1)
graph = [[] for _ in range(node+1)]
for _ in range(edge):
    nowN, nextN, weight = map(int, input().split())
    graph[nowN].append((nextN, weight))

def diAlgo(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        qDistance, qNode = heapq.heappop(queue)
        if distance[qNode] < qDistance:
            continue
        for nextInformation in graph[qNode]:
            weightCost = distance[qNode] + nextInformation[1]
            if weightCost < distance[nextInformation[0]]:
                distance[nextInformation[0]] = weightCost
                heapq.heappush(queue, (weightCost, nextInformation[0]))

diAlgo(start)

for i in range(len(distance)-1):
    if distance[i] == INF:
        print("x")
    else:
        print(distance[i])



