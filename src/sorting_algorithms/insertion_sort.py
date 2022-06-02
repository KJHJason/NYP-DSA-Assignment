from tracemalloc import start


def insertion_sort(arr, reverse=False, startIdx=None, endIdx=None, mode="costPerPax"):
    """
    Do a insertion sort by package cost per pax and package name
    
    Requires 5 arguments:
    - arr (list): The array of elements to sort by package cost per pax
    - reverse (bool): True if the list is to be sorted in descending order 
        - Default: False
    - startIdx (int): The index of the first element to sort 
        - Default: 0
    - endIdx (int): The index of the last element to sort 
        - Default: len(arr)
    - mode (str): The mode of sorting. Can be "costPerPax" or "packageName", etc.
        - default: "costPerPax"
    
    Best time complexity: O(n)
    Worst time complexity: O(n^2)
    Average time complexity: O(n^2)
    """
    if (startIdx is None and endIdx is None):
        endIdx = endIdx or len(arr)
        startIdx = 1

    for i in range(startIdx, endIdx):
        el = arr[i] # save the value to be positioned

        j = i - 1
        if (reverse):
            # Compare el with each element on the left of it and move the smaller element to the right ahead of their current position
            while (j >= 0 and arr[j].get_val(attribute=mode) < el.get_val(attribute=mode)):
                arr[j + 1] = arr[j]
                j -= 1
        else:
            # Compare el with each element on the left of it and move the bigger element to the right ahead of their current position
            while (j >= 0 and arr[j].get_val(attribute=mode) > el.get_val(attribute=mode)):
                arr[j + 1] = arr[j]
                j -= 1

        arr[j + 1] = el