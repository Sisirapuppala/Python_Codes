class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

### write LinkedList class below this line ##


class LinkedList():
    def __init__(self):
        self.head = None
    def insert(self, value):
        n = Node(value)
        if self.head == None:
            self.head = n
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = n
    def remove(self,value):
        prev = self.head
        curr = self.head.next
        if prev.data == value:
            self.head = self.head.next
            return
        while curr!= None:
            if(curr.data == value):
                break
            prev = prev.next
            curr = curr.next

        prev.next = curr.next
        curr = None
    
    def Search(self,value):
        curr = self.head
        while curr != None:
            if curr.data == value:
                return ("true")
            curr = curr.next
        return ("false")

    def insertIndex(self, index, value):
        n = Node(value)
        if(index == 0):
            n.next = self.head
            self.head = n
            return
        curr= self.head
        curr_index = 0
        while(curr_index < index-1):
            curr = curr.next
            curr_index = curr_index+1
        n.next = curr.next
        curr.next = n
    def display(self):
        curr = self.head
        while(curr!=None):
            print(curr.data, end = ' ')
            curr = curr.next







### write LinkedList class above this line ##

if __name__ == "__main__": 
    test_cases=int(input()) # number of test cases
    myList=LinkedList()

    while(test_cases>0):
        instruction=int(input()) # current instruction
        ####
        # 1 means insertion
        # 2 means remove value
        # 3 means search value
        # 4 means insert at particular index
        # 5 means display entire list
        ####

        if(instruction==1): 
            val=int(input())
            print(f'Insert: {val}')
            myList.insert(val)
        elif (instruction==2):
            val=int(input())
            print(f'Delete: {val}')
            myList.remove(val)
        elif (instruction==3):
            val=int(input())
            print(f'Search for {val}. Found: {myList.Search(val)}')
        elif(instruction==4):
            index=int(input())
            val=int(input())
            print(f'Insert {val} at index {index}')
            myList.insertIndex(index,val)
        elif(instruction==5):
            print('Display:')
            myList.display()
            print()
        
        test_cases=test_cases-1

        
