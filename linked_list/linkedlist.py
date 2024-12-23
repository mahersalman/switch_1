

class Node:
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self,head = None):
        self.head = head

    # /*********************************/
    #         Basic Methods          /
    # /*********************************/
        
    def buildLinkedList(self,arr):               
        if not arr :
            return
        self.head = Node(arr[0])
        curr = self.head

        for i in range(1,len(arr)) :
            curr.next = Node(arr[i])
            curr = curr.next
        

    def print_list(self):
        curr = self.head
        while curr :
            print(curr.data, end = " -> ")
            curr = curr.next
        print('None')

    def addToHead(self,val):
        if self.head == None:
            self.head = Node(val)
        
        else:
            temp = Node(val,self.head)
            self.head = temp
    
    def addToTail(self,val):
        if self.head == None:
            self.head = Node(val)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = Node(val)
    
    def deleteHead(self):
        if self.head is None:
            return None
        temp = self.head.data
        self.head = self.head.next
        return temp
    
    def deleteTail(self):
        if self.head is None:
            return None
        if self.head.next is None:
            temp = self.head.data
            self.head = None
            return temp
        
        curr = self.head
        while curr.next:
            curr = curr.next
        temp = curr.next.data
        curr.next = None
        return temp
    
    def find(self,val):
        curr = self.head
        while curr:
            if curr.data == val:
                return curr
            curr = curr.next
        return None
    
    # /*********************************/
    #         Advanced Methods          /
    # /*********************************/

    def hasCycle_Approach1(self):# O(n) time and space
        visited = set()
        curr = self.head
        while curr:
            if curr in visited:
                return True
            visited.add(curr)
            curr = curr.next
        return False
    
    def hasCycle_Floyd(self):# O(n) time - O(1) space
        slow , fast = self.head , self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast :
                return True
        return False
    
def main():
    arr = [3,5,15,66,-6]
    
    lst = LinkedList()

    lst.buildLinkedList(arr)
    lst.print_list()

main()