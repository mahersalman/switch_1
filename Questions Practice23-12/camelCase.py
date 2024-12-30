"""
Camelcase
Write a simple camelCase method  for strings. All words (except for the first) must have their first letter capitalized without spaces.

examples :
'camel case'  = > camelCase
'camel' = > camel
'' = > ''
'camel 3lm' => camel3lm

"""


# approach : O(n^2) : loop and slicing
def to_camelCase(str):
    str = str.lower()
    arr = str.split() 
    if len(arr) == 0 :
        return ''
    
    result = arr[0] 

    for i in range(1,len(arr)): 
        first  = arr[i][0].upper()
        result += first + arr[i][1:]
    
    return result



# approach 2 : O(n) 
def remove_extra_spaces(str):
    result = ""
    current = 0
    while str[current] == " ":
        current+=1

    while current < len(str):
        if str[current] == " ":
            while str[current] == " ":
                current+=1
            result += " "
            continue
        result += str[current]
        current +=1
    return result
            
def to_camelCase_2(str):
    str = remove_extra_spaces(str)
    if len(str) == 0:
        return ''
    
    str = str.lower()

    result = '' 
    i = 0
    while(i < len(str) and str[i] != ' '):
        result += str[i]
        i+=1

    while (i < len(str)):
        if str[i] == ' ' and i+1 < len(str):
            result += str[i+1].upper()
            i+=2
        else:
            result += str[i]
            i+=1
    
    return result


print(to_camelCase_2('   camel  is an animal')) # camelCase


