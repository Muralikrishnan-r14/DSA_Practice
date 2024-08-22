# we have to rotate the array, left rotate the array by one place
def rotate(arr):
    temp=arr[0]
    arr.pop(0)
    arr.append(temp)
    return arr
arr = [1, 2, 3, 4, 5]
print(rotate(arr))
'''Time complexity:Removing the first element of a list involves shifting all remaining elements one position to the left. 
This operation takes 𝑂(𝑛) time , n is number of elements in the list'''

'''Space complexity:single additional variable, temp which requires O(1) space.'''