import math

def is_uppercase(s):
    return 'A' <= s <= 'Z'
def is_even(num):
    return num%2 == 0
def is_prime(num):
    if num <= 1 or is_even(num):
        return False
    if num <= 3 :
        return True
    for i in range(3,int(math.sqrt(num))+1,2):
        if num%i == 0 :
            return False
    return True


def compare(element1,element2,type):
    comparison_functions = {
        'asc'      : lambda x,y : x < y ,
        'desc'     : lambda x,y : x > y ,
        'abs'      : lambda x,y : abs(x) < abs(y),
        'capital'  : lambda x,y : x < y if (is_uppercase(x) == is_uppercase(y)) 
                                    else is_uppercase(x),
        'odd_even' : lambda x,y : x < y if (is_even(x) == is_even(y))
                                    else not is_even(x),
        'prime'    : lambda x,y : x < y if (is_prime(x) == is_prime(y))
                                    else is_prime(x)
    }
    return comparison_functions[type](element1,element2)

def merge(arr,left, mid ,right,type):
    curr_left = left
    curr_right = mid+1

    newArray = []
    while curr_left <= mid and curr_right <= right:
        if compare(arr[curr_left],arr[curr_right],type):
            newArray.append(arr[curr_left])
            curr_left+=1
        else:
            newArray.append(arr[curr_right])
            curr_right+=1
    
    while curr_left <= mid:
        newArray.append(arr[curr_left])
        curr_left+=1
    while curr_right <= right:
        newArray.append(arr[curr_right])
        curr_right+=1

    for i in range(len(newArray)):
        arr[left+i] = newArray[i]


def merge_sort(arr,left = None,right = None , type = 'asc'):
    if left is None or right is None:
        left = 0
        right = len(arr)-1

    if left >= right:
        return 
    
    mid = (left + right)//2
    merge_sort(arr,0,mid,type)
    merge_sort(arr,mid+1,right,type)
    merge(arr,left,mid,right,type)



# Arrays suitable for each type
arr_asc = [38, 27, 43, 3, 9, 82, 10]
arr_desc = [1, 4, 2, 8, 5, 7]
arr_abs = [-12, 11, -13, 5, -6, 7]
arr_capital = ['a', 'B', 'c', 'D', 'e', 'F']
arr_odd_even = [12, 11, 13, 5, 6, 7]
arr_prime = [10, 3, 4, 7, 6, 11]

# Sorting and printing for each type
merge_sort(arr_asc, type='asc')
print('asc : ')
print(arr_asc)

merge_sort(arr_desc, type='desc')
print('desc : ')
print(arr_desc)

merge_sort(arr_abs, type='abs')
print('abs : ')
print(arr_abs)

merge_sort(arr_capital, type='capital')
print('capital : ')
print(arr_capital)

merge_sort(arr_odd_even, type='odd_even')
print('odd_even : ')
print(arr_odd_even)

merge_sort(arr_prime, type='prime')
print('prime : ')
print(arr_prime)