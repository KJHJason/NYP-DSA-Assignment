# import python standard libraries
from math import floor, log2

# import local python files
from .insertion_sort import insertion_sort
from .heap_sort import heap_sort
from .quicksort_utility_functions import median_of_3, partition

# define the maximum length of the array before using insertion sort
SIZE_THRESHOLD = 16 # if less than or equal to 16 elements, introsort will use insertion sort.
                    # I used the integer 16 as the threshold because GNU Standard C++ library also uses it;
                    # https://gcc.gnu.org/onlinedocs/gcc-12.1.0/libstdc++/api/a00650_source.html#l01838

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
    - reverse (bool): True if the array is to be sorted in descending order (Default: False)
    
    Best time complexity: O(n log n)
    Worst time complexity: O(n log n)
    Average time complexity: O(n log n)
    
    Space complexity: O(logn) for the heap sort on a sub-array of the array
    
    More details:
    - https://en.wikipedia.org/wiki/Introsort
    """
    if (not arr):
        # if array is empty, return
        return

    # calculate the max recursion depth of the algorithm for quick sort 
    # as to use heap sort when the max recursion depth has been reached
    # to avoid the worse case complexity of O(n^2) when using quick sort
    maxDepth = 2 * floor(log2(len(arr)))

    intro_sort_process(arr, 0, len(arr), maxDepth, reverse=reverse)

def intro_sort_process(arr, start, end, maxDepth, reverse=False):
    """
    The main function that implements the introsort algorithm with reference to
    C++ Standard Library's std::sort();
    https://gcc.gnu.org/onlinedocs/gcc-12.1.0/libstdc++/api/a00650_source.html#l01908
    
    Requires 5 arguments:
    - arr (list): The array of elements to sort by package name
    - start (int): The starting index of the array
    - end (int): The ending index of the array
    - maxDepth (int): The max recursion depth of the algorithm before using heap sort
    - reverse (bool): True if the list is to be sorted in descending order (Default: False)
    """
    while (end - start > SIZE_THRESHOLD):
        if (maxDepth == 0):
            # base case 1
            # start using heap sort if the max recursion depth is 0 as to avoid
            # the worst case of O(n^2) when using quick sort
            arrCopy = arr[start:end+1]
            heap_sort(arrCopy, reverse=reverse)
            arr[start:end+1] = arrCopy

            # explicitly delete the copy of the array for garbage collector to free up memory
            del arrCopy
            return

        maxDepth -= 1

        # get the pivot for quick sort using the median of three concept
        pivot = median_of_3(arr, start, start + ((end - start) // 2) + 1, end - 1).get_package_name()

        # partition the array around the pivot
        partitionRes = partition(arr, start, end, pivot, reverse=reverse)

        # recursive case:
        # use the returned value from the partition function and recursively
        # sort the RIGHT side of the array by changing the start argument
        # to the returned value from the partition function
        intro_sort_process(arr, partitionRes, end, maxDepth, reverse=reverse)

        # change the end pointer to partitionRes after the recursive call process 
        # of sorting the right side of the array to sort the LEFT side of the array
        # in the next while loop iteration and start sorting the LEFT side of the array recursively
        end = partitionRes

    # base case 2
    # use insertion sort to sort the array/sub-array for smaller arrays as it is faster
    return insertion_sort(arr, startIdx=start, endIdx=end, reverse=reverse, mode="packageName")