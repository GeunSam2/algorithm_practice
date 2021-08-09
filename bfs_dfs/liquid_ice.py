from collections import deque
n, m = list(map(int, input().split(' ')))
plate = [list(map(int, input())) for _ in range(n)]

directions =[(-1,0), (0,1), (1,0), (0,-1)]
count = 0

for x,st1 in enumerate(plate):
    for y,st2 in enumerate(st1):
        if st2 == 0:
            count += 1
            plate[x][y] = 1
            queue = deque([(x,y)])
            while queue:
                cx, cy = queue.popleft()
                for xv, yv in directions:
                    nx = cx + xv
                    ny = cy + yv
                    if (nx < 0 or nx >= n or ny < 0 or ny >= m): 
                        nx = cx
                        ny = cy
                    if (plate[nx][ny] == 0):
                        queue.append((nx,ny))
                        plate[nx][ny] = 1

print (count)




