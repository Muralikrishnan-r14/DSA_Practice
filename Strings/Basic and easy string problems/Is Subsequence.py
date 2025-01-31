def isSubsequence(s: str, t: str) -> bool:
    i = 0
    for char in t:
        if i < len(s):
            if char == s[i]:
                    i += 1
    return i == len(s) # Instead using ifelse use Equality operator it defaultly return 0's and 1's
'''if i == len(s):
    return True
else:
    return False'''
s = ""
t = "abc"
print(isSubsequence(s, t))