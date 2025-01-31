def removeDuplicates(nums):
    left = 0
    for i in range(len(nums)):
        if nums[i] > nums[left]:
            left += 1
            nums[left] = nums[i]
    return left + 1
nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))