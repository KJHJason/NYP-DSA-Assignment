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
        
        # set the rear's next to the new node
        self.rear.next = temp
        
        # change the rear pointer to the new node
        self.rear = temp

    def dequeue(self):
        """
        Removes and returns the item at the front of the queue.
        
        Time Complexity: O(1)
        """
        if (self.is_empty()):
            return
        
        # save the front node as temp
        temp = self.front
        
        # To dequeue the queue, update the front pointer to the next node of the original front node
        self.front = temp.next
        
        # Check if the queue is empty after dequeueing, if so, set rear pointer to None as well
        if (not self.front):
            self.rear = None
        
        # return the dequeued node
        return temp.data

    def __repr__(self):
        """
        Returns a string representation of the queue.
        """
        if (self.is_empty()):
            return "- []"

        # set the current node to the front
        current = self.front

        # loop through the queue and add the data of each node to the string
        arr = []
        while (current):
            arr.append(repr(current.data))
            current = current.next

        return f"- [{', '.join(arr)}]"

# test code for queue
if __name__ == "__main__":
    q = Queue()

    print("Enqueueing 10 elements...")
    for i in range(10):
        q.enqueue(i)

    print(q)

    print("\nDequeuing 3 elements...")
    for i in range(3):
        print("Dequeued:", q.dequeue())

    print()
    print(q)