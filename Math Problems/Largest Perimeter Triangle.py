def largestPerimeterTriangle(n):
    numb = sorted(n, reverse =True)
    for i in range(len(numb) - 2):
        if numb[i] < numb[i+1] + numb[i+2]:
            return numb[i] + numb[i+1] + numb[i+2]
    return 0
print(largestPerimeterTriangle([1,2,1,10]))


