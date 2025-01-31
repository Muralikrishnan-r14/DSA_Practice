def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    i = 0
    j = 1
    while  i < len(nums) and j < len(nums):
        if nums[i] == 0 and nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1
        elif nums[i] != 0 and nums[j] != 0:
            i += 1
            j += 1
        elif nums[i] != 0 and nums[j] == 0 :
            i += 1
            j += 1
        elif nums[j] == 0:
            j += 1
        else:
            i += 1
    return nums
nums =[1,0,1]
print(moveZeroes(nums))