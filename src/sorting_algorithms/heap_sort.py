def heapify(arr, n, i, reverse=False): 
    """
    To heapify subtree rooted at index i. 
    
    Binary heap is a complete binary tree 
    (all levels are completely filled, except possibly the last level 
    and the last level has nodes that are filled from left to right)
    
    Binary heap properties:
    - in ascending order (max-heap): 
        - at any node, the value of the node is greater than or equal to the values of its children
        - the value of the root node is the largest value in the subtree
    - in descending order (min-heap): 
        - at any node, the value of the node is less than or equal to the values of its children
        - the value of the root node is the smallest value in the subtree
    
    Requires 4 arguments:
    - arr (list): The array of elements to heapify
    - n (int): the size of the array
    - i (int): the index of the root of the subtree
    - reverse (bool): whether to make it a max-heap or a min-heap (Default: False)
    """
    l = (2 * i) + 1
    r = (2 * i) + 2

    if (reverse):
        r"""
        e.g. of valid min heap:
          55
         /  \
        57  63
        
        e.g. of Invalid min heap:
        8         
         \
          9 
        Reason: It is not a complete binary tree
        
        e.g. of invalid min heap:
          3                           1
         / \   --> Correct version:  / \
        1   6                       3   6
        Reason: 1 is smaller than 3 which violates the min-heap property
        """
        smallest = i # Initialise smallest as root

        # if left child of root exists and is smaller than root 
        if (l < n and arr[l].get_package_name() < arr[smallest].get_package_name()): 
            smallest = l 

        # if right child of root exists and is smaller than smallest 
        if (r < n and arr[r].get_package_name() < arr[smallest].get_package_name()): 
            smallest = r
        
        # Change root if smallest is not root
        if (smallest != i): 
            arr[i], arr[smallest] = arr[smallest], arr[i] 
            
            # recursively heapify the affected sub-tree
            heapify(arr, n, smallest, reverse)
    else:
        r"""
        e.g. of valid max heap:
          3
         /  \
        57  55
        
        e.g. of invalid max heap:
            9                            9
           / \                          / \
          5   7  --> Correct version:  6   7
         /                            /
        6                            5
        Reason: 6 is smaller than 5 which violates the max heap property
        """
        largest = i # Initialise largest as root 

        # See if left child of root exists and is greater than root 
        if (l < n and arr[largest].get_package_name() < arr[l].get_package_name()): 
            largest = l 
    
        # See if right child of root exists and is greater than largest 
        if (r < n and arr[largest].get_package_name() < arr[r].get_package_name()): 
            largest = r 
    
        # Change root if largest is not root
        if (largest != i): 
            arr[i], arr[largest] = arr[largest],arr[i]
    
            # recursively heapify the affected sub-tree
            heapify(arr, n, largest, reverse) 

def heap_sort(arr, reverse=False):
    """
    Do a heap sort on the database by package name
    
    Requires 2 arguments:
    - arr (list): The array of elements to sort by package name
    - reverse (bool): True if the list is to be sorted in descending order (Default: False)
    
    Best time complexity: O(n log n)
    Worst time complexity: O(n log n)
    Average time complexity: O(n log n)
    """
    n = len(arr) 

    # Build a min or max heap depending on the reverse condition
    # if in ascending order, then build a max heap
    # if in descending order, then build a min heap
    # The range starts from n//2-1 as it is the index of the non-leaf node
    # then perform a reverse level order traversal from the last non-leaf node
    # and heapify each node
    for i in range((n // 2)-1, -1, -1): 
        heapify(arr, n, i, reverse=reverse) 

    # extract elements individually starting from the end of the heap
    for i in range(n-1, -1, -1): 
        # Move current root to end by swapping with last ith element
        # as the largest(max heap)/smallest(min heap) element in the heap is at the root of the heap,
        # Hence, move it to the last ith element and call heapify 
        # on the new root with the new reduced size
        arr[i], arr[0] = arr[0], arr[i]

        # call heapify on the reduced heap
        heapify(arr, i, 0, reverse=reverse) 