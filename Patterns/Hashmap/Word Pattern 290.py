from collections import defaultdict
def wordPattern(pattern,s):
    c = s.split()
    hsh_mp = defaultdict(str)
    if len(set(pattern)) != len(set(c)) or len(c) != len(pattern):
        return False
    for i in range(len(pattern)):
        if c[i] in hsh_mp:
            if hsh_mp[c[i]] != pattern[i]:
                return False
        else:
            hsh_mp[c[i]] = pattern[i]
    return True
pattern = "abcbc"
s = "dog cat bag dog bag"
print(wordPattern(pattern,s))