import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
start = int(input())

graph = [[] for _ in range(n + 1)]
INF = int(1e9)
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    distance[start] = 0
    queue = [(0, start)]

    while queue:
        nextNodeDist, nextNode = heapq.heappop(queue)
        if (nextNodeDist <= distance[nextNode]):
            for node, dist in graph[nextNode]:
                cost = dist + nextNodeDist
                if (cost < distance[node]):
                    distance[node] = cost
                    heapq.heappush(queue, (cost, node))

dijkstra(start)

print (distance[1:])







