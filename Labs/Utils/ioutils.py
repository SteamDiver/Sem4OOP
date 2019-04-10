def read_array(file):
    with open(str(file), 'r') as f:
        arr = [int(x) for x in f.readline().split(", ")]
        return arr

def read_array2d(file):
    with open(str(file), 'r') as f:
        lines = [[float(l) for l in line.split()] for line in f]
        return lines
