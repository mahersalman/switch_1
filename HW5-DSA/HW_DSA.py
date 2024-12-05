

#Task 1 : Recent Call Logs

def RecentCallLog(calls, k):
    return calls[-k:]


# print(RecentCallLog([1001,1002,1003,1004],3))
# print(RecentCallLog([1,2],3))
# print(RecentCallLog([1,2,3,4,5],2))
# print(RecentCallLog([],5))

#Task 2 :  Inventory Shelf Arrangement

def reverse_Order(books_id):
    stack = []
    while books_id:
        stack.append(books_id.pop())
    return stack

# print(reverse_Order([101,102,103,104]))
# print(reverse_Order([1,2,3]))
# print(reverse_Order([]))
# print(reverse_Order([42]))

#Task 3 : Undo Feature in Text Editor

def undo_feature(actions, steps):   
    while steps:
        if actions : 
            actions.pop()
            steps-=1
        else: break
        
    return actions

# print(undo_feature(['type A', 'type B', 'delete'],1))
# print(undo_feature(['A','B'],1))
# print(undo_feature(['x'],2))
# print(undo_feature([],1))

#Task 4 : Validate Parentheses in a Code Snippet

def validate_parentheses(parentheses):
    legal = {
        ']': '[',
        '}': '{',
        ')': '('
    }
    stack = []

    for i in parentheses:
        if i in legal.values():
            stack.append(i)
        else:
            if not stack or stack.pop() != legal[i]:
                return False
    return False if stack else True

# print(validate_parentheses('([{}])'))
# print(validate_parentheses('([])'))
# print(validate_parentheses('([)]'))
# print(validate_parentheses(''))

#Task 9: Daily Temperature Analysis

def warmer_days_brute_force(temperatures): # O(n^2) 
    result = []
    for i in range(len(temperatures)):
        next_warmer_day = 0
        for j in range(i+1, len(temperatures)):
            if temperatures[j] > temperatures[i]:
                next_warmer_day = j-i
                break
        result.append(next_warmer_day)
    return result

def warmer_days_stack(temperatures): #O(n) time
        N = len(temperatures)
        result = [0]*N
        stack = []

        for i in range(N-1,-1,-1):
            while stack:
                if stack[-1][0] > temperatures[i]:
                    result[i] = stack[-1][1] - i
                    break
                else:
                    stack.pop()
            stack.append([temperatures[i],i])
        return result


#print(warmer_days_stack([73, 74, 75, 71, 69, 72, 76, 73]))

# print(warmer_days_brute_force([73, 74, 75, 71, 69, 72, 76, 73]))
# print(warmer_days_brute_force([30, 40, 50, 60]))
# print(warmer_days_brute_force([60, 50, 40]))
# print(warmer_days_brute_force([30]))
# print(warmer_days_brute_force([]))

#Task 5 : Ticket Counter Simulation

def ticket_simulation(customers):
    tickets = []
    while customers:
        tickets.append(customers.pop(0))
    return tickets

# print(ticket_simulation(["Alice", "Bob", "Charlie"]))
# print(ticket_simulation(["John",'Doe']))
# print(ticket_simulation([]))
# print(ticket_simulation(["OnlyOne"]))


#Tree Node class used in next tasks
class TreeNode:
    def __init__(self,value,children = None):
        self.value = value
        self.children = children if children else []

    def add_child(self, value,children = None):
        self.children.append(TreeNode(value,children))


#Task 6: Family Tree Search

def search_name(value, root : TreeNode):
    if root is None:
        return False
    return root.value == value or any(search_name(value, child) for child in root.children)

# root = TreeNode("A")
# root.add_child("B")
# root.add_child("C", [TreeNode("D"), TreeNode("E")])
# print(search_name("D", root)) 
# print(search_name("F", root))

# Task 7: Directory Size Calculation

def calculate_sizez_in_directory(root : TreeNode):
    if root is None:
        return 0
    return root.value + sum(calculate_sizez_in_directory(child) for child in root.children)

# root = TreeNode(10)
# root.children = [
#     TreeNode(5),
#     TreeNode(15,[TreeNode(10) ,TreeNode(5)])
# ]
# print(calculate_sizez_in_directory(root))  



# Task 13: Check Tree Symmetry

class Tree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def subtree_isSymmetric(left : Tree , right: Tree):
    if left == None and right == None:
        return True
    if left is None or right is None or left.val != right.val:
        return False
    return subtree_isSymmetric(left.left,right.right) and subtree_isSymmetric(left.right,right.left)

    
def isSymmetric(root: Tree):
    if root is None:
        return True
    return subtree_isSymmetric(root.left,root.right)

# tree1 = Tree(1,Tree(val=2,left = Tree(3)),Tree(val=2, right = Tree(3)))
# tree2 = Tree(val = 1 , left =Tree(2))

# print(isSymmetric(tree1))
# print(isSymmetric(tree2))