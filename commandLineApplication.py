

def palindrome(txt):
    '''
        check palindrome using two pointers :
          start and end which pointer to first char and last char ,
          then check if char in those indexes is equals and move pointer while start not equal to end.
    '''
    start, end = 0, len(txt)-1
    while start < end:
        if txt[start] != txt[end]:
            return False
        start+=1
        end-=1
    return True

def lower(txt):
    '''
        check if all characters in text is lower case
    '''
    for i in txt:
        if not (i >= 'a' and i <= 'z'):
            return False
    return True

def digit(txt):
    '''
        check if all characters is digits
    '''
    for i in txt:
        if not (i >= '0' and i <= '9'):
            return False
    return True

def long(txt):
    return len(txt) > 15

def empty(txt):
    return len(txt) == 0


# create operation list and use labmda functions to build the output
operation_list = {
    '1' : ('Palindrome: Check if the input is Palindrome', lambda txt : "The input is Palindrome.\n" if palindrome(txt) else "The input is NOT Palindrome.\n"),
    '2' : ('Lower: Check if all characters in the input are lowercase', lambda txt : "The input is lowercase.\n" if lower(txt) else "The input is NOT lowercase.\n"),
    '3' : ('Digit: Check if all characters in the input are digits', lambda txt: "The input is all digits .\n" if digit(txt) else "The input is NOT all digits.\n"),
    '4' : ('Long: Check if the input length is longer than 15', lambda txt: "The input is longer than 15 .\n" if long(txt) else "The input is NOT longer than 15 .\n"),
    '5' : ('Empty: Check if the input is empty.', lambda txt: "The input is empty .\n" if empty(txt) else "The input is NOT empty .\n"),
    '6' : ('Exit', None)
}

def printOperationsList():
    print("The Available Opearions are :")
    for index , (op , _) in operation_list.items():
        print(f"{index} - {op}")

def main():
    while True:
        printOperationsList()
        operationNumberInput = input('Please enter the number of the operation you choose:')
        if operationNumberInput == '6':
            print("Exit Successfully.")
            break
        elif operationNumberInput in operation_list:
            txtInput = input("Enter an input : ")
            print(operation_list[operationNumberInput][1](txtInput))            
        else:
            print('Wrong Input Try Again .. \n')
            continue

        
if __name__ == "__main__":
    main()