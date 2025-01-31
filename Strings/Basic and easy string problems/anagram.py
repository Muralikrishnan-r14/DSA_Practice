def isAnagram(s: str, t: str):
    j = set(s)
    v = 0
    for char in t:
        if char in j:
            v += 1
    if len(s) == v:
        return True
    else:
        return False
s = "anagram"
t = "nagaram"
print(isAnagram(s, t))
print(len(s))