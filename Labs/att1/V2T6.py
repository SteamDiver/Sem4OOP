def read(file):
    with open(str(file), 'r') as f:
        lines = [int(line.strip()) for line in f]
        return tuple(lines)

arr = read("input2.txt")
s = (n for n in arr if n==max(arr, key=arr.count))
print(max(s))
