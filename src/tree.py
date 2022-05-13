class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

# create a AVL tree
class AVLTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, root, data):
        if (not root):
            return TreeNode(data)
        
        elif data < root.key:
            root.left = self.insert_node(root.left, data)
        else:
            root.right = self.insert_node(root.right, data)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
    
        # update the balance factor and balance the tree
        balanceFactor = self.get_balance(root)
        if (balanceFactor > 1):
            if (data < root.left.key):
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)
        
        elif (balanceFactor < -1):
            if (data > root.right.key):
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)
        
        return root
    
    def delete(self, data):
        self.root = self._delete(self.root, data)
        
    def _delete(self, root, data):
        if (not root):
            return root

        elif (data < root.key):
            root.left = self._delete(root.left, data)
        elif (data > root.key):
            root.right = self._delete(root.right, data)
        else:
            if (not root.left):
                temp = root.right
                root = None
                return temp
            elif (not root.right):
                temp = root.left
                root = None
                return temp
        
            temp = self.get_min_value(root.right)
            root.key = temp.key
            root.right = self._delete(root.right, temp.key)
            
        if (not root):
            return root
        
        # balance the tree
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        
        balanceFactor = self.get_balance(root)
        if (balanceFactor > 1):
            if (self.get_balance(root.left) >= 0):
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)

        elif (balanceFactor < -1):
            if (self.get_balance(root.right) <= 0):
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)
        
        return root
    
    def left_rotate(self, root):
        y = root.right
        T2 = y.left
        y.left = root
        root.right = T2
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
    
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        
        return y
    
    def right_rotate(self, root):
        y = root.left
        T3 = y.right
        y.right = root
        root.left = T3
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        
        return y