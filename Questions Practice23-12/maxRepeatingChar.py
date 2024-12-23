
def find_first_max_repeating_char(str):
    counter = {}
    max_repeating = 0
    for c in str:
        counter[c] = counter.get(c,0) + 1
        if counter[c] > max_repeating:
            max_repeating = counter[c]
    
    for c in str:
        if counter[c] == max_repeating:
            return c
    return None

# Test cases
print(find_first_max_repeating_char("hello"))         
print(find_first_max_repeating_char("test"))           
print(find_first_max_repeating_char("aabbcc"))         
print(find_first_max_repeating_char("aabbccc"))        
print(find_first_max_repeating_char("abcabcabc"))      
print(find_first_max_repeating_char("a"))              
print(find_first_max_repeating_char(""))               
print(find_first_max_repeating_char("abacabad")) 