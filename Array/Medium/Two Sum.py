# nums = [1,2,4,7,9,11], target = 20
# output = [4, 5] return the index of the two  sum two values of num variable
def twoSum(nums, target):
    hmap = {}
    for i in range(len(nums)):
        c = target - nums[i]
        if c in hmap:
            return [hmap[c], i]
        hmap[nums[i]] = i
nums = [1,2,4,7,9,11]
target = 20
print(twoSum(nums, target))



