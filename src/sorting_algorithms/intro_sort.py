# import python standard libraries
from math import ceil, log2

# import local python files
from .insertion_sort import insertion_sort
from .heap_sort import heap_sort
from .quicksort_utility_functions import median_of_3, partition

SIZE_THRESHOLD = 19 # if array length is less than or equal to SIZE_THRESHOLD, use insertion sort

def intro_sort(arr, reverse=False):
    """
    Introsort or introspective sort is a hybrid sorting algorithm that consists of quick sort, 
    heap sort, and insertion sort.
    It is used in popular languages such as C++ which I have experience with. Hence, I wanted
    to implement std::sort(arr.begin(), arr.end()); in Python.
    
    By using a combination of these three sorting algorithms, introsort is able 
    to sort the array by package name in O(n log n) time for all best, worst, and average case 
    and eliminate quick sort's worst time complexity of O(n^2).
    
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
    while (end - start > SIZE_THRESHOLD):
        if (maxDepth == 0):
            # start using heap sort if the max recursion depth is 0 as to avoid
            # the worst case of O(n^2) when using quick sort
            return heap_sort(arr, reverse=reverse)
        maxDepth -= 1

        # get the pivot for quick sort using the median of three concept
        pivot = median_of_3(arr, start, start + ((end - start) // 2) + 1, end - 1).get_package_name()

        # partition the array around the pivot
        pivotRes = partition(arr, start, end, pivot, reverse=reverse)

        # use the returned value from the partition function and call
        # intro_sort_process() again and change the start pointer to the pivotRes
        # to sort the right side of the array likely using quick sort
        intro_sort_process(arr, pivotRes, end, maxDepth, reverse=reverse)

        # change the end pointer to the pivotRes after the recursive call process
        # of the intro_sort_process() to sort the left side of the array likely using quick sort
        end = pivotRes

    # use insertion sort to sort the array for smaller arrays as it is faster
    return insertion_sort(arr, startIdx=start, endIdx=end, reverse=reverse, mode="packageName")