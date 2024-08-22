# without using any inbuilt functions
def arry1(arr):
    for i in range(1,len(arr)):
        if arr[i]>arr[i-1]:
            pass
        else:
            return False
    return True
''' Time complexity: O(N)
    space complexity:O(1)'''
# Using inbuilt sort function
# sorted returns the new list that is sorted ,leaving the original list unchanged
def arry2(arr):
    s=sorted(arr)
    if arr == s:
        return True
    else:
        return False
''' Time complexity: O(N log N)
    space complexity:O(N)'''
arr=[1,2,3,4,6]
print(arry2(arr))