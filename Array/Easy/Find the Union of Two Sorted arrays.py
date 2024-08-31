def union_brut(arr1, arr2):
    freq = {}        # TC : O(n1+n2)
    union = []       # SC : O(n1+n2)
    for num in arr1:  # O(n1)
        freq[num] = freq.get(num, 0)+1
    for num in arr2:  # O(n2)
        freq[num] = freq.get(num, 0)+1
    for num in freq:  # O(n1+n2)
        union.append(num)
    return union

def union_better(arr1, arr2):
    s = set()                  # TC : O(n1+n2)
    for num in arr1:           # SC : O(n1+n2)
        s.add(num)
    for num in arr2:
        s.add(num)
    return list(s)




def find_union(arr1, arr2):
    i, j = 0, 0  # Pointers
    union = []  # Union list

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:  # Case 1 and 2
            if len(union) == 0 or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1
        else:  # Case 3
            if len(union) == 0 or union[-1] != arr2[j]:
                union.append(arr2[j])
            j += 1

    while i < len(arr1):  # If any elements left in arr1
        if union[-1] != arr1[i]:
            union.append(arr1[i])
        i += 1

    while j < len(arr2):  # If any elements left in arr2
        if union[-1] != arr2[j]:
            union.append(arr2[j])
        j += 1
    return union
arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [2, 3, 4, 4, 5, 11, 12]

union = find_union(arr1, arr2)

print("Union of arr1 and arr2 is:")
print(union)

