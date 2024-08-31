# Input: s = "the sky is blue"
# Output: "blue is sky the"
# Using standard library
def reverseWordsString(st):
    s = st.split()  # Tc : O(n)
    words = s[::-1] # Sc : O(n)
    return ''.join(words)
# without using libraries
def reverseWords(st):
    ans = []   # TC : O(n)
    temp = ""  # SC : O(n)
    for ch in st:
        if ch != " ":
            temp += ch
        elif temp != "":
            ans.append(temp)
            temp = ""
    if temp != "":
        ans.append(temp)
    return ' '.join(ans)

st = "the sky is blue"
print(reverseWords(st))
