def mirror (arr):
    for i in range(0, len(arr)):
        for j in range (i, len(arr[i])):
            t = arr[i][j]
            arr[i][j] = arr[j][i]
            arr[j][i] = t
    return arr
