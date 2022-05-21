"""---------------------- BINARY SEARCH FOR PACKAGE NAME ----------------------"""

def findAllNameOccurrences(arr, i, name):
    """
    Search for all occurrences of the target name specified by the user starting from the index found from a search algorithm.
    Limitations: Array must sorted by target name type
    
    Requires 3 arguments:
    - arr (list): The array of elements to search
    - i (int) <-- refers to the index obtained from a search algorithm
    - name (string) <-- package name
    
    Best time complexity: O(n)
    Worst time complexity: O(n)
    Average time complexity: O(n)
    """
    iCopy = i
    # search the right
    while (i < len(arr) - 1 and arr[i + 1].get_package_name() == name):
        i += 1

    # search the left
    while (iCopy > 0 and arr[iCopy - 1].get_package_name() == name):
        iCopy -= 1

    return iCopy, i

def binary_search_for_package_name(arr, packageName, descending_order):
    """
    Do a binary search on the database for the package name
    
    Requires 3 argument:
    - arr (list): The array of elements to search
    - packageName (string)
    - descending_order (bool): Indicates the order of the array (True if descending order)
    
    Best time complexity: O(1)
    Worst time complexity: O(log(n))
    Average time complexity: O(log(n))
    """
    l = 0
    r = len(arr) - 1
    while (l <= r):
        mid = (l + r) // 2
        
        # return mid if the package name is found in the subarray
        if (arr[mid].get_package_name() == packageName):
            # will return the index of the first and last occurrence of the package name in a tuple
            return findAllNameOccurrences(arr, mid, packageName) 

        if (not descending_order):
            # if the package name to find is greater than mid, search the right half
            if (arr[mid].get_package_name() < packageName):
                l = mid + 1
            # if the package name to find is smaller than mid, search the left half
            else:
                r = mid - 1
        else:
            # if the package name to find is smaller than mid, search the right half
            if (arr[mid].get_package_name() > packageName):
                l = mid + 1
            # if the package name to find is greater than mid, search the left half
            else:
                r = mid - 1

    return -1, -1 # return -1 if the package name is not found

"""---------------------- END OF BINARY SEARCH FOR PACKAGE NAME ----------------------"""

"""---------------------- BINARY SEARCH FOR PACKAGE COST PER PAX ----------------------"""

def costLowerIndex(arr, i, lowerRange, descending_order):
    """
    Search for any records within the lowerRange of the cost specified by the user starting from the index found from a search algorithm.
    Limitations: Array must sorted by package cost per pax
    
    Requires 4 arguments:
    - arr (list): The array of elements to search
    - i (int) <-- refers to the index obtained from a search algorithm
    - lowerRange (int)
    - descending_order (bool): Indicates the order of the array (True if descending order)
    
    Best time complexity: O(n)
    Worst time complexity: O(n)
    Average time complexity: O(n)
    """
    if (not descending_order):
        while (i > 0 and arr[i - 1].get_package_cost_per_pax() >= lowerRange):
            i -= 1
    else:
        while (i < len(arr) - 1 and arr[i + 1].get_package_cost_per_pax() >= lowerRange):
            i += 1
    return i

def costUpperIndex(arr, i, upperRange, descending_order):
    """
    Search for any records within the upperRange of the cost specified by the user starting from the index found from a search algorithm.
    Limitations: Array must sorted by package cost per pax
    
    Requires 4 arguments:
    - arr (list): The array of elements to search
    - i (int) <-- refers to the index obtained from a search algorithm
    - upperRange (int)
    - descending_order (bool): Indicates the order of the array (True if descending order)
    
    Best time complexity: O(n)
    Worst time complexity: O(n)
    Average time complexity: O(n)
    """
    if (not descending_order):
        while (i < len(arr) - 1 and arr[i + 1].get_package_cost_per_pax() <= upperRange):
            i += 1
    else:
        while (i > 0 and arr[i - 1].get_package_cost_per_pax() <= upperRange):
            i -= 1
    return i

def binary_search_for_range_of_cost(arr, lowRange, highRange, descending_order):
    """
    Do a binary search on the database for the package name
    
    Requires 4 arguments:
    - arr (list): The array of elements to search
    - lowRange (int/float)
    - highRange (int/float)
    - descending_order (bool): Indicates the order of the array (True if descending order)
    
    Best time complexity: O(1)
    Worst time complexity: O(log(n))
    Average time complexity: O(log(n))
    """
    l = 0
    r = len(arr) - 1
    while (l <= r):
        mid = (l + r) // 2
        
        # return mid if the range is found in the subarray
        if (arr[mid].get_package_cost_per_pax() >= lowRange and arr[mid].get_package_cost_per_pax() <= highRange):
            if (descending_order):
                return costUpperIndex(arr, mid, highRange, descending_order),\
                    costLowerIndex(arr, mid, lowRange, descending_order)
            else:
                return costLowerIndex(arr, mid, lowRange, descending_order), \
                    costUpperIndex(arr, mid, highRange, descending_order)

        if (not descending_order):
            # if the lower range to find is greater than mid, search the right half
            if (arr[mid].get_package_cost_per_pax() < lowRange):
                l = mid + 1
            # if the upper range to find is less than mid, search the left half
            else:
                r = mid - 1
        else:
            # if the upper range to find is greater than mid, search the right half
            if (arr[mid].get_package_cost_per_pax() > highRange):
                l = mid + 1
            # if the lower range to find is less than mid, search the left half
            else:
                r = mid - 1

    return -1, -1 # return -1 if the package name is not found

"""---------------------- END OF BINARY SEARCH FOR PACKAGE COST PER PAX ----------------------"""