a = (1, 1.2, 2, 2.3, 4)
b = list((a.index(i), i) for i in a)
print(b)
