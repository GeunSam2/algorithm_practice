n, k  = map(int, input().split(' '))

result = 0
while (n != 1):
    remain = n % k
    if (remain == 0): 
        n //= k
        result += 1
    else: 
        n -= remain
        result += remain
    

print (result)