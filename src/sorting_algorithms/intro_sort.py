# import python standard libraries
from math import ceil, log2

# import local python files
from .insertion_sort import insertion_sort
from .heap_sort import heap_sort
from .quicksort_utility_functions import median_of_3, partition

# define the maximum length of the array before using insertion sort
SIZE_THRESHOLD = 16 # if less than 16 elements, introsort will use insertion sort 
                    # use the integer 16 as the threshold as GNU Standard C++ library also uses this value

def intro_sort(arr, reverse=False):
    """
    Introsort or introspective sort is a hybrid sorting algorithm that consists of quick sort, 
    heap sort, and insertion sort.
    It is used in popular languages such as C++ which I have experience with. Hence, I wanted
    to implement std::sort(arr.begin(), arr.end()); in Python.
    
    By using a combination of these three sorting algorithms, introsort is able 
    to sort the array by package name in O(n log n) time for all best, worst, and average case 
    and eliminate quick sort's worst time complexity of O(n^2). 
    However, this algorithm is not stable due to the use of the quick sort algorithm.
    
    Why not just use heap sort?
    - Quick sort is actually faster than heap sort in most cases.
    - The disadvantage of quick sort is its worst time complexity of O(n^2)
    - Hence, introsort combines quick sort for its efficiency and 
      heap sort to avoid quick sort's worst time complexity of O(n^2)
    
    Requires 2 arguments:
    - arr (list): The array of elements to sort by package name
    - reverse (bool): True if the list is to be sorted in descending order (Default: False)
    
    Best time complexity: O(n log n)
    Worst time complexity: O(n log n)
    Average time complexity: O(n log n)
    
    More details:
    - https://en.wikipedia.org/wiki/Introsort
    """
    if (not arr):
        # if list is empty, return
        return

    # calculate the max recursion depth of the algorithm for quick sort 
    # as to use heap sort when the max recursion depth has been reached
    # to avoid the worse case complexity of O(n^2) when using quick sort
    maxDepth = 2 * ceil(log2(len(arr)))

    intro_sort_process(arr, 0, len(arr), maxDepth, reverse=reverse)

def intro_sort_process(arr, start, end, maxDepth, reverse=False):
    """
    The main function that implements the introsort algorithm.
    
    Requires 5 arguments:
    - arr (list): The array of elements to sort by package name
    - start (int): The starting index of the array
    - end (int): The ending index of the array
    - maxDepth (int): The max recursion depth of the algorithm before using heap sort
    - reverse (bool): True if the list is to be sorted in descending order (Default: False)
    """
    # if the array length is less than SIZE_THRESHOLD, 
    if (end - start < SIZE_THRESHOLD):
        # use insertion sort as it is faster for smaller arrays
        insertion_sort(arr, startIdx=start, endIdx=end, reverse=reverse, mode="packageName")
        return

    # if the max recursion depth has been reached, use heap sort
    if (maxDepth == 0):
        # usually happens for large arrays (to avoid quick sort's worst case complexity of O(n^2))
        heap_sort(arr, reverse=reverse)
        return

    # get the pivot for quick sort using the median of three concept to optimise quick sort
    # For the mid argument, I used the formula, mid = start + ((end - start) // 2) 
    # to avoid overflow/index out of bounds
    pivot = median_of_3(arr, start, start + ((end - start) // 2), end - 1).get_package_name()

    # partition the array around the pivot
    partitionRes = partition(arr, start, end, pivot, reverse=reverse)

    # use the returned value from the partition function and recursively
    # sort the RIGHT side of the array by changing the start argument
    # to the returned value from the partition function
    intro_sort_process(arr, partitionRes, end, maxDepth-1, reverse=reverse)

    # use the returned value from the partition function and recursively
    # sort the LEFT side of the array by changing the end argument
    # to the returned value from the partition function
    intro_sort_process(arr, start, partitionRes, maxDepth-1, reverse=reverse)