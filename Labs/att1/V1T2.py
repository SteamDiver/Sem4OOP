def generator(n):
    for a in range(n):
        for b in range(n):
            for c in range(n):
                if a!=0 and b != 0 and c != 0:
                    if a*a + b*b == c:
                        yield (a, b, c)

g = generator(25)
while True:
    try:
        print(next(g))
    except StopIteration:
        break
