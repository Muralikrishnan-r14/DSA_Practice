def product_array(nums):
    l_multr = 1
    r_multr = 1
    n = len(nums)
    l_arr = [0] * n
    r_arr = [0] * n
    for i in range(n):
        j = -i - 1
        l_arr[i] = l_multr
        r_arr[j] = r_multr
        l_multr = l_multr * nums[i]
        r_multr = r_multr * nums[j]
    return [l * r for l, r in zip(l_arr, r_arr)]
arr = [1,2,3,4]
print(product_array(arr))