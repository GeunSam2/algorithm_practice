board_size = int(input())
directions = input().split(' ')

x , y = 1, 1
for direction in directions:
    if (direction == 'L' and x > 1):
        x -= 1
    elif (direction == 'R' and x < board_size):
        x += 1
    elif (direction == 'U' and y > 1):
        y -= 1
    elif (direction == 'D' and y < board_size):
        y += 1

print (y, x)