def container_with_most_water(arr):
    ''' res = 0
    # BRUTEFORCE SOLN
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            area = (j - i) * min(arr[i], arr[j])
            res = max(res, area)
    return res
    TC O(N^2), SC O(1) '''
    res = 0
    l,r = 0, len(arr)-1
    while l < r:
        area = (r - l) * min(arr[l], arr[r])
        res = max(res, area)
        if arr[l] < arr[r]:
            l += 1
        else:
            r -= 1
    return res
    # Tc O(N), SC O(1)

height = [1,8,6,2,5,4,8,3,7]
print(container_with_most_water(height))