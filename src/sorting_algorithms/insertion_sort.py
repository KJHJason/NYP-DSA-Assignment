def insertion_sort(arr, reverse=False):
    """
    Do a insertion sort by package cost per pax
    
    Requires 2 arguments:
    - arr (list): The array of elements to sort by package cost per pax
    - reverse (bool): True if the list is to be sorted in descending order (Default: False)
    
    Best time complexity: O(n)
    Worst time complexity: O(n^2)
    Average time complexity: O(n^2)
    """
    dbSize = len(arr)
    for i in range(1, dbSize):
        el = arr[i] # save the value to be positioned
        
        j = i - 1
        if (reverse):
            # Compare el with each element on the left of it and move the smaller element to the right ahead of their current position
            while (j >= 0 and arr[j].get_package_cost_per_pax() < el.get_package_cost_per_pax()):
                arr[j + 1] = arr[j]
                j -= 1
        else:
            # Compare el with each element on the left of it and move the bigger element to the right ahead of their current position
            while (j >= 0 and arr[j].get_package_cost_per_pax() > el.get_package_cost_per_pax()):
                arr[j + 1] = arr[j ]
                j -= 1

        arr[j + 1] = el