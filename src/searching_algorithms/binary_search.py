"""---------------------- BINARY SEARCH FOR PACKAGE NAME ----------------------"""

def find_all_name_occurrences(arr, i, target, typeOfSearch):
    """
    Search for all occurrences of the target name specified by the user starting from the index found from a search algorithm.
    Limitations: Array must sorted by target name type
    
    Requires 3 arguments:
    - arr (list): The array of elements to search
    - i (int): refers to the index obtained from a search algorithm
    - target (string): package name or customer name
    - typeOfSearch (str): indicates what to search by (customerName or packageName)
    
    Best time complexity: O(n)
    Worst time complexity: O(n)
    Average time complexity: O(n)
    """
    iCopy = i
    # search the right
    while (i < len(arr) - 1 and arr[i + 1].get_val(typeOfSearch) == target):
        i += 1

    # search the left
    while (iCopy > 0 and arr[iCopy - 1].get_val(typeOfSearch) == target):
        iCopy -= 1

    return iCopy, i

def binary_search_for_name(arr, target, descendingOrder, typeOfSearch, l=None, r=None):
    """
    Do a binary search on the database for the package name
    
    Requires 3 argument:
    - arr (list): The array of elements to search
    - target (string)
    - descendingOrder (bool): Indicates the order of the array (True if descending order)
    - typeOfSearch (str): indicates what to search by (customerName or packageName)
    
    Optional arguments:
    - l (int): left index (defaults to 0)
    - r (int): right index (defaults to n-1)
    
    Best time complexity: O(1)
    Worst time complexity: O(log(n))
    Average time complexity: O(log(n))
    """
    if (l is None and r is None):
        l = 0
        r = len(arr) - 1

    while (l <= r):
        mid = (l + r) // 2
        
        # return mid if the package name is found in the subarray
        if (arr[mid].get_val(typeOfSearch) == target):
            # will return the index of the first and last occurrence of the package name in a tuple
            return find_all_name_occurrences(arr, mid, target, typeOfSearch) 

        if (not descendingOrder):
            # if the package name to find is greater than mid, search the right half
            if (arr[mid].get_val(typeOfSearch) < target):
                l = mid + 1
            # if the package name to find is smaller than mid, search the left half
            else:
                r = mid - 1
        else:
            # if the package name to find is smaller than mid, search the right half
            if (arr[mid].get_val(typeOfSearch) > target):
                l = mid + 1
            # if the package name to find is greater than mid, search the left half
            else:
                r = mid - 1

    return -1, -1 # return -1 if the package name is not found

"""---------------------- END OF BINARY SEARCH FOR PACKAGE NAME ----------------------"""

"""---------------------- BINARY SEARCH FOR PACKAGE COST PER PAX ----------------------"""

def cost_lower_index(arr, i, lowerRange, descendingOrder):
    """
    Search for any records within the lowerRange of the cost specified by the user starting from the index found from a search algorithm.
    Limitations: Array must sorted by package cost per pax
    
    Requires 4 arguments:
    - arr (list): The array of elements to search
    - i (int) <-- refers to the index obtained from a search algorithm
    - lowerRange (int)
    - descendingOrder (bool): Indicates the order of the array (True if descending order)
    
    Best time complexity: O(n)
    Worst time complexity: O(n)
    Average time complexity: O(n)
    """
    if (not descendingOrder):
        while (i > 0 and arr[i - 1].get_package_cost_per_pax() >= lowerRange):
            i -= 1
    else:
        while (i < len(arr) - 1 and arr[i + 1].get_package_cost_per_pax() >= lowerRange):
            i += 1
    return i

def cost_upper_index(arr, i, upperRange, descendingOrder):
    """
    Search for any records within the upperRange of the cost specified by the user starting from the index found from a search algorithm.
    Limitations: Array must sorted by package cost per pax
    
    Requires 4 arguments:
    - arr (list): The array of elements to search
    - i (int) <-- refers to the index obtained from a search algorithm
    - upperRange (int)
    - descendingOrder (bool): Indicates the order of the array (True if descending order)
    
    Best time complexity: O(n)
    Worst time complexity: O(n)
    Average time complexity: O(n)
    """
    if (not descendingOrder):
        while (i < len(arr) - 1 and arr[i + 1].get_package_cost_per_pax() <= upperRange):
            i += 1
    else:
        while (i > 0 and arr[i - 1].get_package_cost_per_pax() <= upperRange):
            i -= 1
    return i

def binary_search_for_range_of_cost(arr, lowRange, highRange, descendingOrder):
    """
    Do a binary search on the database for the package name
    
    Requires 4 arguments:
    - arr (list): The array of elements to search
    - lowRange (int/float)
    - highRange (int/float)
    - descendingOrder (bool): Indicates the order of the array (True if descending order)
    
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
            if (descendingOrder):
                return cost_upper_index(arr, mid, highRange, descendingOrder),\
                    cost_lower_index(arr, mid, lowRange, descendingOrder)
            else:
                return cost_lower_index(arr, mid, lowRange, descendingOrder), \
                    cost_upper_index(arr, mid, highRange, descendingOrder)

        if (not descendingOrder):
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