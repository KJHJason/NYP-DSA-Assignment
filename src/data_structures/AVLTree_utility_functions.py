# import local python files
if (__package__ is None or __package__ == ""):
    from DoublyLinkedList import DoublyLinkedList
else:
    from .DoublyLinkedList import DoublyLinkedList

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

def get_height(node):
    """
    Get the height of the tree from the node
    
    Requires one argument:
    - node (TreeNode): the node to get the height from
    """
    if (node is None):
        return 0

    return node.height

def get_balance(root):
    """
    Get the balance factor of the tree
    
    Formula:
    get_balance(x) = get_height(left child) - get_height(right child)
    
    Balance factor is used to determine if the tree is balanced or not.
    
    A tree is balanced if the balance factor is -1, 0, or 1
    
    Requires one argument:
    - root (TreeNode): The root node of the tree/subtree
    """
    if (root is None):
        return 0

    return get_height(root.left) - get_height(root.right)

def get_min_value(root):
    """
    Find the minimum value node in the tree
    
    Requires one argument:
    - root (TreeNode): The root node of the tree/subtree
    """
    current = root

    # loop down to find the leftmost leaf as the smallest node is 
    # the left child of a root node of a subtree
    while (current.left is not None):
        current = current.left

    return current

def left_rotate(x):
    """
    To perform left rotation on the subtree rooted with x
    
    Requires one argument:
    - x (TreeNode): The root node of the subtree
    """
    y = x.right
    childSubtree = y.left
    
    # Perform the rotation
    y.left = x
    x.right = childSubtree

    # update the heights
    x.height = 1 + max(get_height(x.left), get_height(x.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y

def right_rotate(y):
    """
    To perform right rotation on the subtree rooted with y
    
    Requires one argument:
    - y (TreeNode): The root node of the subtree
    """
    x = y.left
    childSubtree = x.right
    
    # perform the rotation
    x.right = y
    y.left = childSubtree

    # update the heights
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))

    return x

def search_node(root, target):
    """
    Do a search on the tree
    
    Best Time complexity: O(log n)
    Worst Time complexity: O(log n)
    Average Time complexity: O(log n)

    Requires two arguments:
    - root (TreeNode): The root node of the tree/subtree
    - target (string): The target value to search for (customer name)
    """
    # If the target is less than the current node, search the left subtree
    if (target < root.key):
        if (root.left is None):
            return -1 # If the left child is empty, return -1
        else:
            return search_node(root.left, target)
    # If the target is greater than the current node, search the right subtree
    elif (target > root.key):
        if (root.right is None):
            return -1 # If the right child is empty, return -1
        else:
            return search_node(root.right, target)
    else:
        # If the target is equal to the current node, return 
        # a linkedlist of hotel record objects
        return root.data 

def insert_node(root, data):
    """
    Insert a node into the tree or append the data to the linkedlist in the node
    
    Best Time complexity: O(log n)
    Worst Time complexity: O(log n)
    Average Time complexity: O(log n)
    
    Requires two arguments:
    - root (TreeNode): The root node of the tree/subtree
    - data (RecordData): The data of the node to be inserted into the tree
    """
    # If the tree is empty, return a new node as the root
    if (root is None):
        return TreeNode(data)
    # If the data key is less than the current node, insert the node to the left subtree
    elif (data.get_customer_name() < root.key):
        root.left = insert_node(root.left, data)
    # If the data key is greater than the current node, insert the node to the right subtree
    elif (data.get_customer_name() > root.key):
        root.right = insert_node(root.right, data)
    # If the data key is equal to the current node, append the data to the linkedlist in the node
    else:
        root.data.add_to_back(data)
        return root

    # update the height of the current node
    root.height = 1 + max(get_height(root.left), get_height(root.right))

    # get the balance factor of the current node to check if the tree needs to be balanced
    balanceFactor = get_balance(root)
    
    # If the balance factor is greater than 1, the tree needs to be balanced
    if (balanceFactor > 1):
        # If the data key is less than the left child, rotate right
        if (data.get_customer_name() < root.left.key):
            r"""
            e.g. of left left case
                        5 (bf:  2-0 = 2)
                       /
                      2 (bf: 1-0 = 1)
                     /
            (bf: 0) 1 
            Afterwards, in this example, we will have to balance the tree with 
            a right rotation on the subtree with root 5.

            y = 5
            initialise x and childSubtree
            x = y.left (5.left = 2)
            childSubtree = x.right (2.right = None)
            
            then we perform the rotation
            2.right = y (5)
            5.left = childSubtree (None)
            
            return x node (2)

            After doing a right rotation (clockwise rotation), the balanced tree will look like this:
                      2 (bf: 1-1 = 0)
                     / \
            (bf: 0) 1   5 (bf: 0)
            """
            return right_rotate(root)
        # If the data key is greater than the right child, rotate left and then rotate right
        else:
            r"""
            e.g. of left right case
            
              5 (bf:  2-0 = 2)
             / 
            2 (bf: 0-2 = -2)
             \
              3 (bf: 0-1 = -1)

            Afterwards, in this example, we will have to balance the tree with a left rotation 
            and then a right rotation (left right case).
            
            First left rotation (anti-clockwise rotation) on the left child of the subtree rooted at node 2:
                5 (bf:  2-0 = 2)
               / 
              3 (bf: 1-0 = 1) 
             /
            2 (bf: 0

            Then right rotation (clockwise rotation) on the subtree rooted at node 5:
                      3 (bf:  1-1 = 0)
                     / \
            (bf: 0) 2   5 (bf: 0)
            """
            root.left = left_rotate(root.left)
            return right_rotate(root)

    # If the balance factor is less than -1, the tree needs to be balanced
    if (balanceFactor < -1):
        # If the data key is greater than the right child, rotate left
        if (data.get_customer_name() > root.right.key):
            r"""
            e.g. of right right case
            5 (bf:  0-2 = -2)
             \
              6 (bf: 0-1 = -1)
               \
                8 (bf: 0)
            Afterwards, in this example, we will have to balance the tree with a left rotation
            on the subtree with root 5.

            x = 5
            initialise y and childSubtree
            y = x.right (5.right = 6)
            childSubtree = y.left (6.left = None)

            then we perform the rotation
            6.left = x (5)
            5.right = childSubtree (None)

            return y node (6)

            After doing a left rotation (anti-clockwise rotation), the balanced tree will look like this:
                      6 (bf: 1-1 = 0)
                     / \
            (bf: 0) 5   8 (bf: 0)
            """
            return left_rotate(root)
        # If the data key is less than the left child, rotate right and then rotate left
        else:
            r"""
            e.g. of right left case
            
            1 (bf:  0-2 = -2)
             \ 
              3 (bf: 1-0 = 1)
             /
            2(bf: 0)

            Afterwards, in this example, we will have to balance the tree with a right rotation
            and then a left rotation (right left case).

            First right rotation (clockwise rotation) on the right child of the subtree rooted at node 3:
            1 (bf:  0-2 = -2)
             \
              2 (bf: -1-0 = -1)
               \
                3 (bf: 0)

            Then left rotation (anti-clockwise rotation) on the subtree rooted at node 1:
                      2 (bf:  1-1 = 0)
                     / \
            (bf: 0) 1   3 (bf: 0)
            """
            root.right = right_rotate(root.right)
            return left_rotate(root)

    return root

def delete_node(root, data):
    """
    Delete a node from the tree and balance the tree if the node is deleted
    
    Best Time complexity: O(log n)
    Worst Time complexity: O(log n)
    Average Time complexity: O(log n)
    
    Requires two argument:
    - root (TreeNode): The root node of the tree/subtree
    - data (RecordData): The data of the node to be deleted from the linkedlist
    """
    # if the root is None, return None.
    # This will happen if the node to be deleted is not in the tree
    if (root is None):
        return root
    # If the target is smaller than the current node, search the left subtree
    elif (data.get_customer_name() < root.key):
        root.left = delete_node(root.left, data)
    # If the target is greater than the current node, search the right subtree
    elif (data.get_customer_name() > root.key):
        root.right = delete_node(root.right, data)
    # target found!
    else:
        # if the node has more than one object inside the linkedlist, delete the target object from the linkedlist
        if (len(root.data) > 1):
            root.data.remove_node(data)
            return root

        # if the node has no children (leaf node), return None to delete the node
        if (root.left is None and root.right is None):
            return None

        # if the node has only one child, replace the node with its child
        # and delete the child's parent (the node to be deleted from the tree)
        if (root.left is None):
            temp = root.right
            del root
            return temp
        elif (root.right is None):
            temp = root.left
            del root
            return temp

        r"""
        if the node has two childrens, find the inorder successor 
        (smallest value in the right subtree/
        the node with the smallest key greater than the key of the input node)

        e.g. 
                        4 (bf: 2-1 = 1)
                       / \
        (bf: 1-1 = 0) 2   5 (bf: 0)
                     / \
            (bf: 0) 1   3 (bf: 0)

        If we want to delete the node with value 4, we will find 
        the inorder successor in the right subtree which will be the node with value 5.

                    5 (inorder successor, bf: 2-0 = 2)
                   /
                  2 (bf: 1-1 = 0)
                 / \
        (bf: 0) 1   3 (bf: 0)

        We will then replace the node that we wanted to delete with the inorder successor as shown above.
        """
        temp = get_min_value(root.right)

        # Copy the inorder successor's content to this node
        root.key = temp.key
        root.data = temp.data

        # Delete the inorder successor
        root.right = delete_node(root.right, temp.key)

    # if the tree had only one node, just return it as there is no need to balance the tree
    if (root is None):
        return root

    # Now, to balance the tree...
    # update the height of the current node
    root.height = 1 + max(get_height(root.left), get_height(root.right))

    # get the balance factor of the current node to check if the tree needs to be balanced
    balanceFactor = get_balance(root)
    
    # If the balance factor is greater than 1, the tree needs to be balanced
    if (balanceFactor > 1):
        # If the balance factor of the left child is greater than 1, rotate right
        if (get_balance(root.left) >= 0):
            # Left left case
            return right_rotate(root)
        # If the balance factor of the left child is less than 0, rotate left and then rotate right
        else:
            # Left right case
            root.left = left_rotate(root.left)
            return right_rotate(root)

    # If the balance factor is less than -1, the tree needs to be balanced
    if (balanceFactor < -1):
        # If the balance factor of the right child is less than -1, rotate left
        if (get_balance(root.right) <= 0):
            # Right right case
            return left_rotate(root)
        # If the balance factor of the right child is greater than 0, rotate right and then rotate left
        else:
            # Right left case
            root.right = right_rotate(root.right)
            return left_rotate(root)

    return root