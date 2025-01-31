def compress(chars):
    w = 0
    r = 0
    while r < len(chars):
        c = chars[r]
        cnt = 0
        while r < len(chars) and c == chars[r]:
            cnt += 1
            r += 1
        chars[w] = c
        w += 1
        if cnt > 1:
            for digit in str(cnt):
                chars[w] = digit
                w += 1
    return chars[:w]


# Example usage:
chars = ["a", "a", "a", "b", "b", "a", "a"]
print(compress(chars))



