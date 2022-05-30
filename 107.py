n = 6
for i in range(0, 5):
    for j in range(n - i - 1):
        print('  ', end='')
    for j in range(i + 1):
        print(j + 1, end='   ')
    print()
