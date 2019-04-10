def read(file):
    with open(str(file), 'r') as f:
        lines = [tuple(line.split()) for line in f]
        return tuple(lines)

arr = read("input1.txt")
target_length = len(max(set(i) for i in arr))
print(tuple(str for str in arr if len(str) == target_length))
