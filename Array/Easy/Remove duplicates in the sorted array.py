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
