# NYP Data Structures & Algorithms Assignment

This assignment (40%) provided me the chance to implement the data structures and algorithms we learnt in class and also through personal research.

## Minimum Requirements
1. Design a suitable data structure (e.g. by making use of Python list, dictionary, objects, etc.) to manage the staycation booking records. You are required to store the following staycation booking records. Each record has: Package Name, Customer Name, number of pax and Package Cost per pax.
2. The data structure will store up to 10 records. All records are to be pre-initialized in the program.
3. Design a menu for the application to allow the user to perform the following:
    - Display all records
    - Sort record by Customer Name using Bubble sort
    - Sort record by Package Name using Selection sort
    - Sort record by Package Cost using Insertion sort
    - Search record by Customer Name using Linear Search and update record
    - Search record by Package Name using Binary Search and update record
    - List records range from $X to $Y. e.g $100-200
    - Exit Application
4. All sorting algorithms are in ascending order only. After sorting, the record will be stored as sorted order for next display.
5. All search algorithms MUST ignore case sensitivity. Upon update, the updated record will be stored.
6. Error handling is required.
7. User friendly interface and design

### Additional Data Structures & Algorithms Implemented

- Efficient Sorting Algorithms
    1. Introsort [intro_sort.py](src/sorting_algorithms/intro_sort.py)
    2. Heap sort [heap_sort.py](src/sorting_algorithms/heap_sort.py)
    3. Tree sort [tree_sort.py](src/data_structures/AVLTree.py)
    4. Radix sort [radix_sort.py](src/sorting_algorithms/radix_sort.py)
    5. Shell sort [shellsort.py](src/sorting_algorithms/shellsort.py)

- Bad Sorting Algorithms
    1. Bogosort [bogo_sort.py](src/bad_sorting_algorithms/bogo_sort.py)
    2. Bozosort [bogo_sort.py](src/bad_sorting_algorithms/bogo_sort.py)
    3. Gnome sort [gnome_sort.py](src/bad_sorting_algorithms/gnome_sort.py)
    4. Pancake sort [pancake_sort.py](src/bad_sorting_algorithms/pancake_sort.py)
    5. Sleep sort [sleep_sort.py](src/bad_sorting_algorithms/sleep_sort.py)
    6. Slow sort [slow_sort.py](src/bad_sorting_algorithms/slow_sort.py)
    7. Stalin sort [stalin_sort.py](src/bad_sorting_algorithms/stalin_sort.py)

- Search Algorithms
    1. Fibonacci search [fibonacci_search.py](src/searching_algorithms/fibonacci_search.py)
    2. Exponential Search [exponential_search.py](src/searching_algorithms/exponential_search.py)

- Data Structures
    1. AVL Tree [AVLTree.py](src/data_structures/AVLTree.py)
    2. Doubly Linked List [DoublyLinkedList.py](src/data_structures/DoublyLinkedList.py)