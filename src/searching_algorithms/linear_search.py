"""---------------------- LINEAR SEARCH FOR RANGE OF COST ----------------------"""

def linear_search_range_of_cost(arr, low, high):
    """
    Do a linear search on the database for the range of cost specified by the user.
    
    Requires 3 arguments:
    - arr (list): The array of elements to search
    - low (int)
    - high (int)
    
    Best time complexity: O(n)
    Worst time complexity: O(n)
    Average time complexity: O(n)
    """
    matchedArr = []
    for record in arr:
        if (record.get_package_cost_per_pax() >= low and record.get_package_cost_per_pax() <= high):
            matchedArr.append(record)
    return matchedArr

"""---------------------- END OF LINEAR SEARCH FOR RANGE OF COST ----------------------"""

"""---------------------- LINEAR SEARCH FOR CUSTOMER NAME/PACKAGE NAME ----------------------"""

def get_val(record, typeOfVal):
    """
    Get the respective attribute from the RecordData object based on the typeOfVal given.
    
    Used in the linear search function below.
    
    Requires 2 arguments:
    - record (RecordData)
    - typeOfVal (str): "customer" or "package"
    """
    return record.get_customer_name() if (typeOfVal == "customer") \
                                      else record.get_package_name()

def linear_search(arr, target, typeOfSearch):
    """
    Do a linear search on the database for the customer name
    
    Requires 3 arguments:
    - arr (list): The array of elements to search
    - target (string)
    - typeOfSearch (string) <-- "customer" or "package"
    
    Best time complexity: O(n)
    Worst time complexity: O(n)
    Average time complexity: O(n)
    """
    if (typeOfSearch not in ("customer", "package")):
        raise ValueError(f"Invalid search type, {typeOfSearch}, Must be either \"customer\" or \"package\"!")

    matchedArr = []
    for record in arr:
        if (get_val(record, typeOfSearch) == target):
            matchedArr.append(record)
    return -1 if (len(matchedArr) == 0) else matchedArr

"""---------------------- END OF LINEAR SEARCH FOR CUSTOMER NAME/PACKAGE NAME ----------------------"""