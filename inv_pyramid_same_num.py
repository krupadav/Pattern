rows = int(input('Enter a number:'))
for i in range(rows, 0, -1):
    for j in range(0, i):
        print(rows, end='')
    print('\r')
