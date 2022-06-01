"""
This is a python file that contains slow sorting algorithms 
that is meant to be used as a joke.

Used for the easter egg menu in the assignment.

Algorithms in this file:
- bogo sort
    - bozo sort (a variant of bogo sort)
- stalin sort
- slow sort
- sleep sort
- gnome sort
"""

# import python standard libraries
from random import randint, sample, shuffle
from time import sleep
from threading import Timer

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

def stalin_sort(arr, reverse=False):
    """
    Sorts the array by removing any elements that are not in the correct order.
    
    Sorts by customer name.
    
    Best Time Complexity: O(n)
    Worst Time Complexity: O(n)
    Average Time Complexity: O(n)
    
    Space Complexity: O(n)

    Requires two arguments:
    - arr: the array to be sorted
    - reverse: if True, the array will be sorted in a descending order (default: False)
    
    Returns the new sorted array.
    """
    if (len(arr) <= 1):
        return arr

    temp = arr[0]
    newArr = []
    for el in arr:
        if (not reverse):
            if (el.get_customer_name() >= temp.get_customer_name()):
                newArr.append(el)
                temp = el
        else:
            if (el.get_customer_name() <= temp.get_customer_name()):
                newArr.append(el)
                temp = el

    return newArr

def slow_sort(arr, i, j, reverse=False):
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
    
    Requires four arguments:
    - arr: the array to be sorted
    - i: the starting index of the array
    - j: the ending index of the array
    - reverse: if True, the array will be sorted in a descending order (default: False)
    """
    # base case
    if (i >= j):
        return

    mid = (i + j) // 2

    # recursively sort the left half
    slow_sort(arr, i, mid, reverse=reverse)

    # recursively sort the right half
    slow_sort(arr, mid + 1, j, reverse=reverse)

    if (not reverse):
         # swap the elements if jth element is greater than the mid element
        if (arr[j].get_package_cost_per_pax() < arr[mid].get_package_cost_per_pax()):
            arr[j], arr[mid] = arr[mid], arr[j]
    else:
        # swap the elements if jth element is less than the mid element
        if (arr[j].get_package_cost_per_pax() > arr[mid].get_package_cost_per_pax()):
            arr[j], arr[mid] = arr[mid], arr[j]

    # recursively sort the whole array again except the last jth element as it is the maximum element
    slow_sort(arr, i, j - 1, reverse=reverse)

def add_to_list(el, arr):
    """
    Adds the element to the list.
    
    Used for sleepsort.
    
    Requires two arguments: 
    - el: the element to be added
    - arr: the list to be added to
    """
    arr.append(el)

def sleep_sort(arr, reverse=False):
    """
    Creates different threads for each elements and 
    each thread sleeps for an amount of time proportional to the element's value.
    
    Sorts by pax number.
    
    Best Time Complexity: O(max(arr))
    Worst Time Complexity: O(max(arr))
    Average Time Complexity: O(max(arr))
    
    Space Complexity: O(n)
    
    Requires two arguments:
    - arr: the array to be sorted
    - reverse: if True, the array will be sorted in a descending order (default: False)
    
    Returns the new sorted array.
    """
    newArr = []

    maxEl = arr[0] # initialise the first element to be the maximum element
    for el in arr:
        # if the current element is greater than the maximum element
        if (maxEl.get_pax_num() < el.get_pax_num()): 
            # set the current element as the maximum element
            maxEl = el

        # create a thread for each element with the interval proportional to the element's value
        # and add the element to the list by calling the add_to_list function
        Timer(el.get_pax_num(), add_to_list, (el, newArr)).start()

    # wait for all threads to finish
    sleep(maxEl.get_pax_num() + 1)
    if (not reverse):
        # return sorted array (in ascending order)
        return newArr

    # treat the array like a stack using .pop() to reverse it and return a new list
    # instead of using python's in-built .reverse() or [::-1]
    return [newArr.pop() for _ in range(len(newArr))]

def gnome_sort(arr, reverse=False):
    """
    ⣿⣿⣿⣿⣿⠟⠉⠁⠄⠄⠄⠈⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⠏⠄⠄⠄⠄⠄⠄⠄⠄⠄⠸⢿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣏⠄⡠⡤⡤⡤⡤⡤⡤⡠⡤⡤⣸⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣗⢝⢮⢯⡺⣕⢡⡑⡕⡍⣘⢮⢿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⡧⣝⢮⡪⡪⡪⡎⡎⡮⡲⣱⣻⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⠟⠁⢸⡳⡽⣝⢝⢌⢣⢃⡯⣗⢿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⠟⠁⠄⠄⠄⠹⡽⣺⢽⢽⢵⣻⢮⢯⠟⠿⠿⢿⣿⣿⣿⣿⣿
    ⡟⢀⠄⠄⠄⠄⠄⠙⠽⠽⡽⣽⣺⢽⠝⠄⠄⢰⢸⢝⠽⣙⢝⢿
    ⡄⢸⢹⢸⢱⢘⠄⠄⠄⠄⠄⠈⠄⠄⠄⣀⠄⠄⣵⣧⣫⣶⣜⣾
    ⣧⣬⣺⠸⡒⠬⡨⠄⠄⠄⠄⠄⠄⠄⣰⣿⣿⣿⣿⣿⣷⣽⣿⣿
    ⣿⣿⣿⣷⠡⠑⠂⠄⠄⠄⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣄⠠⢀⢀⢀⡀⡀⠠⢀⢲⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⢐⢀⠂⢄⠇⠠⠈⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣧⠄⠠⠈⢈⡄⠄⢁⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⡀⠠⠐⣼⠇⠄⡀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣯⠄⠄⡀⠈⠂⣀⠄⢀⠄⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣶⣄⣀⠐⢀⣸⣷⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿
    
    Gnome sort, also known as stupid sort, is a sorting algorithm that works by 
    comparing the current element with the previous element and starts swapping elements 
    if they are not in order.
    
    E.g. arr = [3, 2, 1], sorting in ascending order...
    First iteration: [2, 3, 1], i = 0 (swap 2 and 3)
    Second iteration: [2, 3, 1], i = 2 (no swap)
    Third iteration: [2, 1, 3], i = 1 (swap 1 and 3)
    Fourth iteration: [1, 2, 3], i = 0 (swap 1 and 2)
    Fifth iteration: [1, 2, 3], i = 2 (no swap)
    Sixth iteration: [1, 2, 3], i = 3 (no swap and end loop)
    
    Similar to insertion sort but it is significantly slower than insertion as
    there is a lot of swappings involved.
    
    Useful resources:
    - GNOME SORT: How (NOT) To Sort Your Arrays.
        - https://youtu.be/pMjAllOR3eY
    
    Requires 2 arguments:
    - arr: the array to be sorted
    - reverse: if True, sorts in descending order (defaults to False)
    
    Best Time Complexity: O(n)
    Worst Time Complexity: O(n^2)
    Average Time Complexity: O(n^2)
    """
    i = 0
    while (i < len(arr)):
        # if the current element is the first element, 
        # increment i to move to the next element
        if (i == 0):
            i += 1

        if (not reverse): 
            # ascending order
            if (arr[i - 1].get_pax_num() <= arr[i].get_pax_num()):
                # if the current element is greater than or equal to the previous element,
                # increment i to check the next element since it's in the correct order
                i += 1
            else:
                # if the current element is not in order, 
                # swap it with the previous element and decrement by 1
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                i -= 1
        else: 
            # descending order
            if (arr[i - 1].get_pax_num() >= arr[i].get_pax_num()):
                # if the current element is smaller than or equal to the previous element,
                # increment i to check the next element since it's in the correct order
                i += 1
            else:
                # if the current element is not in order, 
                # swap it with the previous element and decrement by 1
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                i -= 1