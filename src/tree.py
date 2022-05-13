# import local python files
from linkedlist_code import DoublyLinkedList

class TreeNode:
    """
    Creates a TreeNode object with the given data

    Requires one argument:
    data: the data to be added to the node
    
    Will create a doubly linked list to store all occurrences of the key (customer name)
    to prevent duplicate keys in the BST.
    """
    def __init__(self, data):
        self.key = data.get_customer_name()
        self.left = None
        self.right = None
        self.height = 1 # new node is initially added at leaf
        self.data = DoublyLinkedList() # to store data of the same customer name

        self.data.add_to_back(data)

class AVLTree:
    """
    This is an AVL tree that is a type of self-balancing binary search tree where
    the heights of the left and right subtrees of any node differ by less than or equal to 1.
    
    Guarantees that insertion, deletion, and search are O(log n) operations.
    
    More details: 
    - https://en.wikipedia.org/wiki/AVL_tree
    - https://www.programiz.com/dsa/avl-tree
    """
    def __init__(self):
        self.root = None

    def inorder_return_node(self, arr, reverse=False):
        """
        Traverse the tree in order and return the nodes by appending them to an array
        
        Requires two arguments:
        - arr (list): The array to append the nodes to
        - reverse (bool): Whether to return the nodes in ascending or descending order. 
        Defaults to False for ascending order.
        """
        return self._inorder_return_node(self.root, arr, reverse)

    def _inorder_return_node(self, root, arr, reverse=False):
        if (not root):
            return

        if (reverse):
            self._inorder_return_node(root.right, arr, reverse)
            arr.append(root)
            self._inorder_return_node(root.left, arr, reverse)
        else:
            self._inorder_return_node(root.left, arr, reverse)
            arr.append(root)
            self._inorder_return_node(root.right, arr, reverse)

    def tree_sort(self, reverse=False):
        """
        Returns a sorted array of the tree by customer name
        
        Best Time complexity: O(n)
        Worst Time complexity: O(n)
        Average Time complexity: O(n)
        
        Space complexity: O(n)
        Where n is the number of elements in the tree (not the number of nodes)
        
        Requires one argument:
        - reverse (bool): Whether to return the nodes in ascending or descending order. Defaults to False
        """
        if (not self.root):
            return []
        
        arr = []
        self.inorder_return_node(arr, reverse=reverse) # will return a list of linkedlist nodes
        
        # convert the list of linkedlist nodes into a list of RecordData objects
        newArr = []
        for node in arr:
            nodeData = node.data.convert_to_array()
            for data in nodeData:
                newArr.append(data)

        # return the sorted list of RecordData objects by customer name
        return newArr

    def search(self, target):
        """
        Do a search on the tree
        
        Best Time complexity: O(log n)
        Worst Time complexity: O(log n)
        Average Time complexity: O(log n)
    
        Requires one argument:
        - target (string): The target value to search for (customer name)
        """
        return self._search(self.root, target)

    def _search(self, root, target):
        # If the target is less than the current node, search the left subtree
        if (target < root.key):
            if (not root.left):
                return -1 # If the left child is empty, return -1
            else:
                return  self._search(root.left, target)

        # If the target is greater than the current node, search the right subtree
        elif (target > root.key):
            if (not root.right):
                return -1 # If the right child is empty, return -1
            else:
                return self._search(root.right, target)

        else:
            return root.data # If the target is equal to the current node, return a linkedlist of hotel record objects

    def insert(self, data):
        """
        Insert a node into the tree or append the data to the linkedlist in the node
        
        Best Time complexity: O(log n)
        Worst Time complexity: O(log n)
        Average Time complexity: O(log n)
        
        Requires one argument:
        - data (RecordData): The data of the node to be inserted into the tree
        """
        self.root = self._insert(self.root, data)

    def _insert(self, root, data):
        # If the tree is empty, return a new node as the root
        if (not root):
            return TreeNode(data)
        # If the data key is less than the current node, insert the node to the left subtree
        elif (data.get_customer_name() < root.key):
            root.left = self._insert(root.left, data)
        # If the data key is greater than the current node, insert the node to the right subtree
        elif (data.get_customer_name() > root.key):
            root.right = self._insert(root.right, data)
        # If the data key is equal to the current node, append the data to the linkedlist in the node
        else:
            root.data.add_to_back(data)
            return root

        # update the height of the current node
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # get the balance factor of the current node to check if the tree needs to be balanced
        balanceFactor = self.get_balance(root)
        
        # If the balance factor is greater than 1, the tree needs to be balanced
        if (balanceFactor > 1):
            # If the data key is less than the left child, rotate right
            if (data.get_customer_name() < root.left.key):
                # Left left case
                return self.right_rotate(root)
            # If the data key is greater than the right child, rotate left and then rotate right
            else:
                # Left right case
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)

        # If the balance factor is less than -1, the tree needs to be balanced
        if (balanceFactor < -1):
            # If the data key is greater than the right child, rotate left
            if (data.get_customer_name() > root.right.key):
                # Right right case
                return self.left_rotate(root)
            # If the data key is less than the left child, rotate right and then rotate left
            else:
                # Right left case
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

        return root

    def delete(self, data):
        """
        Delete a node from the tree and balance the tree if the node is deleted
        
        Best Time complexity: O(log n)
        Worst Time complexity: O(log n)
        Average Time complexity: O(log n)
        
        Requires one argument:
        - data (RecordData): The data of the node to be deleted from the linkedlist
        """
        self.root = self._delete(self.root, data)

    def _delete(self, root, data):
        # if the root is None, return None.
        # This will happen if the node to be deleted is not in the tree
        if (not root):
            return root
        # If the target is smaller than the current node, search the left subtree
        elif (data.get_customer_name() < root.key):
            root.left = self._delete(root.left, data)
        # If the target is greater than the current node, search the right subtree
        elif (data.get_customer_name() > root.key):
            root.right = self._delete(root.right, data)
        # target found!
        else:
            # if the node has more than one object inside the linkedlist, delete the target object from the linkedlist
            if (len(root.data) > 1):
                root.data.remove_node(data)
                return root

            # if the node has only one child or no child, replace the node with its child or None
            if (not root.left):
                temp = root.right
                root = None
                return temp
            elif (not root.right):
                temp = root.left
                root = None
                return temp

            # if the node has two childrens, find the inorder successor (smallest value in the right subtree)
            temp = self.get_min_value(root.right)

            # Copy the inorder successor's content to this node
            root.key = temp.key
            root.data = temp.data

            # Delete the inorder successor
            root.right = self._delete(root.right, temp.key)

        # if the tree had only one node, just return it as there is no need to balance the tree
        if (not root):
            return root

        # Now, to balance the tree...
        # update the height of the current node
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # get the balance factor of the current node to check if the tree needs to be balanced
        balanceFactor = self.get_balance(root)
        
        # If the balance factor is greater than 1, the tree needs to be balanced
        if (balanceFactor > 1):
            # If the balance factor of the left child is greater than 1, rotate right
            if (self.get_balance(root.left) >= 0):
                # Left left case
                return self.right_rotate(root)
            # If the balance factor of the left child is less than 0, rotate left and then rotate right
            else:
                # Left right case
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)

        # If the balance factor is less than -1, the tree needs to be balanced
        if (balanceFactor < -1):
            # If the balance factor of the right child is less than -1, rotate left
            if (self.get_balance(root.right) <= 0):
                # Right right case
                return self.left_rotate(root)
            # If the balance factor of the right child is greater than 0, rotate right and then rotate left
            else:
                # Right left case
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

        return root

    def left_rotate(self, x):
        """
        To perform left rotation on the subtree rooted with x
        """
        y = x.right
        subtree = y.left
        
        # Perform the rotation
        y.left = x
        x.right = subtree

        # update the heights
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def right_rotate(self, y):
        """
        To perform right rotation on the subtree rooted with y
        """
        x = y.left
        subtree = x.right
        
        # perform the rotation
        x.right = y
        y.left = subtree

        # update the heights
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x

    def get_height(self, root):
        """
        Get the height of the tree from the node
        """
        if (not root):
            return 0

        return root.height

    def get_balance(self, root):
        """
        Get the balance factor of the tree
        
        Formula:
        get_balance(x) = get_height(left child) - get_height(right child)
        
        Balance factor is used to determine if the tree is balanced or not.
        
        A tree is balanced if the balance factor is -1, 0, or 1
        
        Requires one argument:
        - root (TreeNode): The root node of the tree/subtree
        """
        if (not root):
            return 0

        return self.get_height(root.left) - self.get_height(root.right)

    def get_min_value(self, root):
        """
        Find the minimum value node in the tree
        """
        current = root

        # loop down to find the leftmost leaf as the smallest node is 
        # the left child of a root node of a subtree
        while (current.left):
            current = current.left

        return current

    def visualise_tree(self, root, indent="", rightChildNode=1):
        """
        Print the tree in a visual representation
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

            print(root.key, f"({len(root.data)} elements)")
            self.visualise_tree(root.left, indent, False)
            self.visualise_tree(root.right, indent, True)

    def __str__(self):
        """
        Return a string representation of the tree
        """
        self.visualise_tree(self.root)
        return ""

if __name__ == "__main__":
    from hotel_record import RecordData

    nodeList = []
    for i in range(0, 20, 4):
        for j in range(3):
            nodeList.append(RecordData(f"Product {j}", f"Customer {i}", 12, 1000))

    tree = AVLTree()
    for node in nodeList:
        tree.insert(node)
    
    print("tree:")
    print(tree)
    
    print("\nsearching")
    print(tree.search(nodeList[0].get_customer_name()))
    
    tree.delete(nodeList[0])
    print("\ntree after deleting one data from the node:")
    print(tree)
    
    for i in range(1, 3):
        tree.delete(nodeList[i])
    print("\ntree after deleting the node twice:")
    print(tree)
    
    print("\nTree sort by customer name:")
    arr = tree.tree_sort()
    [print(repr(x)) for x in arr]