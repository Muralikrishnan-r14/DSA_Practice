def merge(arr1, arr2):
    return sorted(arr1+arr2)

'''Time complexity:O((n+m)log(n+m))=O(n+m) for concatenation and O(log(n+m)) for sorting'''
'''Space complexity:O(n+m),Concatenating arr1 and arr2 creates a new list of size n+m and Timsort requires 
O(k) additional space where k=n+m for storing temporary data during the sort.'''

def mergwthtinblt(arr1, arr2):
    i = len(arr1)-1
    j = len(arr2)-1
    n = (i+j)+1
    result=[0]*(len(arr1)+len(arr2))
    while n >= 0:
        if i >= 0 and (j < 0 or arr1[i] >= arr2[j]):
            result[n] = arr1[i]
            i -= 1
        elif j >= 0:
            result[n] = arr2[j]
            j -= 1
        n -= 1
    return result
'''TimeComplexity:O(n+m)
SpaceComplexity:O(n+m)'''
arr1 = [-1000, -999, -500, -300, -100, -1, 0, 1, 2, 2, 2, 500, 1000, 1001]
arr2 = [-1001, -1000, -800, -600, -500, -400, -200, 0, 2, 3, 3, 3, 700, 1000, 2000]
print(mergwthtinblt(arr1, arr2))


