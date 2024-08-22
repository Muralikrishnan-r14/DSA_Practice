'''Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.'''
# I/P=[3,0,1], n=3 O/P=2
def missingnumb(arr,n):
    return (n*(n+1))//2 - sum(arr)
arr=[2,0,1]
n=3
print(missingnumb(arr,n))
"Time complexity:O(n)"
"Space complexity:O(1)"