def mrge(s,v):
    op = ""
    i = 0
    j = 0
    while i < len(s) and j <len(v):
        op += s[i] + v[j]
        i += 1
        j += 1
    while i < len(s):
        op += s[i]
        i += 1
    while j < len(v):
        op += v[j]
        j += 1
    return op
s = "abcd"
j = "klmnopqrst"
print(mrge(s,j))