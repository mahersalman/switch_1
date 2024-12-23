
# Brute Force - O(n^2)
def shift_str(str):
    return str[-1] + str[:-1]

def is_Rotation(cycle, str):
    if not cycle and not str :
        return True
    if len(cycle) != len(str):
        return False
    
    for i in range(len(cycle)):
        if cycle == str :
            return True
        str = shift_str(str)
    return False



# Optimal - > O(n) 
def is_Rotation(cycle, str):
    if not cycle and not str :
        return True
    if len(cycle) != len(str):
        return False
    
    return str in (cycle + cycle)

    

