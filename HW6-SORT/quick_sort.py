def get_Category(n):
    if n%3 == 0 and n%5 == 0:
        return 3
    elif n%5 == 0:
        return 2
    elif n%3 == 0:
        return 1
    return 0


def advanced_typeOf_sorts(x,y,type):
    n=5
    operation = {
        'divided_5&3'        : lambda x  : get_Category(x),
        'numberOfDigits'     : lambda x  : len(str(x)),
        'reminder'           : lambda x  : x%n
    }
    n1 = operation[type](x)
    n2 = operation[type](y)
    if n1 == n2:
        return x > y
    return n1 > n2

#true if element1 bigger element2 otherwise false
def compare(element1,element2,type):
    comparison_functions = {
        'asc'  : lambda x,y,z: x > y ,
        'desc' : lambda x,y,z: x < y ,
        'divided_5&3'   : lambda x,y,z : advanced_typeOf_sorts(x,y,z),
        'numberOfDigits': lambda x,y,z : advanced_typeOf_sorts(x,y,z),
        'reminder'      : lambda x,y,z : advanced_typeOf_sorts(x,y,z)
    }
    return comparison_functions[type](element1,element2,type)



def partition(arr,left,right,type):
    index = left
    pivot = arr[right]
    for i in range(left,right):
        if compare(pivot, arr[i],type):
            arr[index],arr[i] = arr[i],arr[index]
            index+=1
    arr[index],arr[right] = arr[right],arr[index]
    return index

def quick_sort(arr,left = None, right = None,type = 'asc'):
    if left is None or right is None:
        left = 0
        right = len(arr)-1
    if left >= right:
        return
    
    pivot_index = partition(arr,left,right,type)
    quick_sort(arr,left,pivot_index-1,type)
    quick_sort(arr,pivot_index+1,right,type)
    

 # Example arrays to sort
arr1 = [38, 27, 43, 3, 9, 82, 10]
arr2 = [1, 4, 2, 8, 5, 7]
arr3 = [12, 11, 13, 5, 6, 7]

# Call the merge_sort function on each array
quick_sort(arr1)
quick_sort(arr2,type = 'desc')
quick_sort(arr3)

# Print the sorted arrays
print(arr1)
print(arr2)
print(arr3)


# Example arrays suitable for each comparison type
arr_divided = [15, 10, 9, 30, 5, 3, 1]
arr_digits = [123, 4, 56, 7890, 12, 345]
arr_reminder = [14, 7, 21, 5, 10, 3]

# Sorting and printing for each type
quick_sort(arr_divided, type='divided_5&3')
print('divided_5&3 : ')
print(arr_divided)

quick_sort(arr_digits, type='numberOfDigits')
print('numberOfDigits : ')
print(arr_digits)

quick_sort(arr_reminder, type='reminder')
print('reminder : ')
print(arr_reminder)