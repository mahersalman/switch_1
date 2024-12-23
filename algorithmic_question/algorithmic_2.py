#Odd number of times  
#Given an array, find the int that appears an odd number of times


def find_first_char_appears_odd_times(arr):
    result = {}
    for i in arr :
        result[i] = result.get(i,0) + 1

    for i in arr :
        if result[i]%2 == 1:
            return i
    return None


#print(find_first_char_appears_odd_times('abcabdefdefcc'))


def find_char_appears_odd_times(arr):
    result = 0
    for i in arr:
        result ^= ord(i)
    return chr(result) 

#print(find_char_appears_odd_times('abcabdefdefcc'))



#Find in a sorted array the closest number to a given number

def find_closest_number(arr,target):
    closest = arr[0]
    for i in range(1,len(arr)):
        if abs(target-arr[i]) < abs(target - closest):
            closest = arr[i]
    return closest


def find_closest_number_2(arr,target):
    left, right = 0 , len(arr)-1
    closest = arr[(left + right)//2]
    while left <= right:
        mid = (right + left)//2
        if abs(target - closest) > abs(target - arr[mid]):
            closest = arr[mid] 
        if arr[mid] == target :
            return arr[mid]
        elif arr[mid] > target:
            right = mid-1
        else:
            left = mid+1
    return closest


# Test cases for find_closest_number_2
print(find_closest_number([1, 2, 3, 4, 5, 8, 9], 8))  # Output: 8
print(find_closest_number([1, 2, 3, 4, 5, 8, 9], 7))  # Output: 8
print(find_closest_number([1, 2, 3, 4, 5, 8, 9], 6))  # Output: 5
print(find_closest_number([1, 2, 3, 4, 5, 8, 9], 10)) # Output: 9
print(find_closest_number([1, 2, 3, 4, 5, 8, 9], 0))  # Output: 1
print(find_closest_number([1, 2, 3, 4, 5, 8, 9], 4))  # Output: 4

print ('____')
# Test cases for find_closest_number_2
print(find_closest_number_2([1, 2, 3, 4, 5, 8, 9], 8))  # Output: 8
print(find_closest_number_2([1, 2, 3, 4, 5, 8, 9], 7))  # Output: 8
print(find_closest_number_2([1, 2, 3, 4, 5, 8, 9], 6))  # Output: 5
print(find_closest_number_2([1, 2, 3, 4, 5, 8, 9], 10)) # Output: 9
print(find_closest_number_2([1, 2, 3, 4, 5, 8, 9], 0))  # Output: 1
print(find_closest_number_2([1, 2, 3, 4, 5, 8, 9], 4))  # Output: 4