def palindrome(x):
    return str(x) == str(x)[::-1]
x = -121
print(palindrome(x))