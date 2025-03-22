def generate(numRows):
    arr = [[1], [1, 1]]
    for i in range(3, (numRows + 1)):
        curr = [1] * i
        for j in range(1,i - 1):
            c = arr[i-2][j - 1] + arr[i-2][j]
            curr[j] = c
        arr.append(curr)
    return arr
numRows = 5
print(generate(numRows))
