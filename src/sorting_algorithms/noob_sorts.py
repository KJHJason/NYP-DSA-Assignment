"""
This is a python file that contains slow sorting algorithms 
that is meant to be used as a joke.

Used for the easter egg menu in the assignment.

Algorithms in this file:
- bogosort
- stalinsort
- slowsort
- sleepsort
"""

# import python standard libraries
from random import shuffle
from time import sleep
from threading import Timer

def is_sorted(arr):
    """
    Checks if the array is sorted.
    
    Function is used for bogosort.
    """
    for i in range(len(arr) - 1):
        if (arr[i].get_package_name() > arr[i + 1].get_package_name()):
            return False
    return True

def bogosort(arr):
    """
    Randomly shuffles the array until it is sorted by package name.
    
    Best Time Complexity: O(n)
    Worst Time Complexity: O(inf) as this algorithm has no upper bound
    Average Time Complexity: O(n*n!)
    """
    i = 0

    while (not is_sorted(arr)):
        i += 1
        shuffle(arr)
    return arr, i

def stalinsort(arr):
    """
    Sorts the array by removing any elements that are not in the correct order.
    
    Sorts by customer name.
    
    Best Time Complexity: O(n)
    Worst Time Complexity: O(n)
    Average Time Complexity: O(n)
    
    Space Complexity: O(n)
    """
    if (len(arr) <= 1):
        return arr

    temp = arr[0]
    newArr = []
    for element in arr:
        if (element.get_customer_name() >= temp.get_customer_name()):
            newArr.append(element)
            temp = element

    return newArr

def slowsort(arr, i, j):
    """
    Based on the principle of multiply and surrender which is the opposite of divide and conquer.
    
    Sorts by package cost.
    
    According to GeeksforGeeks, its time complexities are;
    Best Time Complexity: O(n^2.709)
    Worst Time Complexity: O(n^2.709)
    Average Time Complexity: O(n^2.709)
    which is worse than other O(n^2) algorithms such as bubble sort
    
    Works by 
    - Splitting the array into two halves
    - Sort each halves recursively, and then compare the highest element from each half
    - Move the highest element to the end of the array
    - Repeat the process from the top excluding the highest elements at the end for the remaining elements
    """
    if (i >= j):
        return

    mid = (i + j) // 2

    # recursively sort the left half
    slowsort(arr, i, mid)

    # recursively sort the right half
    slowsort(arr, mid + 1, j)

    # swap the elements if first element is greater than the second element
    if (arr[j].get_package_cost_per_pax() < arr[mid].get_package_cost_per_pax()):
        arr[j], arr[mid] = arr[mid], arr[j]

    # recursively sort the whole array again except the last jth element as it is the maximum element
    slowsort(arr, i, j - 1)

def add_to_list(el, arr):
    """
    Adds the element to the list.
    
    Used for sleepsort.
    
    Requires two arguments: 
    - el: the element to be added
    - arr: the list to be added to
    """
    arr.append(el)

def sleepsort(values):
    """
    Creates different threads for each elements and 
    each thread sleeps for an amount of time proportional to the element's value.
    
    Sorts by pax number.
    
    Best Time Complexity: O(max(values))
    Worst Time Complexity: O(max(values))
    Average Time Complexity: O(max(values))
    
    Space Complexity: O(n)
    """
    newArr = []

    maxEl = values[0] # initialise the first element to be the maximum element
    for v in values:
        # if the current element is greater than the maximum element
        if (maxEl.get_pax_num() < v.get_pax_num()): 
            # set the current element as the maximum element
            maxEl = v

        # create a thread for each element with the interval proportional to the element's value
        # and add the element to the list by calling the add_to_list lambda function
        Timer(v.get_pax_num(), add_to_list, (v, newArr)).start()

    # wait for all threads to finish
    sleep(maxEl.get_pax_num() + 1)
    return newArr