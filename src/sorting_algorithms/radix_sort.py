def counting_sort_for_radix_sort(arr, place, reverse):
    """
    Counting sort for radix sort
    
    Requires 3 argument:
    - arr (list): The array of elements to sort by package cost per pax
    - place (int): The current digit number
    - reverse (bool): True if the list is to be sorted in descending order
    
    Best time complexity: O(n+b)
    Worst time complexity: O(n+b)
    Average time complexity: O(n+b)
    
    Space complexity: O(n+b)
    Where n is the number of elements and b is the base number, 10
    """
    n = len(arr)
    outputArr = [0] * n
    countArr = [0] * 10

    # Calculate count of elements
    for i in range(n):
        index = int(arr[i].get_package_cost_per_pax() * 100) // place
        countArr[index % 10] += 1

    # Calculate cumulative count...
    if (reverse):
        # in a descending order
        for i in range(8, -1, -1):
            countArr[i] += countArr[i + 1]
    else:
        # in an ascending order
        for i in range(1, 10):
            countArr[i] += countArr[i - 1]

    # Find the index of each element and place it in the output array
    for i in range(n-1, -1, -1):
        index = int(arr[i].get_package_cost_per_pax() * 100) // place
        outputArr[countArr[index % 10] - 1] = arr[i]
        countArr[index % 10] -= 1

    # Copy the sorted elements into original array
    for i in range(n):
        arr[i] = outputArr[i]

def radix_sort(arr, reverse=False):
    """
    Do a radix sort (base 10) on the database by cost per pax

    Requires 2 arguments:
    - arr (list): The array of elements to sort by package cost per pax
    - reverse (bool): True if the list is to be sorted in descending order (Default: False)
    
    Best time complexity: O(d(n+b))
    Worst time complexity: O(d(n+b))
    Average time complexity: O(d(n+b))
    where d is the number of digits in the largest number
    and b is the base number, 10. 
    
    Note that I multiplied the cost per pax by 100 as 
    it is a float with a decimal place of 2
    """
    # Find the maximum number to know number of digits
    maxCostEl = max(arr, key=lambda x : x.get_package_cost_per_pax())
    maxCost = int(maxCostEl.get_package_cost_per_pax() * 100)

    # Do counting sort for every digit based on palce value
    place = 1
    while (maxCost // place > 0):
        counting_sort_for_radix_sort(arr, place, reverse=reverse)
        place *= 10