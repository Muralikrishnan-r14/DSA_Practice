def ishappy(n):
    visit = set()
    while n not in visit:
        visit.add(n)
        n = sumofsqr(n)
    if n == 1:
        return True
    return False
def sumofsqr(n):
    output = 0
    while n:
        digit = n % 10
        digit = digit ** 2
        output += digit
        n = n // 10
    return output
n = 2
print(ishappy(n))
