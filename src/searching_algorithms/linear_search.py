"""---------------------- LINEAR SEARCH FOR RANGE OF COST ----------------------"""

def linear_search_range_of_cost(arr, low, high):
    """
    Do a linear search on the database for the range of cost specified by the user.
    
    Requires 3 arguments:
    - arr (list): The array of elements to search
    - low (int): The lower bound of the range of cost
    - high (int): The upper bound of the range of cost
    
    Best time complexity: O(n)
    Worst time complexity: O(n)
    Average time complexity: O(n)
    
    Space complexity: O(n) for matched elements
    """
    matchedArr = []
    for record in arr:
        if (record.get_package_cost_per_pax() >= low and record.get_package_cost_per_pax() <= high):
            matchedArr.append(record)
    return matchedArr

"""---------------------- END OF LINEAR SEARCH FOR RANGE OF COST ----------------------"""

"""---------------------- LINEAR SEARCH FOR CUSTOMER NAME/PACKAGE NAME ----------------------"""

def linear_search_for_name(arr, target, typeOfSearch):
    """
    Do a linear search on the database for the customer name
    
    Requires 3 arguments:
    - arr (list): The array of elements to search
    - target (string): The name to search for
    - typeOfSearch (string):"customerName" or "packageName"
    
    Best time complexity: O(n)
    Worst time complexity: O(n)
    Average time complexity: O(n)
    
    Space complexity: O(n) for matched elements
    """
    if (typeOfSearch not in ("customerName", "packageName")):
        raise ValueError(f"Invalid search type, {typeOfSearch}, Must be either 'customerName' or 'packageName'!")

    matchedArr = []
    for i, record in enumerate(arr):
        if (record.get_val(typeOfSearch) == target):
            matchedArr.append((record, i))
    return -1 if (len(matchedArr) == 0) else matchedArr

"""---------------------- END OF LINEAR SEARCH FOR CUSTOMER NAME/PACKAGE NAME ----------------------"""