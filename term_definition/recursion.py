

#1 Fibonachii 

def get_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return get_fibonacci(n-1) + get_fibonacci(n-2)
    
print(get_fibonacci(6))

#2 find all subset

def get_all_subsets(s):
    if len(s) == 0:
        return [[]]
    else:
        sub_permutation = get_all_subsets(s[1:])
        return sub_permutation + [[s[0]] + i for i in sub_permutation]

print(get_all_subsets([1,2]))