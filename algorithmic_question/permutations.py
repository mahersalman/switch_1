"""
Permutations of a String
Problem: Write a function to generate all possible permutations of a given string.
Example Input: permutations("abc")
Expected Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

"""
"""
            abc[cba,cab,bca,bac,acb,abc]
  ab = [ab,ba]          ac[ac,ca]           bc[bc,cb]
    [a] [b]                  [a] [c]     [b] [c]

T(n) = n*T(n-1) + O(n)
"""
def get_permutations(str): 
    if len(str) == 0 :
        return []
    if len(str) == 1:
        return [str]
    
    permutations = []
    for i in range(len(str)):
        for sub_permutation in get_permutations(str[:i] + str[i+1:]):
            permutations.append(str[i] + sub_permutation)
    return permutations

print(get_permutations('abc'))















