def lengthOfLongestSubstring(s):
    l = 0
    longest = 0
    sett = set()
    for i in range(len(s)):
        while s[i] in sett:
            sett.remove(s[l])
            l += 1
        w = (i - l) + 1
        longest = max(longest, w)
        sett.add(s[i])
    return longest
s = "dvdf"
print(lengthOfLongestSubstring(s))

''' import math
    cnt = 0
    res = -math.inf
    seen = set()
    for i in range(len(s)):
        if s[i] not in seen:
            cnt += 1
            seen.add(s[i])
            res = max(res, cnt)
        else:
            seen = set()
            cnt = 1
            seen.add(s[i])
    return res '''