# Removing duplicates in the sorted array
def remdup(arr):
    j=0
    for i in range(len(arr)):
        if arr[i]!=arr[i-1]:
            arr[j]=arr[i]
            j+=1

    return arr[:j]
arr=[1,1,1,2,2,3,3,3,3,4,4]
print(remdup(arr))
# Time complexity O(N)
# space complexity O(N) , want to achieve O(1) means avoid slicing bcz it creates a new list
