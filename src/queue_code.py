class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        """
        Returns True if the queue is empty, False otherwise.
        """
        return self.front == None

    def enqueue(self, item):
        """
        Adds an item to the rear of the queue.

        Time Complexity: O(1)
        """
        temp = Node(item)
        
        # If the queue is empty, set the front and rear to the new node
        if (not self.rear):
            self.front = self.rear = temp
            return
        
        self.rear.next = temp
        self.rear = temp

    def dequeue(self):
        """
        Removes and returns the item at the front of the queue.
        
        Time Complexity: O(1)
        """
        if (self.is_empty()):
            return
        
        temp = self.front
        self.front = temp.next
        
        # Check if the queue is empty after dequeueing, if so, set rear pointer to None as well
        if (not self.front):
            self.rear = None
            
        return temp.data