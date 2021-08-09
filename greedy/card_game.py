n, m = map(int, input().split(' '))
cardList = [min(list(input().split(' '))) for _ in range(n)]
result = max(cardList)
print (result)