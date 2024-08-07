# type 1
def larger_element(arr):
    max_pos = 0
    for i in range(len(arr)):
        if max_pos < (arr[i]):
            max_pos=arr[i]
    return max_pos
# type 2
def larger_element2(arr):
    s=arr.sort()
    return s[-1]
# type 3
def larger_element3(arr):
    return max(arr)

if __name__=="__main__":
    arr = [2, 6, 1, 4, 8, 3, 11, 0, 21, 19]
    print(larger_element(arr))

