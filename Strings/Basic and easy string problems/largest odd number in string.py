# Input: num = "52"  Input: num = "4206"   Input: num = "35427"
# Output: "5"        Output: ""            Output: "35427"

def largestOddnumber(num):
    for i in range(len(num)-1,-1,-1):
        # Check if the current digit is odd
        if num[i] in '13579':
            # Return the substring from the start to this position
            return num[:i+1]
    # If no odd digit is found, return an empty string
    return ""


num = '35427'
print(largestOddnumber(num))

'''Time Complexity: O(n), where n is the length of the string. The function scans through the string
from the end to the beginning once.
Space Complexity: O(1). The space used is constant, apart from the return value.'''