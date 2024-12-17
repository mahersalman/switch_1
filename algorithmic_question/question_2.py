#Find the first non-repeating character



def find_first_non_repeating_char(s):
    char_appearance = {}

    for curr in range(len(s)):
        if s[curr] not in char_appearance:
            char_appearance[s[curr]] = set([curr])
        else:
            char_appearance[s[curr]].add(curr)

    for curr in range(len(s)):
        if len(char_appearance[s[curr]]) == 1:
            return s[curr]
    return None


#  # Test cases
# print(find_first_non_repeating_char("swiss"))  # Output: "w"
# print(find_first_non_repeating_char("hello"))  # Output: "h"
# print(find_first_non_repeating_char("aabbcc"))  # Output: None
# print(find_first_non_repeating_char("alphabet"))  # Output: "l"
# print(find_first_non_repeating_char("racecar"))  # Output: "e"
# print(find_first_non_repeating_char("aabbc"))  # Output: "c"



def get_char_of_length(s):
    i = 0
    char_of_length = ''
    while i < len(s):
        j = i+1
        count = 1
        while j < len(s) and s[j] == s[i]:
            count+=1
            j+=1
        char_of_length += f"{s[i]}{count}"
        i+= count

    return char_of_length        

print(get_char_of_length('aaabbcb'))