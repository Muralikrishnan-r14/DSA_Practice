def largestAltitude(gain):
    g = 0
    sm = 0
    for num in gain:
        sm += num
        if sm > g:
            g = sm
    return g
gain = [-5,1,5,0,-7]
print(largestAltitude(gain))