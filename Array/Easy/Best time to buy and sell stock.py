def bst(nums):
    minn = nums[0]
    maxx = 0
    for i in range(len(nums)):
        minn = min(minn, nums[i])
        maxx = max(maxx, nums[i] - minn)
    return maxx
prices = [7,6,4,3,1]
print(bst(prices))