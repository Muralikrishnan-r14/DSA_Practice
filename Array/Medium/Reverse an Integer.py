def reverse(x):
    rev = 0
    j = 3
    while j > 0:
        rev = rev * 10 + x % 10
        x //= 10
        j -= 1
    return rev
print(reverse(-123))
