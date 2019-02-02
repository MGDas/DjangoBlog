x = imput('Ввидите диапазон от 0 до: ') # 100
a = 0
answer = True
while answer:
    a = int(x) / 2
    print('Это число ' + a + '?')
    ans = input('yes/no: ')
    if ans == 'yes':
        print('Ураа!!')
        answer = False
