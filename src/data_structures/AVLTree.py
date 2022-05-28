# import local python files
if (__package__ is None or __package__ == ""):
    from AVLTree_utility_functions import search_node, insert_node, delete_node
else:
    from .AVLTree_utility_functions import search_node, insert_node, delete_node

class AVLTree:
    """
    This is an AVL tree that is a type of self-balancing binary search tree where
    the heights of the left and right subtrees of any node differ by less than or equal to 1.
    
    Guarantees that insertion, deletion, and search are O(log n) operations.
    
    More details: 
    - https://en.wikipedia.org/wiki/AVL_tree
    - https://www.programiz.com/dsa/avl-tree
    - https://www.javatpoint.com/avl-tree
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
        
        Note: It is O(n) in this case as in the HotelDatabase object, the AVLTree object is automatically
        updated every time the user adds, changes, or deletes a customer name.
        Hence, removing the need to insert the nodes into the tree when sorting using tree sort.
        
        Space complexity: O(m + n)
        Where m is the number of nodes in the tree and 
        n is the number of elements (inside all linkedlist) in the tree
        
        Requires one argument:
        - reverse (bool): Whether to return the nodes in ascending or descending order. Defaults to False
        """
        if (self.root is None):
            return []

        arr = []
        self.inorder_return_node(arr, reverse=reverse) # will return a list of linkedlist nodes

        # convert the list of linkedlist nodes into a list of RecordData objects
        sortedArr = []
        for node in arr:
            # get the data from the linkedlist and append it to sortedArr
            for data in node.data.convert_to_array():
                sortedArr.append(data)

        # return the sorted list of RecordData objects by customer name
        return sortedArr

    def move_node(self, data):
        """
        Used when the user has changed the customer name in one of the nodes in the tree.
        Hence, there will be a need to delete the old data in the linkedlist that may result 
        in deletion of the tree node if there is only one data in the linkedlist.
        Since, there is a new customer name, we will have to insert a node into the root with a new key.
        
        Requires one argument:
        - data (RecordData): The data of the node to be deleted from the linkedlist
        """
        self.delete(data)
        self.insert(data)

    def search(self, target):
        return search_node(self.root, target)

    def insert(self, data):
        self.root = insert_node(self.root, data)

    def delete(self, data):
        self.root = delete_node(self.root, data)

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
        self.visualise_tree(self.root)
        return ""

if (__name__ == "__main__"):
    from uuid import uuid4
    class TestData:
        def __init__(self, name):
            self.__customer_name = name
            self.id = uuid4().hex
        
        def get_customer_name(self):
            return self.__customer_name
        
        def __repr__(self):
            return f"{self.__customer_name} ({self.id})"

    nodeList = []
    for i in range(0, 20, 4):
        for j in range(3):
            nodeList.append(TestData(f"Customer {i}"))

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