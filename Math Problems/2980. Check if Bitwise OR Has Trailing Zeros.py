def hasTrailingZeros(nums):
    cnt = 0
    for num in nums:
        if bin(num)[-1] == '0':
            cnt += 1
        if cnt >= 2:
            return True
    return False
nums = [1,2,3,4,5]
print(hasTrailingZeros(nums))