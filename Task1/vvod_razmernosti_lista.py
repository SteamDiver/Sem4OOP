array = [1, 16, 4, 10, 7, 11, 1, -2]
# логика приложения
minimum = len(array)
base_item_index = -1
base_delta = 0

for i in range(len(array) - 1):
    for j in range(i + 1, len(array) - 1):
        delta = (array[j] - array[i]) / (j - i)
        if delta.is_integer():
            counter = 0
            for k in range(0, len(array) - 1):
                if array[k] != array[i] - (i - k) * delta:
                    counter += 1

            if counter < minimum:
                minimum = counter
                base_item_index = i
                base_delta = delta

print(minimum)

for i in range(len(array) - 1):
    if array[i] != array[base_item_index] - (base_item_index - i) * base_delta:
        array[i] = array[base_item_index] - (base_item_index - i) * base_delta

print(array)