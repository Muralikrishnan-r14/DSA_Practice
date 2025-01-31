def maxOperations(nums,k):
    hsh_mp = {}
    pairs = 0
    for num in nums:
        c = k - num
        if c in hsh_mp and hsh_mp.get(c, 0) > 0:
            pairs += 1
            hsh_mp[c] -= 1
        else:
            hsh_mp[num] = hsh_mp.get(num, 0) + 1
    return pairs
nums = [3,1,3,4,3]
k = 6
print(maxOperations(nums, k))