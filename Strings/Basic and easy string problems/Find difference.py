def diff(s,t):
    from collections import Counter
    s_counts = Counter(s)
    t_counts = Counter(t)

    for key, val in t_counts.items():

        if key not in s_counts:
            return key

        if key in s_counts.keys() and s_counts[key] < val:
            return key

    return ""
'''s = sorted(s)
    t = sorted(t)
    for i in range(len(s)):
        if s[i] != t[i]:
            return t[i]
    return t[-1]'''
s = "abcd"
t = "abcde"
print(diff(s,t))