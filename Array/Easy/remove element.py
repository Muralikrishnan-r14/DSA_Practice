def removeElement(nums, val):
    v = 0
    for num in nums:
        if num != val:
            nums[v] = num
            v += 1
    return v
nums = [3,2,2,3]
val = 3
print(removeElement(nums, val))
