#Linear search is a simple search algorithm that checks each element in a list or array
# sequentially until it finds the target value or reaches the end of the list.
#When to use:
'''for small datasets or when the data is unsorted and random access is not available.'''
'''just as effective and easier to use when you have only a few items to search through.'''
'''small amounts of data, the extra work required by more complicated search algorithms isn't worth it.'''
#Time Complexity
#Worst Case:O(n) - The target value is either at the last position or not present at all.
#Best Case: O(1) - The target value is at the first position

def linear_search(arr,t):
    for i in range(len(arr)):
        if arr[i]==t:
            return i
    return "target not found"
arr=[1,10,32,11,44,2,100,7]
t=7
print(linear_search(arr,t))