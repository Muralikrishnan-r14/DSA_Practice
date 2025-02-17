from collections import Counter
def canConstruct(ransomNote,magazine):
    '''t = Counter(ransomNote)

    for char in magazine:
        if char not in t or t[char] == 0:
            return False
        else:
            t[char] = t[char] - 1
    return True'''
    if len(ransomNote) > len(magazine):
        return False
    for c in set(ransomNote):
        if magazine.count(c) < ransomNote.count(c):
            return False
    return True
ransomNote = "aab"
magazine ="aab"
print(canConstruct(ransomNote,magazine))