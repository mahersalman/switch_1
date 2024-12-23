

def find_second_biggest_element(arr):
    if len(arr) < 2:
        return None
    first = second = float('-inf')
    for i in arr:
        if i > first:
            second = first
            first = i
        elif first > i > second:
            second = i
    return second if second != float('-inf') else None

print(find_second_biggest_element([1, 2, 3, 4, 5]))  # Output: 4
print(find_second_biggest_element([5, 4, 3, 2, 1]))  # Output: 4
print(find_second_biggest_element([1, 2, 2, 3, 3]))  # Output: 2
print(find_second_biggest_element([1]))              # Output: None
print(find_second_biggest_element([]))               # Output: None
print(find_second_biggest_element([10, 10, 9]))      # Output: 9
print(find_second_biggest_element([10, 10, 10]))     # Output: None