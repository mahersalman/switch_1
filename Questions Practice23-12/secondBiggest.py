

def find_second_biggest_element(numbers):
    if len(numbers) < 2:
        return None
    first = second = float('-inf')
    for curr in numbers:
        if curr > first:
            second = first
            first = curr
        elif first > curr > second:
            second = curr
    return second if second != float('-inf') else None

print(find_second_biggest_element([1, 2, 3, 4, 5]))  # Output: 4
print(find_second_biggest_element([5, 4, 3, 2, 1]))  # Output: 4
print(find_second_biggest_element([1, 2, 2, 3, 3]))  # Output: 2
print(find_second_biggest_element([1]))              # Output: None
print(find_second_biggest_element([]))               # Output: None
print(find_second_biggest_element([10, 10, 9]))      # Output: 9
print(find_second_biggest_element([10, 10, 10]))     # Output: None