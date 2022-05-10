# import local python files
from queue_code import Queue

class binaryTreeNode:
    def __init__(self, data):
        self.key = data.get_customer_name()
        self.data = [data]
        self.left = None
        self.right = None

    def insert(self, data):
        """
        Insert a new node into the tree
        
        Time complexity: O(log n)
        
        Requires one argument:
        - data (RecordData): The value to insert into the tree
        """
        # If the data is less than the current node, insert it into the left subtree
        if (data.get_customer_name() < self.key):
            if (not self.left):
                self.left = binaryTreeNode(data)
            else:
                self.left.insert(data)

        # If the data is greater than the current node, insert it into the right subtree
        elif (data.get_customer_name() > self.key):
            if (not self.right):
                self.right = binaryTreeNode(data)
            else:
                self.right.insert(data)

        # If the data is equal to the current node, aka duplicates, append it to the data list
        else:
            self.data.append(data)

    def search(self, target):
        """
        Do a binary search on the tree
        
        Time complexity: O(log n)
    
        Requires one argument:
        - target (int): The target value to search for
        """
        # If the target is less than the current node, search the left subtree
        if (target < self.key):
            if self.left is None:
                return -1 # Target not found
            else:
                return self.left.search(target)

        # If the target is greater than the current node, search the right subtree
        elif (target > self.key):
            if (not self.right):
                return -1 # If the right subtree is empty, return False
            else:
                return self.right.search(target)

        else:
            return self.data # If the target is equal to the current node, return a list of hotel record objects

    """ ------ Utility functions to print out the tree for debugging purposes below ------ """

    def inorder(self, printData):
        """
        Print the tree in inorder tree traversal (Left, Visit, Right)
        
        Time complexity: O(n) where n is the number of nodes in the tree
        
        Requires one argument:
        - printData (bool): Whether to print the data or the key (customer name)
        """
        if (self.left):
            self.left.inorder(printData)
        
        if (printData):
            print(self.data)
        else:
            print(self.key)

        if (self.right):
            self.right.inorder(printData)

    def preorder(self, printData):
        """
        Print the tree in preorder tree traversal (Visit, Left, Right)
        
        Time complexity: O(n) where n is the number of nodes in the tree
        
        Requires one argument:
        - printData (bool): Whether to print the data or the key (customer name)
        """
        if (printData):
            print(self.data)
        else:
            print(self.key)

        if (self.left):
            self.left.preorder(printData)
        if (self.right):
            self.right.preorder(printData)

    def postorder(self, printData):
        """
        Print the tree in postorder tree traversal (Left, Right, Visit)
        
        Time complexity: O(n) where n is the number of nodes in the tree
        
        Requires one argument:
        - printData (bool): Whether to print the data or the key (customer name)
        """
        if (self.left):
            self.left.postorder(printData)
        if (self.right):
            self.right.postorder(printData)

        if (printData):
            print(self.data)
        else:
            print(self.key)

    def levelorder(self, printData):
        """
        Print the tree in levelorder tree traversal using a queue data structure
        
        Time complexity: O(n) where n is the number of nodes in the tree        
        
        Requires one argument:
        - printData (bool): Whether to print the data or the key (customer name)
        """
        q = Queue()
        q.enqueue(self)
        while (not q.is_empty()):
            node = q.dequeue()
            if (printData):
                print(node.data)
            else:
                print(node.key)

            if (node.left):
                q.enqueue(node.left)
            if (node.right):
                q.enqueue(node.right)

def print_tree(root, traversalType=False, printData=False):
    """
    Print the tree in a specified order

    Requires two arguments:
    - root (binaryTreeNode): The root node of the tree
    - traversalType (int): The order to print the tree in, defaults to 0
        - 0: inorder traversal (Depth-first)
        - 1: preorder traversal (Depth-first)
        - 2: postorder traversal (Depth-first)
        - 3: levelorder traversal (Breadth-first)
    - printData (bool): Whether to print the data or the key (customer name)
    """
    if (not root):
        print("Tree is empty")
    else:
        if (traversalType == 0):
            root.inorder(printData)
        elif (traversalType == 1):
            root.preorder(printData)
        elif (traversalType == 2):
            root.postorder(printData)
        elif (traversalType == 3):
            root.levelorder(printData)
        else:
            raise Exception("Invalid traversal type passed into print_tree() function")

""" ---------------- End of utility functions ---------------- """

def insert(root, data):
    """
    Insert a new node into the tree

    Requires two arguments:
    - root (binaryTreeNode): The root node of the tree
    - data (RecordData): The object to insert into the tree
    """
    if (not root):
        root = binaryTreeNode(data)
    else:
        root.insert(data)
    return root

def search(root, target):
    """
    Do a binary search on the tree

    Requires two arguments:
    - root (binaryTreeNode): The root node of the tree
    - target (string): The target value to search for (customer name)
    """
    if (not root):
        return -1
    else:
        return root.search(target.title())

def minValueNode(root):
    """
    Find the minimum value node in the tree

    Time complexity: O(log n) when the tree is sorted and balanced
    Worst case: O(n) when the tree is left-skewed

    Requires one argument:
    - root (binaryTreeNode): The root node of the tree
    """
    # loop down to find the leftmost leaf as the smallest node is the left child of a root node
    current = root
    while (current.left):
        current = current.left
    return current

def deleteNode(root, target, deleteAll=False):
    """
    Delete a node from the tree and returns the root of modified tree

    Requires three arguments:
    - root (binaryTreeNode): The root node of the tree
    - target (RecordData): The target object to delete
    - deleteAll (bool): Whether or not to delete all instances of the target, 
    i.e. delete the node that contains the object, defaults to False
    """
    if (not root):
        return root
    
    # If the target is smaller than the current node, search the left subtree
    elif (target.get_customer_name() < root.key):
        root.left = deleteNode(root.left, target)
    
    # If the target is greater than the current node, search the right subtree
    elif (target.get_customer_name() > root.key):
        root.right = deleteNode(root.right, target)
    
    # target found!
    else:
        # if the user chose to delete one ocurrences of the target and it has more than one object inside the list, delete the first one
        if (not deleteAll and len(root.data) > 1):
            for i in range(len(root.data)):
                if (root.data[i] == target):
                    root.data.pop(i)
                    break
            return root

        # otherwise, delete the node that has only one or no child
        if (not root.left):
            return root.right
        elif (not root.right):
            return root.left

        # if the node has two childrens, find the index of the minimum value node in the right subtree
        temp = minValueNode(root.right)
        
        # copy the smallest value node's content to the current node
        root.key = temp.key
        root.data = temp.data
        
        # delete the smallest value node
        root.right = deleteNode(root.right, temp.key)

    return root

if __name__ == "__main__":
    from data import RecordData
    
    nodeToBeDeleted = RecordData("Package 1", "Customer 1", 12, 120)
    root = insert(None, nodeToBeDeleted)
    root = insert(root, RecordData("Package 1", "Customer 2", 12, 120))
    root = insert(root, RecordData("Package 1", "Customer 3", 12, 120))    
    root = insert(root, RecordData("Package 1", "Customer 4", 12, 120))
    root = insert(root, RecordData("Package 1", "Customer 1", 12, 120))
    root = insert(root, RecordData("Package 1", "Customer 1", 12, 120))

    print("tree:")
    print_tree(root, traversalType=3)
    
    print("\nsearching")
    print(search(root, nodeToBeDeleted))

    delete = deleteNode(root, "Customer 1")
    print("\ntree:")
    print_tree(root, traversalType=0, printData=0)
    
    root = deleteNode(root, nodeToBeDeleted, deleteAll=True)
    print("\ntree:")
    print_tree(root, traversalType=3, printData=0)
    
    root = insert(root, RecordData("Package 1", "Customer 1", 12, 120))
    print("\ntree:")
    print_tree(root, traversalType=3, printData=0)