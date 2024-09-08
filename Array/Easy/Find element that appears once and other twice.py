def cnt(arr, n):
    dt = {}
    for i in range(n):
        dt[arr[i]] = dt.get(arr[i], 0)+1
    for i, n in dt.items():
        if n == 1:
            return i
arr = [1, 2, 2, 1, 4]
print(cnt(arr, n = len(arr)))


