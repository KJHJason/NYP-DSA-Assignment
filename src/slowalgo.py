from random import shuffle

def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

def bogosort(arr):
    i = 0
    while (not is_sorted(arr)):
        i += 1
        shuffle(arr)
        print(f"\rSort {i}...", end="")
    return arr

def stalinsort(arr):
    if (len(arr) <= 1):
        return arr
    
    temp = arr[0]
    res = []
    for element in arr:
        if (element >= temp):
            res.append(element)
            temp = element
    
    return res

from threading import Timer
from time import sleep
def sleepsort(arr):
    sleepsort.result = []
    def add_to_list(x):
        sleepsort.result.append(x)

    mx = arr[0]
    for v in arr:
        if (mx < v): 
            mx = v
        Timer(v, add_to_list, [v]).start()

    sleep(mx + 1)
    return sleepsort.result

if __name__ == "__main__":
    print("Bogo sort")
    arr = [1,2,3,4,5,6,7,8,9,10]
    print(bogosort(arr))
    
    arr = [10,9,8,7,6,5,4,3,2,1]
    # print(bogosort(arr))
    print("\nStalin sort")
    arr = [1,2,3,4,5,6,7,8,9,10]
    print(stalinsort(arr))
    
    arr = [1, 2, 5, 3, 6, 4, 10]
    print(stalinsort(arr))
    
    arr = [10, 1, 2, 3, 4]
    print(stalinsort(arr))
    
    print("\nSleep sort")
    arr = [1, 5, 3, 6, 4, 10]
    print(sleepsort(arr))