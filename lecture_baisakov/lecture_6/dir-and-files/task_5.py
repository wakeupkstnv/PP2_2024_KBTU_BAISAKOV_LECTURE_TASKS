with open('test.txt', 'w') as text:
    lst = [input() for _ in range(10 ** 6)]
    
    for i in lst:
        text.write(f'{i}\n')
        