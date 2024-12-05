
def CompareAsPalindromic(x,y):
    def isPalindrome(z):
        return str(z) == str(z)[-1::-1]
    if isPalindrome(x) == isPalindrome(y):
        return x > y
    return not isPalindrome(x)

def compare(x,y,type):
    n = 5
    comparison_functions = {
        'asc'              : lambda x,y: x > y ,
        'desc'             : lambda x,y: x < y ,
        'diffFromN'        : lambda x,y : n-x > n-y,
        'palindromic-first': lambda x,y : CompareAsPalindromic(x,y)
    }
    return comparison_functions[type](x,y)


def bubble_sort(arr,type = 'asc'):
    for i in range(len(arr)-1, 0 , -1):
        for j in range(1,i+1):
            if compare(arr[j-1],arr[j],type):
                arr[j-1] ,arr[j] = arr[j] , arr[j-1]

arr1 = [38, 27, 43, 3, 9, 82, 10]
arr2 = [1, 4, 2, 8, 5, 7]
arr3 = [12, 11, 13, 5, 6, 7,-2,9,-9]
arr4 = []
arr5 = [1]

bubble_sort(arr1)
bubble_sort(arr2)
bubble_sort(arr3)
bubble_sort(arr4)
bubble_sort(arr5)


print(arr1)
print(arr2)
print(arr3)
print(arr4)
print(arr5)


# Arrays suitable for each type
arr_asc = [38, 27, 43, 3, 9, 82, 10]
arr_desc = [1, 4, 2, 8, 5, 7]
arr_diffFromN = [12, 11, 13, 5, 6, 7,-2,9,-9]

arr_palindromic = [121, 131, 20, 11, 22, 33]

# Sorting and printing for each type
bubble_sort(arr_asc, type='asc')
print('asc : ')
print(arr_asc)

bubble_sort(arr_desc, type='desc')
print('desc : ')
print(arr_desc)

bubble_sort(arr_diffFromN, type='diffFromN')
print('diffFromN : ')
print(arr_diffFromN)

bubble_sort(arr_palindromic, type='palindromic-first')
print('palindromic-first : ')
print(arr_palindromic)