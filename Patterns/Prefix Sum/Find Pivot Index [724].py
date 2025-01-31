def pivotIndex1(nums):
    forward = 0
    backward = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if j < i:
                forward += nums[j]
            elif j > i:
                backward += nums[j]
        if forward == backward:
            return i
        forward = 0
        backward = 0

    return -1

def pivotIndex(nums):
    total = sum(nums)
    curr_sum = 0
    for num in nums:
        if total - (curr_sum + num) == curr_sum:
            return num
        curr_sum += num
    return -1
nums = [1,7,3,6,5,6]
print(pivotIndex(nums))