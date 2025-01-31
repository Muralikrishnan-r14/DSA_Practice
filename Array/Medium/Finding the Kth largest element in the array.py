import heapq
def minheap(nums,k):
    if k>len(nums):
        return "list index out of range"
    for i in range(k,len(nums)):
        heapq.heapify(nums)
        if i<k:
            heapq.heappush(nums[i])
        heapq.heappop(nums)
    return nums[0]
nums = [9, 12, 2, 4, 7, 6, 3]
k = 7
print(minheap(nums, k))