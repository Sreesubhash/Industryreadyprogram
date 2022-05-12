n = 6
for i in range(1, 6):
    for j in range(i, -1, -1):
        print(' ', end=' ')
    for j in range(n - i, 0, -1):
        print(n - j, end=' ')
    print()