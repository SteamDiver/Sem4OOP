def read(file):
    with open(str(file), 'r') as f:
        lines = [line.strip() for line in f]
        return tuple(lines)

arr = read("input3.txt")
s = (w for w in arr if len(w) == len(min(arr)))
print(tuple(s))
