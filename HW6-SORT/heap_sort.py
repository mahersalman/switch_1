
def sum_of_digits(x):
    x = abs(x)
    sum = 0
    while x > 0 :
        sum += x%10
        x /= 10
    return sum

def is_perfect_number(num):
    if num <= 0:
        return False
    divisor_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisor_sum += i
    return divisor_sum == num


def sort_Operation(element1,element2,type):
    comprehension_function = {
        'asc' : lambda x,y : x < y,
        'desc': lambda x,y : x > y,
        'sumOfDigits' : lambda x,y : x < y if sum_of_digits(x) == sum_of_digits(y) 
                                else sum_of_digits(x) < sum_of_digits(y) ,
        'perfectFirst': lambda x,y : x < y if is_perfect_number(x) == is_perfect_number(y) 
                                        else is_perfect_number(x)
    }
    return comprehension_function[type](element1,element2)

def heapify_down(arr,index , N,type):
    largest = index
    while True:
        left  = 2 * index +1
        right = 2 * index +2

        if left <= N and sort_Operation(arr[largest] , arr[left],type):
            largest = left
        if right <= N and sort_Operation(arr[largest] , arr[right],type):
            largest = right
        
        if largest == index:
            break
        arr[largest],arr[index] = arr[index] , arr[largest]
        index = largest


def heap_sort(arr,type = 'asc'):
    N = len(arr)-1
    for i in range((N-1)//2 , -1,-1):
        heapify_down(arr,i,N,type)
    
    for i in range(N,0,-1):
        arr[0],arr[i] = arr[i],arr[0]
        heapify_down(arr,0,i-1,type)
    

# Arrays suitable for each type
arr_asc = [38, 27, 43, 3, 9, 82, 10]
arr_desc = [1, 4, 2, 8, 5, 7]
arr_sumOfDigits = [123, 4, 56,29, 789, 12, 345]
arr_perfectFirst = [6, 28, 496, 12, 18, 20]

# Sorting and printing for each type
heap_sort(arr_asc, type='asc')
print('asc : ')
print(arr_asc)

heap_sort(arr_desc, type='desc')
print('desc : ')
print(arr_desc)

heap_sort(arr_sumOfDigits, type='sumOfDigits')
print('sumOfDigits : ')
print(arr_sumOfDigits)

heap_sort(arr_perfectFirst, type='perfectFirst')
print('perfectFirst : ')
print(arr_perfectFirst)
