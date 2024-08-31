#Input S = "(()())(())"
# Output "()()()"
def removeOutermostParanthese(s):
    ans = ''  # TC : O(n^2) due to string concatenation
    cnt = 0   # SC : O(n)
    for ch in s:
        if ch == '(':
            if cnt:
                ans += ch
            cnt += 1
        else:
            cnt -= 1
            if cnt:
                ans += ch
    return ans

# optimising Time Complexity for this code using list
def removeOutermostParanthesesOptsoln(s):
    cnt = 0   # TC : O(n)
    ans = []  # SC : O(n)
    for ch in s:
        if ch == '(':
            if cnt:
                ans.append(ch)
            cnt += 1
        else:
            cnt -= 1
            if cnt:
                ans.append(ch)
    return ''.join(ans)
S = "(()())(())"
print(removeOutermostParanthesesOptsoln(S))

