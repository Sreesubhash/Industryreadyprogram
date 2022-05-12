n = 6
for i in range(5, 0, -1):
    for j in range(n - i - 1):
        print(' ', end='')
    for j in range(i):
        print(i, end=' ')
    print()
