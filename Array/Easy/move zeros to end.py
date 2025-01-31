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

'''i = 0
        j = 1
        while i < len(nums) and j < len(nums):
            if nums[i] == 0 and nums[j] != 0:
                nums[i],nums[j] = nums[j],nums[i]
                i += 1
                j += 1
            elif nums[i] != 0 and nums[j] != 0:
                i += 1
                j += 1
            elif nums[i] != 0 and nums[j] == 0:
                i += 1
                j += 1
            elif nums[j] == 0:
                j += 1
            elif nums[i] == 0:
                i += 1
        return nums'''
