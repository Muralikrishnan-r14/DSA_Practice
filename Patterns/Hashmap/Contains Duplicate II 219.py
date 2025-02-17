def containsNearbyDuplicates(nums, k):
    window = set()
    l = 0
    for i in range(len(nums)):
        if i-l > k:
            window.remove(nums[l])
            l += 1
        if nums[i] in window:
            return True
        window.add(nums[i])
    return False
nums = [1,2,3,1]
k = 3
nums1 = [1,2,3,1,2,3]
k1 = 2
print(containsNearbyDuplicates(nums1, k1))


