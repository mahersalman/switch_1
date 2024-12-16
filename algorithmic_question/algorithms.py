
# time O(n+m)
# space worst cast - O(max(n,m))
def find_common_elements(arr1,arr2):
    commonArray = set()
    visited = set(arr1)
    for i in arr2:
        if i in visited:
            commonArray.add(i)
    return list(commonArray)

#time - O(nlogn + mlogm) 
#space - O(1)
def find_common_elements_approch2(arr1,arr2):
    arr1.sort()
    arr2.sort()
    
    index1,index2 = 0,0
    while index1 < len(arr1) and index2 < len(arr2):
        if arr1[index1] == arr2[index2]:
            print(arr1[index1])
            current = arr1[index1]
            while index1 < len(arr1) and arr1[index1] == current:
                index1+=1
            while index2 < len(arr2) and arr2[index2] == current:
                index2+=1
            continue
        if arr1[index1] > arr2[index2]:
            index2+=1
        else :
            index1+=1
    




    
# arr1 = [1, 2, 3, 4, 5,12]
# arr2 = [4, 5 ,12,6, 7, 8]

# common_elements = find_common_elements(arr1, arr2)
# print(common_elements) 



def find_common_elements_3(arr1,arr2,arr3):
    common1 = find_common_elements(arr1,arr2)
    return find_common_elements(arr3,common1)


# arr1 = [1, 2 , 3, 4, 5,12]
# arr2 = [4, 5 ,12,6, 7, 8]
# arr3 = [7, 4 , 9]
# common_elements = find_common_elements_3(arr1, arr2,arr3)
# print(common_elements) 


# ______________

# Count vowels

    
def count_vowels(str):
    def is_alpha(s):
        return 'A' <= s <= 'Z' or 'a' <= s <= 'z'
    
    VOWELS = set(['a','e','i','o','u','A','E','I','O','U'])
    vowel_count = 0
    consonant_count = 0

    for i in str:
        if is_alpha(i):
            if i in VOWELS:
                vowel_count+=1
            else:
                consonant_count+=1
    return vowel_count,consonant_count

# vowels, consonants = count_vowels("Hello World ! ")

# # Display the results
# print(f"Number of vowels: {vowels}")
# print(f"Number of consonants: {consonants}")


def median_char(s):
    if len(s) == 0:
        raise ValueError('string must not be empty')
    if len(s) == 1:
        return s[0]
    
    sorted_list = sorted(s) 
    
    median_index = len(sorted_list) // 2
    return sorted_list[median_index]

# print(median_char("question")) 
# print(median_char("median"))
# print(median_char("hello"))


def get_char_score(c):
    return ord(c) - ord('a') + 1

def get_word_score(word):
    score = 0
    for i in word:
        score += get_char_score(i)
    return score

def get_max_score_word(s): 
    highest_score = 0
    highest_word = ''
    words = s.split()

    for word in words :
        curr_score = get_word_score(word)

        if curr_score > highest_score:
            highest_score = curr_score
            highest_word = word

    return highest_word


# # Test case 1
# input_string1 = "the quick brown fox jumps over the lazy dog"
# highest_scoring_word1 = get_max_score_word(input_string1)
# print(highest_scoring_word1)

# # Test case 2
# input_string2 = "hello world this is a test"
# highest_scoring_word2 = get_max_score_word(input_string2)
# print(highest_scoring_word2)
# # Test case 3
# input_string3 = "a quick movement of the enemy will jeopardize five gunboats"
# highest_scoring_word3 = get_max_score_word(input_string3)
# print(highest_scoring_word3)


def largest_of_3(num1,num2,num3):
    max_num = num1
    if max_num < num2 :
        max_num = num2
    if max_num < num3 :
        max_num = num3
    return max_num

#for 32 bit integer
def get_largest_of_2(num1,num2):
    diff = num1 - num2
    sign = (diff >> 31) & 1
    return sign*num2 + (1-sign)*num1

def get_largest_of_3_approach2(num1,num2,num3):
    return get_largest_of_2(get_largest_of_2(num1,num2),num3)

print(get_largest_of_3_approach2(5,3,7))
print(get_largest_of_3_approach2(5,3,1))
print(get_largest_of_3_approach2(5,9,4))


