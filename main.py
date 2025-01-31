def missingNumber(nums):
    x = 0
    y = 0
    for i in range(len(nums)):
        x = x ^ nums[i]
        y = y ^ i
    y = y ^ (len(nums) + 1)
    return x ^ y
nums = [3,0,1]
print(missingNumber(nums))