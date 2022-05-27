def shellsort(arr, reverse=False):
    """
    Shellsort algorithm works like the insertion sort algorithm but
    shellsort will sort the elements that are far apart from each other,
    and progressively reduces the interval gap between the elements to be compared.
    
    Sorts by pax number
    
    Requires 2 arguments:
    - arr (list): The array of elements to sort by package cost per pax
    - reverse (bool): True if the list is to be sorted in descending order (Default: False)
    
    Best Time Complexity: O(n log n)
    Average Time Complexity: O(n log n)
    Worst Time Complexity: O(n^2)
    """
    # initialise the gap by halving the array size first
    gap = len(arr) // 2

    while (gap > 0):
        # loop through the elements in the array in intervals of the gap
        for i in range(gap, len(arr)):
            temp = arr[i] # store the current element as temp
            j = i # initialise j to be the value of i

            # rearrange the elements at n/2, n/4, n/8,... intervals

            # if j is still greater or equal to the gap,
            # checks if the value at j-gap is greater than temp,
            # where j - gap is the element at the first element of the gap
            while (not reverse and j >= gap and arr[j - gap].get_pax_num() > temp.get_pax_num()):
                arr[j] = arr[j - gap] # if it is, replace the value at j with the value at j-gap
                j -= gap

            # same as the previous while loop, but checks if the value at j-gap is less than temp
            while (reverse and j >= gap and arr[j - gap].get_pax_num() < temp.get_pax_num()):
                arr[j] = arr[j - gap]
                j -= gap

            # finally, replace the value at j with temp 
            # in the case where arr[j] was replaced by arr[j - gap]
            # j would be pointed to the first element of the gap
            # hence, effectively swapping the elements
            arr[j] = temp 

        gap //= 2 # halve the gap