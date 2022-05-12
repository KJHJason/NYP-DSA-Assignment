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
    newArr = []
    for i in range(len(arr) - 1):
        if (arr[i] < arr[i + 1]):
            newArr.append(arr[i])

        if (i == len(arr) - 2):
            newArr.append(arr[i + 1])
    return newArr

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9,10]
    print(bogosort(arr))
    
    arr = [10,9,8,7,6,5,4,3,2,1]
    # print(bogosort(arr))

    arr = [1,2,3,4,5,6,7,8,9,10]
    print(stalinsort(arr))
    
    arr = [1, 5, 2, 2, 1]
    print(stalinsort(arr))