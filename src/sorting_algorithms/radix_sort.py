def counting_sort_for_radix_sort(arr, place, reverse):
    """
    Counting sort for radix sort
    
    Requires 3 arguments:
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
        index = int(arr[i].get_cost_per_pax() * 100) // place
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

    for i in range(n-1, -1, -1):
        # finding the index of the element in the count array by calculating the cost divided by the 
        # place value modulo 10 to get the remainder as to avoid index out of range error
        countArrIdx = (int(arr[i].get_cost_per_pax() * 100) // place) % 10

        # we will retrieve the element from the countArr using the countArrIdx we calculated above.
        # the retrieved element minus one (to account for indexing) will be the index of the element 
        # in the output array
        outputArr[countArr[countArrIdx] - 1] = arr[i]

        # decrement the count array by 1 for the next element
        countArr[countArrIdx] -= 1

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
    maxCostEl = max(arr, key=lambda x : x.get_cost_per_pax())
    maxCost = int(maxCostEl.get_cost_per_pax() * 100)

    # Do counting sort for every digit based on palce value
    place = 1
    while (maxCost // place > 0):
        counting_sort_for_radix_sort(arr, place, reverse=reverse)
        place *= 10