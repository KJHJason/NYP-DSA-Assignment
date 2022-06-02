# import python standard libraries
from random import randint, sample

def is_sorted(arr, reverse=False):
    """
    Checks if the array is sorted.
    
    Function is used for bogosort and bozosort.
    
    Requires two arguments:
    - arr: the array to be checked
    - reverse: if True, the array will be sorted in a descending order (default: False)
    """
    for i in range(len(arr) - 1):
        if (not reverse and arr[i].get_package_name() > arr[i + 1].get_package_name()):
            return False
        elif (reverse and arr[i].get_package_name() < arr[i + 1].get_package_name()):
            return False
    return True

def bogo_sort(arr, variant=False, reverse=False):
    """
    Randomly shuffles the array until it is sorted by package name.
    
    Best Time Complexity: O(n)
    Worst Time Complexity: O(inf) as this algorithm has no upper bound
    Average Time Complexity: O(n*n!)

    Requires three arguments:
    - arr: the array to be sorted
    - variant: if True, the array will be sorted using bozosort, a variant of bogosort
        - Bozosort works by randomly swapping two elements in the array until it is sorted by package name.
    - reverse: if True, the array will be sorted in a descending order (default: False)
    
    Returns the number of shuffling/swappings done to sort the array.
    """
    c = 0
    while (not is_sorted(arr, reverse=reverse)):
        if (not variant):
            # shuffle the whole array (bogo sort)
            for i in range(len(arr)):
                # 0 and n-1 as they are inclusive and to avoid IndexError
                idx = randint(0, len(arr) - 1)
                # swap the elements with the randomised index
                arr[i], arr[idx] = arr[idx], arr[i]
        else:
            # swap two random elements in the array (bozo sort)
            idxA, idxB = sample(range(0, len(arr)), 2)
            arr[idxA], arr[idxB] = arr[idxB], arr[idxA]
        c += 1
    return c