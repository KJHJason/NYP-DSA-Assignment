from turtle import left
from regex import R


class RecordData:
    def __init__(self, packageName, customerName, paxNum, packageCostPerPax):
        self.__packageName = packageName.title()
        self.__customerName = customerName.title()
        self.__paxNum = paxNum
        self.__packageCostPerPax = packageCostPerPax
    
    def set_package_name(self, packageName):
        self.__packageName = packageName.title()
    def get_package_name(self):
        return self.__packageName
    
    def set_customer_name(self, customerName):
        self.__customerName = customerName.title()
    def get_customer_name(self):
        return self.__customerName
    
    def set_pax_num(self, paxNum):
        self.__paxNum = paxNum
    def get_pax_num(self):
        return self.__paxNum
    
    def set_package_cost_per_pax(self, packageCostPerPax):
        self.__packageCostPerPax = packageCostPerPax
    def get_package_cost_per_pax(self):
        return self.__packageCostPerPax
    
    def __str__(self):
        return f"""
Package Name: {self.__packageName} 
Customer Name: {self.__customerName}
Number of Pax: {self.__paxNum}
Cost per Pax: {self.__packageCostPerPax}
"""

class HotelDatabase:
    def __init__(self):
        """
        Constructor for the Hotel Database which will create an empty list and set the descending order flag to False
        """
        self.__db = []
        self.__descending_order = False

    def add_record(self, packageName, customerName, paxNum, packageCostPerPax):
        """
        Add a record to the database
        
        Requires 4 arguments for the record:
        1. Package Name (string)
        2. Customer Name (string)
        3. Number of Pax (int)
        4. Package Cost per Pax (int)
        """
        self.__db.append(RecordData(packageName, customerName, paxNum, packageCostPerPax))

    def search_for_package(self, packageName):
        """
        Do a binary search on the database for the package name
        """
        return self.binary_search(packageName.title())

    def search_for_customer(self, customerName):
        """
        Do a linear search on the database for the customer name
        """
        return self.linear_search(customerName.title())
    
    def sort_by_cost(self, descendingFlag = False):
        """
        Do a merge sort on the database by package cost per pax
        """
        self.__db = self.merge_sort(self.__db, descendingFlag)

    def empty(self):
        """
        Check if the database is empty and will return True if it is empty
        """
        return True if not self.__db else False

    def linear_search(self, customerName):
        """
        Do a linear search on the database for the customer name
        
        Best time complexity: O(1)
        Worst time complexity: O(n)
        Average time complexity: O(n)
        
        Space complexity: O(1)
        """
        for record in self.__db:
            if (record.get_customer_name() == customerName):
                return record
        return -1

    def binary_search(self, packageName):
        """
        Do a binary search on the database for the package name
        
        Best time complexity: O(1)
        Worst time complexity: O(log(n))
        Average time complexity: O(log(n))
        
        Space complexity: O(1)
        """
        l = 0
        r = len(self.__db) - 1
        while (l <= r):
            mid = (l + r) // 2
            
            # return mid if the package name is found in the subarray
            if (self.__db[mid].get_package_name() == packageName):
                return self.__db[mid]

            if (not self.__descending_order):
                # if the package name to find is greater than mid, search the right half
                if (self.__db[mid].get_package_name() < packageName):
                    l = mid + 1
                # if the package name to find is smaller than mid, search the left half
                else:
                    r = mid - 1
            else:
                # if the package name to find is smaller than mid, search the right half
                if (self.__db[mid].get_package_name() > packageName):
                    l = mid + 1
                # if the package name to find is greater than mid, search the left half
                else:
                    r = mid - 1

        return -1 # return -1 if the package name is not found

    def bubble_sort(self, descendingFlag = False):
        """
        Do a bubble sort on the database by customer name
        
        Best time complexity: O(n)
        Worst time complexity: O(n^2)
        Average time complexity: O(n^2)
        
        Space complexity: O(1)
        """
        self.__descending_order = descendingFlag
        flag = 0
        for i in range(len(self.__db)):
            for j in range(len(self.__db) - 1):
                if (descendingFlag):
                    # swap the elements if the jth customer name is smaller than the next customer name
                    if (self.__db[j].get_customer_name() < self.__db[j + 1].get_customer_name()):
                        self.__db[j], self.__db[j + 1] = self.__db[j + 1], self.__db[j]
                        flag = 1
                else:
                    # swap the elements if the jth customer name is greater than the next customer name
                    if (self.__db[j].get_customer_name() > self.__db[j + 1].get_customer_name()):
                        self.__db[j], self.__db[j + 1] = self.__db[j + 1], self.__db[j]
                        flag = 1

            if (not flag):
                break # break when the array is already sorted

    def selection_sort(self, descendingFlag = False):
        """
        Do a selection sort by package name
        
        Best time complexity: O(n^2)
        Worst time complexity: O(n^2)
        Average time complexity: O(n^2)
        
        Space complexity: O(1)
        """
        self.__descending_order = descendingFlag
        dbSize = len(self.__db)
        for i in range(dbSize):
            # initialise the element at ith index and assume that it is the smallest/biggest element based on the descendingFlag
            index = i

            for j in range(i + 1, dbSize):
                if (descendingFlag):
                    # find the next biggest element to compare with index
                    if (self.__db[j].get_package_name() > self.__db[index].get_package_name()):
                        index = j
                else:
                    # find the next smallest element to compare with index
                    if (self.__db[j].get_package_name() < self.__db[index].get_package_name()):
                        index = j

            if (index != i):
                # swap the found minimum/maximum element with the element at index i if the smallest/biggest elemment is not in its proper position
                self.__db[i], self.__db[index] = self.__db[index], self.__db[i]

    def insertion_sort(self, descendingFlag = False):
        """
        Do a insertion sort by package cost
        
        Best time complexity: O(n)
        Worst time complexity: O(n^2)
        Average time complexity: O(n^2)
        
        Space complexity: O(1)
        """
        self.__descending_order = descendingFlag
        dbSize = len(self.__db)
        for i in range(1, dbSize):
            el = self.__db[i] # save the value to be positioned
            
            j = i - 1
            if (descendingFlag):
                # Compare el with each element on the left of it and move the smaller element to the right ahead of their current position
                while (j >= 0 and self.__db[j].get_package_cost_per_pax() < el.get_package_cost_per_pax()):
                    self.__db[j + 1] = self.__db[j]
                    j -= 1
            else:
                # Compare el with each element on the left of it and move the bigger element to the right ahead of their current position
                while (j >= 0 and self.__db[j].get_package_cost_per_pax() > el.get_package_cost_per_pax()):
                    self.__db[j + 1] = self.__db[j ]
                    j -= 1

            self.__db[j + 1] = el

    def heapify(self, n, i, descendingFlag): 
        """
        To heapify subtree rooted at index i. 
        """
        l = (2 * i) + 1
        r = (2 * i) + 2

        if (descendingFlag):
            smallest = i  # Initialise smallest as root

            # if left child of root exists and is smaller than root 
            if (l < n and self.__db[l].get_package_name() < self.__db[smallest].get_package_name()): 
                smallest = l 

            # if right child of root exists and is smaller than smallest 
            if (r < n and self.__db[r].get_package_name() < self.__db[smallest].get_package_name()): 
                smallest = r
            
            # Change root if smallest is not root
            if (smallest != i): 
                self.__db[i], self.__db[smallest] = self.__db[smallest], self.__db[i] 
                
                # recursively heapify the root.
                self.heapify(n, smallest, descendingFlag)
        else:
            largest = i   # Initialise largest as root 

            # See if left child of root exists and is greater than root 
            if (l < n and self.__db[largest].get_package_name() < self.__db[l].get_package_name()): 
                largest = l 
        
            # See if right child of root exists and is greater than largest 
            if (r < n and self.__db[largest].get_package_name() < self.__db[r].get_package_name()): 
                largest = r 
        
            # Change root if largest is not root
            if (largest != i): 
                self.__db[i], self.__db[largest] = self.__db[largest],self.__db[i]
        
                # recursively heapify the root.
                self.heapify(n, largest, descendingFlag) 

    def heap_sort(self, descendingFlag = False):
        """
        Do a heap sort on the database by package name
        
        Best time complexity: O(n log(n))
        Worst time complexity: O(n log(n))
        Average time complexity: O(n log(n))
        
        Space complexity: O(1)
        """
        self.__descending_order = descendingFlag
        n = len(self.__db) 

        # Build a heap
        for i in range((n // 2) - 1, -1, -1): 
            self.heapify(n, i, descendingFlag) 

        # extract elements individually starting from the end
        for i in range(n - 1, -1, -1): 
            self.__db[i], self.__db[0] = self.__db[0], self.__db[i] # swap the first element with the last node from the heap
            self.heapify(i, 0, descendingFlag) # call heapify on the reduced list

    def merge(self, leftArr, rightArr, descendingFlag):
        """
        Merge two sub-arrays
        """
        if (descendingFlag):
            leftArr = leftArr[::-1]
            rightArr = rightArr[::-1]

        newArr = []
        i = j = 0
        leftArrSize = len(leftArr)
        rightArrSize = len(rightArr)
        while (i < leftArrSize and j < rightArrSize):
            if (descendingFlag):
                if (leftArr[i].get_package_cost_per_pax() > rightArr[j].get_package_cost_per_pax()):
                    newArr.append(leftArr[i])
                    i += 1
                else:
                    newArr.append(rightArr[j])
                    j += 1
            else:
                if (leftArr[i].get_package_cost_per_pax() < rightArr[j].get_package_cost_per_pax()):
                    newArr.append(leftArr[i])
                    i += 1
                else:
                    newArr.append(rightArr[j])
                    j += 1

        while (i < leftArrSize):
            newArr.append(leftArr[i])
            i += 1

        while (j < rightArrSize):
            newArr.append(rightArr[j])
            j += 1

        return newArr

    def merge_sort(self, arr, descendingFlag = False):
        """
        Do a merge sort on the database by cost per pax
        
        Best time complexity: O(n log(n))
        Worst time complexity: O(n log(n))
        Average time complexity: O(n log(n))
        
        Space complexity: O(n)
        """
        arrLen = len(arr)
        if (arrLen <= 1): 
            return arr # return if the array has only one element
        
        self.__descending_order = descendingFlag
        
        mid = arrLen // 2
        leftHalf = self.merge_sort(arr[:mid])
        rightHalf = self.merge_sort(arr[mid:])
        
        newArr = self.merge(leftHalf, rightHalf, descendingFlag)
        return newArr

    def counting_sort(self, place):
        """
        Counting sort for radix sort
        
        Best time complexity: O(n+k)
        Worst time complexity: O(n+k)
        Average time complexity: O(n+k)
        
        Space complexity: O(n+k)
        Where n is the number of elements and k is the range of the elements in the array
        """
        n = len(self.__db)
        outputArr = [0] * n
        countArr = [0] * 10

        # Calculate count of elements
        for i in range(0, n):
            index = (self.__db[i].get_package_cost_per_pax() * 100) // place
            countArr[index % 10] += 1

        # Calculate cumulative count
        for i in range(1, 10):
            countArr[i] += countArr[i - 1]

        # Place the elements in sorted order
        i = n - 1
        while i >= 0:
            index = (self.__db[i].get_package_cost_per_pax() * 100) // place
            outputArr[countArr[index % 10] - 1] = self.__db[i]
            countArr[index % 10] -= 1
            i -= 1

        for i in range(0, n):
            self.__db[i] = outputArr[i]
    
    def radix_sort(self, descendingFlag = False):
        """
        Do a radix sort on the database by cost per pax
        
        Best time complexity: O(nk)
        Worst time complexity: O(nk)
        Average time complexity: O(nk)
        
        Space complexity: O(n+k)
        Where n is the number of keys and k is the range of keys
        """
        # Find the maximum number to know number of digits
        maxCost = max(self.__db, key=lambda x: x.get_package_cost_per_pax()).get_package_cost_per_pax() * 100

        # Do counting sort for every digit. Note that instead of passing digit number, place is passed. 
        # place is 10^i where i is current digit number
        place = 1
        while (maxCost // place > 0):
            self.counting_sort(place)
            place *= 10
            
        if (descendingFlag):
            self.__db = self.__db[::-1]

    def __str__(self):
        for record in self.__db:
            print(record)
        return ""

h = HotelDatabase()
for i in range(25):
    h.add_record(f"Package {i}", f"Customer {i}", i, i)

h.add_record(f"Deluxe package", f"J", 1, 1000)
h.add_record(f"Deluxe package", f"Xed", 1, 10000)
h.add_record(f"Deluxe package", f"Apples", 1, 100000)
h.radixSort()
print(h)