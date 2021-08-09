n, m  = map(int, input().split(' '))
y, x, d  = map(int, input().split(' '))

map_list = [input().split(' ') for _ in range(n)]
hang_count = 0
result = 0
while True:
    hang_count += 1

    # 방향회전
    d -= 1
    if (d == -1): d = 3

    # 이동 예정 위치 설정
    if (d == 0): 
        if (hang_count == 4):
            next_x = x
            next_y = y + 1
        else:
            next_x = x
            next_y = y - 1
    elif (d == 1): 
        if (hang_count == 4):
            next_x = x - 1
            next_y = y
        else:
            next_x = x + 1
            next_y = y
    elif (d == 2): 
        if (hang_count == 4):
            next_x = x
            next_y = y - 1
        else:
            next_x = x
            next_y = y + 1
    elif (d == 3): 
        if (hang_count == 4):
            next_x = x + 1
            next_y = y
        else:
            next_x = x - 1
            next_y = y

    #
    if (next_x >= 0 and next_y >= 0):
        map_list[x][y] = '3'
        if (map_list[next_x][next_y] == '0'):
            x, y = next_x, next_y
            hang_count = 0
            result += 1
        elif (map_list[next_x][next_y] == '3' and hang_count == 4):
            x, y = next_x, next_y
            hang_count = 0
            result += 1
        elif (map_list[next_x][next_y] == '1' and hang_count == 4):
            break


print (result)

        
        

