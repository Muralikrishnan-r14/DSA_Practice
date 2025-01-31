def increasingTriplet(nums):
    first = inf
    second = inf 
    for i in range(2,len(nums)):
        if nums[i] <= first:
            first = nums[i]
        elif nums[i] <= second:
            second = nums[i]
        elif nums[i] > second:
            return True
    return False
nums = [2,1,5,0,3]
print(increasingTriplet(nums))