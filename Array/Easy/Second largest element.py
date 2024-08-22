# Finding the Secondlargest element in the array
# Without using any inbuilt functions
def second_largest(arr):
    second_larges = largest = float('-inf')
    second_smallest = smallest = float('inf')
    for num in arr:
        if num > largest:
            second_larges = largest
            largest = num
        elif num > second_larges and num != largest:
            second_larges = num
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num<second_smallest and num != smallest:
            second_smallest = num
    return [second_smallest, second_larges]

# Using inbuilt functions
def inbuilt(arr):
    arr.sort()
    return[arr[1],arr[-2]]
# Using min max function
def inbuilt2(arr):
    arr.remove(max(arr))
    arr.remove(min(arr))
    return [max(arr),min(arr)]
arr=[7,2,9,8,3,11,4,6,10]
print(inbuilt(arr))


