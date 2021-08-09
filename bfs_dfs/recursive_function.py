def recursive_func(num):
    if (num == 100):
        return
    
    print (f'{num}번째 함수에서 {num+1}번째 함수를 호출함')
    recursive_func(num + 1)
    print (f'{num}번째 함수 종료')

recursive_func(1)