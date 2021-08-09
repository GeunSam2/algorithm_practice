from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        cvertex = queue.popleft()
        print (cvertex, end=' ')
        for nvertex in graph[cvertex]:
            if not visited[nvertex]:
                queue.append(nvertex)
                visited[nvertex] = True

graph = [
    [],
    [2,3,8],
    [7],
    [4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * len(graph)

bfs(graph, 1, visited)
