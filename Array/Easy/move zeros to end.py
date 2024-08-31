''' Input:
 1 ,0 ,2 ,3 ,0 ,4 ,0 ,1
Output:
 1 ,2 ,3 ,4 ,1 ,0 ,0 ,0 '''
def move_zeros(arr):
    position = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            if i != position:
                arr[position], arr[i] = arr[i], arr[position]
            position += 1
    return arr
arr=[1, 2, 0, 3, 0, 0, 5]
print(move_zeros(arr))
