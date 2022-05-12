n = 0
for i in range(5, 0, -1):
    n += 1
    for j in range(1, i + 1):
        print(n, end=' ')
    print()