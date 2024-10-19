class Node:
    def __init__(self, data):
        self.data = data  # Store data
        self.next = None  # Store reference (next node)

class SinglyLinkedList:
    def __init__(self):
        self.head = None  # Initialize head as None

    def isEmpty(self):
        return self.head==None

    def search(self,value):  # For Searching Node for the Given Value
        if self.isEmpty():
            return None
        else:
            current_node=self.head   # Creating Temporary Node for Traversing
            while current_node:
                if current_node.data == value:  #Checking Data of current_node
                    return current_node
                current_node=current_node.next    #For Traversing in whole list
            return None

    def insert_at_beginning(self, data):
        new_node = Node(data)     # Create a new node
        new_node.next = self.head     # Link new node to the current head
        self.head = new_node      # Update head to point to the new node

    def insert_at_end(self, data):
        new_node = Node(data)     # Create a new node
        if self.head == None:
            self.head = new_node    #Updating head to point new node
        else:
            last_node = self.head      #Creating Temporary Node for Traversing
            while last_node.next:
                last_node = last_node.next     #Traversing till Last Node
            last_node.next = new_node     #Assigning new node to last_node.next

    def insert_after(self,value,data):
        new_node = Node(data)         #Creating a New Node
        given_node = self.search(value)    #Searching the Node for given Value
        if given_node == None:
            print("The Given Key is not available in the List! ")
        else:
            new_node.next = given_node.next
            given_node.next = new_node

    def delete_first(self):
        if self.head==None:
            print("Linked List is Empty")
        else:
            temp = self.head    #Creating Temporary Node and assigning head
            self.head=self.head.next   #Traversing the Head 1 time for deletion
            temp.next = None    #Assigning None to deleted Node

    def delete_last(self):
        if self.head==None:
            print("Linked List is Empty")
        elif self.head.next==None:  #Checking if there is only one node in List
            self.head=None   #If there is only one node assigning None to head
        else:
            current_node = self.head  #Creating Temporary Node for Traversing
            while current_node.next.next:
                current_node = current_node.next #Travering Temporary Node
            current_node.next = None

    def delete_specific(self, key):
        if(self.head.data==key):
            self.delete_first()
        else:
            current_node = self.head #Creating Temporary Node for Traversing
            prev=current_node  #Creating 1 more Temporary Node for previous Node
            while current_node:
                if current_node.data==key:   #Checking Data of current Node
                    prev.next=current_node.next  #Deleting Current Node
                    current_node.next=None #Assigning None to next deleted Node
                    break #If we found the node and it is deleted, no need to
                          #do more Traversing

                prev=current_node         # Assigning current_node to prev
                current_node=current_node.next #For Traversing

    def traverse_list(self): # To display the current Linked Lsit on the Screen
        current_node = self.head  #Creating Temporary Node for Traversing

        while current_node:
            print(current_node.data, end=" -> ") #printing data of current Node
            current_node = current_node.next  #For Traversing
        print("None")   # printing None at the End of the Linked List
