pos = input()
xpos = ord(pos[0]) - 96
ypos = int(pos[1])
result = 0
xforward = [2, 2, 1, -1, -2, -2, 1, -1]
yforward = [-1, 1, 2, 2, -1, 1, -2, -2]

for index in range(8):
    calcx = xpos + xforward[index]
    calcy = ypos + yforward[index]
    #print (calcx, calcy)
    if (calcx >= 1 and calcy >= 1): result += 1

print (result)