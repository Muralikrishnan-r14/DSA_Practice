def rotatearr(nums, k):
    k = k % len(nums)
    l, r = 0, len(nums) - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1
    l, r = k , len(nums) - 1
    while l < r :
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1
    l, r = 0, k-1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1


    return nums

nums = [1,2,3,4,5,6,7,8]
print(rotatearr(nums, 3))























'''n = len(nums)
    for j in range(n - 1, (n-k)-1, -1):
        lst_element = nums[n - 1]
        nums.remove(lst_element)
        nums.insert(0, lst_element)
    return nums'''