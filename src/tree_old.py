# import local python files
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
        
        Best Time complexity: O(log n) when the tree is balanced
        Worst Time complexity: O(n) when the tree is unbalanced
        Average Time complexity: O(log n)
        
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
        Do a search on the tree
        
        Best Time complexity: O(log n) when the tree is balanced
        Worst Time complexity: O(n) when the tree is unbalanced
        Average Time complexity: O(log n)
    
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

    def inorder_return_node(self, arr, reverse=False):
        """
        Return each node in the tree in inorder tree traversal for tree sort
        (Left, Visit, Right) --> Ascending
        (Right, Visit, Left) --> Descending
        
        Time complexity: O(n) where n is the number of nodes in the tree
        
        Requires two argument:
        - arr (list): The list to append the nodes to
        - reverse (bool): Whether to return the nodes in ascending or descending order. Defaults to False
        """
        if (not reverse):
            if (self.left):
                self.left.inorder_return_node(arr, reverse)
            
            arr.append(self)
            
            if (self.right):
                self.right.inorder_return_node(arr, reverse)
        else:
            if (self.right):
                self.right.inorder_return_node(arr, reverse)
            
            arr.append(self)
            
            if (self.left):
                self.left.inorder_return_node(arr, reverse)

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

    def tree_sort(self, reverse=False):
        """
        Returns a sorted array of the tree by customer name
        
        Best Time complexity: O(n)
        Worst Time complexity: O(n)
        Average Time complexity: O(n)
        
        Space complexity: O(n)
        
        Requires one argument:
        - reverse (bool): Whether to return the nodes in ascending or descending order. Defaults to False
        """
        if (not self.root):
            return []
        
        arr = []
        self.root.inorder_return_node(arr, reverse) # will return a list of linkedlist nodes
        
        # convert the list of linkedlist nodes into a list of RecordData objects
        newArr = []
        for node in arr:
            nodeData = node.data.convert_to_array()
            for data in nodeData:
                newArr.append(data)

        # return the sorted list of RecordData objects by customer name
        return newArr

def min_value_node(root):
    """
    Find the minimum value node in the tree

    Best Time complexity: O(log n) when the tree is balanced
    Worst Time complexity: O(n) when the tree is left-skewed
    Average Time complexity: O(log n)

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
    
    Best Time complexity: O(log n) when the tree is balanced
    Worst Time complexity: O(n) when the tree is unbalanced
    Average Time complexity: O(log n)

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
            root.data.remove_node(target)
            return root

        # Case 1: if the node has no children
        if (not root.left and not root.right):
            root = None

        # Case 2: if the node has only one child
        elif (not root.left):
            # make the right child the new root of the subtree by moving the root to the right child
            temp = root.right
            root = None
            root = temp
        elif (not root.right):
            # make the left child the new root of the subtree by moving the root to the left child
            temp = root.left 
            root = None
            root = temp

        # Case 3: the node has two childrens
        else:
            # find the minimum value node in the right subtree
            temp = min_value_node(root.right)
            
            # copy the successor's value to the current node
            root.key = temp.key
            root.data = temp.data
            
            # delete the successor node from the right subtree
            root.right = delete_node(root.right, temp.key)

    return root

def visualise_tree(root, indent="", rightChildNode=1):
    """
    Print the tree to visually check if the tree is balanced 
    in a preorder traversal (Visit, Left, Right)
    
    Requires three arguments:
    root: the root of the tree
    indent: the indentation of the current node
    rightChildNode: the node that is the right child of the current node
    """
    if (root):
        print(indent, end="")
        if (rightChildNode):
            print("R-----", end="")
            indent += "     "
        else:
            print("L-----", end="")
            indent += "|    "

        print(root.key)
        visualise_tree(root.left, indent, False)
        visualise_tree(root.right, indent, True)

# Test codes for the BST
if __name__ == "__main__":
    from hotel_record import RecordData

    nodeList = []
    for i in range(0, 20, 4):
        for j in range(3):
            nodeList.append(RecordData(f"Product {j}", f"Customer {i}", 12, 1000))

    root = BinarySearchTree()
    for node in nodeList:
        root.insert(node)

    print("tree:")
    visualise_tree(root.root)
    
    print("\nsearching")
    print(root.search(nodeList[0].get_customer_name()))
    
    root.delete(nodeList[0])
    print("\ntree after deleting one data from the node:")
    visualise_tree(root.root)
    
    root.delete(nodeList[1])
    root.delete(nodeList[2])
    print("\ntree after deleting the node twice:")
    visualise_tree(root.root)
    
    root.insert(RecordData("Package 1", "Customer 1", 12, 120))
    print("\ntree:")
    root.print_tree(traversalType=3, printData=0)
    
    print("\nTree sort:")
    arr = root.tree_sort()
    [print(repr(x)) for x in arr]