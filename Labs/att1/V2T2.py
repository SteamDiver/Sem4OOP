def generator(n):
    a = list(range(n+1))
    a[1] = 0
    i = 2
    while i <= n:
        if a[i] != 0:
            yield a[i]
            for j in range(i, n+1, i):
                a[j] = 0
        i += 1

print(tuple(generator(100)))
