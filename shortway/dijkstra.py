import sys
input = sys.stdin.readline

n, m = map(int, input().split())
start = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a] = (b, c)

INF = int(1e9)
distance = [INF] * (n + 1)
visited = [False] * (n + 1)

def getNextNode():
    index = 1
    min_val = INF
    for i in range(1, n + 1):
        if (distance[i] < min_val and not visited[i]):
            index = i
            min_val = distance[i]
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = 0

    for point, dist in graph[start]:
        distance[point] = dist

    for i in range(1, n):
        index = getNextNode()
        visited[index] = True

        for point, dist in graph[index]:
            cost = dist + distance[index]
            if (distance[point] > cost):
                distance[point] = cost




