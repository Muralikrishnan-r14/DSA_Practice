def reverseVowels(s: str) -> str:
    n = list(s)
    i = 0
    j = len(n) - 1
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    while i <= j:
        if n[i] in vowels and n[j] in vowels:
            n[i], n[j] = n[j], n[i]
            i += 1
            j -= 1
        elif n[i] in vowels:
            j -= 1
        elif n[j] in vowels:
            i += 1
        else:
            i += 1
            j -= 1
    return "".join(n)
s = "IceCreAm"
print(reverseVowels(s))