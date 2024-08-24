def rotate(arr,k):
    d=len(arr)-k
    return arr[d:]+arr[:d]
'''rotate(),Time Complexity: O(n)
Space Complexity: O(n)'''
def reverse(arr,start,end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr
def rvrse(arr,k):
    n = len(arr)-1
    k = k % n  # Incase k is greater than array length
    reverse(arr, 0, n)
    reverse(arr, 0, k-1)
    reverse(arr, k, n)
    return arr

arr=[1,2,3,4,5,6,7,8]
k=3
print(rvrse(arr, k))

'''rvrse()Time Complexity: O(n)
Space Complexity: O(1)'''
