class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_to_back(self, data):
        """
        Add a node to the end of the linked list

        Time Complexity: O(1)

        Requires one argument:
        data: the data to be added to the linked list
        """
        # case 1: if the linked list is empty
        if (not self.head):
            self.head = Node(data)
            self.tail = self.head
            self.size += 1
            return

        # case 2: if the linked list has more than one node
        self.tail.next = Node(data)
        self.tail.next.prev = self.tail
        self.tail = self.tail.next
        self.size += 1
        return

    def remove_back(self):
        """
        Remove a ndoe from the end of the linked list
        
        Similar to a queue's dequeue() method
        
        Returns the removed node.
        
        Time Complexity: O(1)
        """
        # case 1: if the linked list is empty
        if (not self.head):
            return

        # case 2: if the linked list has only one node
        if (self.head == self.tail):
            temp = self.head
            self.head = None
            self.tail = None
            self.size -= 1
            return temp.data
    
        # case 3: if the linked list has multiple nodes
        temp = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        self.size -= 1
        return temp.data

    def remove_node(self, data):
        """
        Remove a node from the linked list
        
        Best Time Complexity: O(1)
        Worst Time Complexity: O(n)
        Average Time Complexity: O(n)
        
        Advantages over a list:
        - O(1) when removing the node from the beginning or the end of the linkedlist
        - Better performance when removing a node in the linkedlist as it is not necessary to shift the nodes as compared to a list
        
        Requires one argument:
        data: the data to be removed from the linked list
        """
        # case 1: if the linked list is empty
        if (not self.head):
            return

        # case 2: if the node to be removed is the head
        if (self.head.data == data):
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1
            return

        # case 3: if the node to be removed is the tail
        if (self.tail.data == data):
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1
            return

        # case 4: if the linked list has multiple nodes
        current = self.head.next
        while (current):
            # check if the node to be removed is the current node
            if (current.data == data):
                current.prev.next = current.next # if so, set the previous node's next to the current node's next
                current.next.prev = current.prev # set the next node's previous to the current node's previous
                self.size -= 1
                return
            
            # move to the next node
            current = current.next

        return -1 # return -1 if the node is not in the linked list

    def is_empty(self):
        """
        Returns True if the linked list is empty, False otherwise
        """
        return self.size == 0

    def print_list(self):
        """
        Print the linked list object
        """
        current = self.head
        while (current):
            print(current.data)
            current = current.next
    
    def convert_to_array(self):
        """
        Convert the linked list to an array/list
        """
        listOfNodes = []
        current = self.head
        while (current):
            listOfNodes.append(current.data)
            current = current.next
        return listOfNodes

    def __len__(self):
        return self.size

    def __str__(self):
        if (not self.head):
            return "- []"
        
        arr = self.convert_to_array()
        arr = [repr(i) for i in arr]
        return f"- [{', '.join(arr)}]"

# test codes for doubly linked list
if __name__ == "__main__":
    ll = DoublyLinkedList()
    for i in range(10):
        ll.add_to_back(i)

    ll.remove_node(8)
    print(ll)

    ll.remove_node(0)
    print(ll)

    ll.remove_node(9)
    print(ll)

    ll.add_to_back(9)
    print(ll)
    
    print("Removed back element:", ll.remove_back())
    print(ll)