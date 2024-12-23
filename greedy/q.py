

def check_negative_array(arr):
    for i in arr:
        if i > 0:
            return True
    return False

def max_sum_sequence(arr):
    max_sum = 0
    max_seq = []

    curr_sum = 0
    curr_seq = []

    if not check_negative_array(arr):
        return [max(arr)]
    
    for i in arr:
        if i < 0 :
            if curr_sum > max_sum:
                max_sum = curr_sum
                max_seq = curr_seq
                curr_seq = []
                curr_sum = 0
        else:
            curr_sum += i 
            curr_seq.append(i)

    return curr_seq if curr_sum > max_sum else max_seq


print(max_sum_sequence([2,-2,3,4]))
print(max_sum_sequence([-5,-2,-1,-9]))
print(max_sum_sequence([1,2,6,9]))