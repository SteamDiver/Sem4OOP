def _first_max_index(arr):
    max_index = 0
    for i in range(len(arr)):
        if arr[i] > arr[max_index]:
            max_index = i
    return max_index

def _last_min_index(arr):
    min_index = 0
    for i in range(len(arr)):
        if arr[i] <= arr[min_index]:
            min_index = i
    return min_index

def solve(arr):
    start = _first_max_index(arr)
    stop = _last_min_index(arr)
    sub_arr = list(reversed(arr[start + 1 : stop]))
    return arr[0:start + 1] + sub_arr + arr[stop:len(arr)]
