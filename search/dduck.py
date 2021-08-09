n, m  = map(int, input().split(' '))
array = list(map(int, input().split(' ')))
array.sort(reverse=True)

max_height = array[0]
cutted = 0
while cutted < m:
    cutted = 0
    max_height -= 1
    for item in array:
        if (item <= max_height):
            continue
        else:
            cutted += (item - max_height)

print (max_height)
