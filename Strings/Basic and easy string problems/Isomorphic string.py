# Input: s = "egg", t = "add"   Input: s = "foo", t = "bar"   Input: s = "paper", t = "title"
# Output: true                  Output: false                 Output: true

def is_isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    # Dictionaries to store character mappings
    s_to_t_mapping = {}
    t_to_s_mapping = {}

    for c1, c2 in zip(s, t):
        if c1 in s_to_t_mapping:
            print(s_to_t_mapping[c1])
            if s_to_t_mapping[c1] != c2:
                return False
        else:
            s_to_t_mapping[c1] = c2

        if c2 in t_to_s_mapping:
            if t_to_s_mapping[c2] != c1:
                return False
        else:
            t_to_s_mapping[c2] = c1

    return True

# Example usage:
s1 = "adi"
s2 = "egg"
print(is_isomorphic(s1, s2))  # Output: True

s1 = "foo"
s2 = "boo"
print(is_isomorphic(s1, s2))  # Output: False
