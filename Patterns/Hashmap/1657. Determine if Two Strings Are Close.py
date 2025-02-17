from collections import Counter
def closeStrings(word1, word2):
    a = Counter(word1)
    b = Counter(word2)
    return sorted(a.values()) == sorted(b.values())
print(closeStrings('abc', 'bca'))
