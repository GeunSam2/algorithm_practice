target_h = int(input())
h, m, s = 0, 0, 0

result = 0
while (f'{h}:{m}:{s}' != f'{target_h}:59:59'):
    s += 1
    if (s == 60):
        s = 0
        m += 1
    if (m == 60):
        m = 0
        h += 1
    time_string = f'{h}:{m}:{s}'
    if ('3' in time_string):
        result += 1

print (result)