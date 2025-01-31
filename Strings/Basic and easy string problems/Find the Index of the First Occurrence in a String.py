def strStr(haystack: str, needle: str) -> int:
    index = -1
    ln = 0
    i = 0
    for ind, char in enumerate(haystack):
        for chars in range(i, len(needle)):
            if char == needle[chars] and ln == 0:
                index = ind
                ln += 1
                i += 1
                break
            elif char == needle[chars]:
                ln += 1
                i += 1
                if ln == len(needle):
                    return index
                break
            else:
                ln = 0
                i = 0
                index = -1
                break

    return -1
haystack = "mississippi"
needle = "issip"
print(strStr(haystack, needle))
