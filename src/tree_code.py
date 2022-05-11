# import local python files
from queue_code import Queue
from linkedlist_code import DoublyLinkedList

class binaryTreeNode:
    def __init__(self, data):
        self.key = data.get_customer_name()
        self.data = DoublyLinkedList()
        self.left = None
        self.right = None

        self.data.add_to_back(data)

    def insert(self, data):
        """
        Insert a new node into the tree
        
        Time complexity: O(log n)
        
        Requires one argument:
        - data (RecordData): The value to insert into the tree
        """
        # If the data is less than the current node, insert it into the left subtree
        if (data.get_customer_name() < self.key):
            # checks if the current node has a left child
            if (not self.left):
                # if there is no left child, create a new node in the current node's left child
                self.left = binaryTreeNode(data)
            else:
                # if the current node has a left child, recurse down the left subtree
                self.left.insert(data)

        # If the data is greater than the current node, insert it into the right subtree
        elif (data.get_customer_name() > self.key):
            # checks if the current node has a right child
            if (not self.right):
                # if there is no right child, create a new node in the current node's right child
                self.right = binaryTreeNode(data)
            else:
                # if the current node has a right child, recurse down the right subtree
                self.right.insert(data)

        # If the data is equal to the current node, aka duplicates, append it to the data list
        else:
            self.data.add_to_back(data)

    def search(self, target):
        """
        Do a binary search on the tree
        
        Time complexity: O(log n)
    
        Requires one argument:
        - target (string): The target value to search for (customer name)
        """
        # If the target is less than the current node, search the left subtree
        if (target < self.key):
            if (not self.left):
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
            return self.data # If the target is equal to the current node, return a linkedlist of hotel record objects

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

""" ---------------- End of utility functions ---------------- """

class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def insert(self, data):
        """
        Insert a new node into the tree

        Requires two arguments:
        - data (RecordData): The object to insert into the tree
        """
        if (not self.root):
            self.root = binaryTreeNode(data)
        else:
            self.root.insert(data)

    def search(self, target):
        """
        Do a binary search on the tree

        Requires two arguments:
        - root (binaryTreeNode): The root node of the tree
        - target (string): The target value to search for (customer name)
        """
        if (not self.root):
            return -1
        else:
            return self.root.search(target.title())
    
    def delete(self, target):
        """
        Delete a node from the tree

        Requires two arguments:
        - target (RecordData): The target object to delete
        - deleteAll (bool): Whether or not to delete all instances of the target, 
                            i.e. Whether to delete the node that contains the object, defaults to False
        """
        self.root = delete_node(self.root, target)

    def print_tree(self, traversalType=False, printData=False):
        """
        Print the tree in a specified order

        Requires two arguments:
        - traversalType (int): The order to print the tree in, defaults to 0
            - 0: inorder traversal (Depth-first)
            - 1: preorder traversal (Depth-first)
            - 2: postorder traversal (Depth-first)
            - 3: levelorder traversal (Breadth-first)
        - printData (bool): Whether to print the data or the key (customer name)
        """
        if (not self.root):
            print("Tree is empty")
        else:
            if (traversalType == 0):
                self.root.inorder(printData)
            elif (traversalType == 1):
                self.root.preorder(printData)
            elif (traversalType == 2):
                self.root.postorder(printData)
            elif (traversalType == 3):
                self.root.levelorder(printData)
            else:
                raise Exception("Invalid traversal type passed into print_tree() function")

def min_value_node(root):
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

def delete_node(root, target):
    """
    Delete a node from the tree and returns the root of modified tree

    Requires three arguments:
    - root (binaryTreeNode): The root node of the tree
    - target (RecordData): The target object to delete
    """
    if (not root):
        return root
    
    # If the target is smaller than the current node, search the left subtree
    elif (target.get_customer_name() < root.key):
        root.left = delete_node(root.left, target)
    
    # If the target is greater than the current node, search the right subtree
    elif (target.get_customer_name() > root.key):
        root.right = delete_node(root.right, target)
    
    # target found!
    else:
        # if the node has more than one object inside the linkedlist, delete the target object from the linkedlist
        if (len(root.data) > 1):
            root.data.remove_a_node(target)
            return root

        # otherwise, delete the node that has only one or no child
        if (not root.left):
            return root.right
        elif (not root.right):
            return root.left

        # if the node has two childrens, find the index of the minimum value node in the right subtree
        temp = min_value_node(root.right)
        
        # copy the smallest value node's content to the current node
        root.key = temp.key
        root.data = temp.data
        
        # delete the smallest value node
        root.right = delete_node(root.right, temp.key)

    return root

# Test codes for the BST
if __name__ == "__main__":
    from data import RecordData
    
    nodeList = []
    for i in range(0, 3):
        for j in range(3):
            nodeList.append(RecordData(f"Product {j}", f"Customer {i}", 12, 1000))
    
    root = BinarySearchTree()
    for node in nodeList:
        root.insert(node)

    print("tree:")
    root.print_tree(traversalType=3)
    
    print("\nsearching")
    print(root.search(nodeList[0].get_customer_name()))
    
    print("\nbefore deleting...")
    root.print_tree(traversalType=0, printData=1)
    
    root.delete(nodeList[1])
    print("\ntree after deleting one data from the node:")
    root.print_tree(traversalType=0, printData=1)
    
    root.delete(nodeList[0])
    print("\ntree after deleting the node:")
    root.print_tree(traversalType=0, printData=1)
    
    root.insert(RecordData("Package 1", "Customer 1", 12, 120))
    print("\ntree:")
    root.print_tree(traversalType=3, printData=0)