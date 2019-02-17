def find_all(a, value):
    return [i for i, j in enumerate(a) if j == value]


with open('input', 'r') as f:
    arr = [int(x) for x in f.readline().split(", ")]

first_max_index = find_all(arr, max(arr))[0]
last_min_index = find_all(arr, min(arr))[-1]
if first_max_index < last_min_index:
    start_index = first_max_index
    stop_index = last_min_index
else:
    start_index = last_min_index
    stop_index = first_max_index

sub_array = arr[start_index + 1:stop_index]

res_array = arr[0: start_index + 1] + list(reversed(sub_array)) + arr[stop_index:]
print(res_array)
