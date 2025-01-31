'''Input: arr = [1,2,2,1,1,3]
Output: true
Explanation:
The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.'''

def uniqueOccurrences(arr):
    hsh_mp = {}
    for nums in arr:
        hsh_mp.get(nums, 1) + 1
    v = hsh_mp.values()
    s = set(v)
    print(s,v)
    return v == s

arr = [1,2,2,1,1,3]
print(uniqueOccurrences(arr))