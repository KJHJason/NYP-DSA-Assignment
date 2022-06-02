def find_all_name_occurrences(arr, i, target, typeOfSearch):
    """
    Search for all occurrences of the target name specified by the user starting from the index found from a search algorithm.
    Limitations: Array must sorted by target name type
    
    Requires 4 arguments:
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

def cost_lower_index(arr, i, lowerRange, descendingOrder):
    """
    Search for any records within the lowerRange of the cost specified by the user starting from the index found from a search algorithm.
    Limitations: Array must sorted by package cost per pax
    
    Requires 4 arguments:
    - arr (list): The array of elements to search
    - i (int): refers to the index obtained from a search algorithm
    - lowerRange (int)
    - descendingOrder (bool): Indicates the order of the array (True if descending order)
    
    Best time complexity: O(n)
    Worst time complexity: O(n)
    Average time complexity: O(n)
    """
    if (not descendingOrder):
        while (i > 0 and arr[i - 1].get_cost_per_pax() >= lowerRange):
            i -= 1
    else:
        while (i < len(arr) - 1 and arr[i + 1].get_cost_per_pax() >= lowerRange):
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
        while (i < len(arr) - 1 and arr[i + 1].get_cost_per_pax() <= upperRange):
            i += 1
    else:
        while (i > 0 and arr[i - 1].get_cost_per_pax() <= upperRange):
            i -= 1
    return i