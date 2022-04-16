import functions

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

class HotelDatabase:
    def __init__(self):
        """
        Constructor for the Hotel Database which will create an empty list and set the descending order flag to False
        """
        self.__db = []
        self.__descending_order = False
        self.__sort_order = "Not Sorted"

        customerNameHeaderOffset = len("Customer Name")
        packageNameHeaderOffset = len("Package Name")
        paxNumHeaderOffset = len("Number of Pax")
        packageCostPerPaxHeaderOffset = len("Cost Per Pax")
        self.__table_len = [customerNameHeaderOffset, packageNameHeaderOffset, paxNumHeaderOffset, packageCostPerPaxHeaderOffset]

    def get_record(self, index):
        """
        Return the record at the specified index
        
        Requires 1 argument:
        - index (int)
        """
        try:
            return self.__db[index]
        except IndexError:
            return -1

    def add_record(self, packageName, customerName, paxNum, packageCostPerPax):
        """
        Add a record to the database
        
        Requires 4 arguments for the record:
        1. Package Name (string)
        2. Customer Name (string)
        3. Number of Pax (int)
        4. Package Cost per Pax (int)
        """
        packageCostPerPax = float(packageCostPerPax)
        formattedPackageCostPerPax = "${:.2f}".format(round(packageCostPerPax, 2))
        if (len(customerName) > self.__table_len[0]):
            self.__table_len[0] = len(customerName)
        if (len(packageName) > self.__table_len[1]):
            self.__table_len[1] = len(packageName)
        if (len(formattedPackageCostPerPax) > self.__table_len[2]):
            self.__table_len[2] = len(formattedPackageCostPerPax)
        if (len(str(paxNum)) > self.__table_len[3]):
            self.__table_len[3] = len(str(paxNum))

        self.__db.append(RecordData(packageName, customerName, paxNum, packageCostPerPax))

    def search_for_package(self, packageName):
        """
        Do a binary search on the database for the package name
        """
        if (self.__sort_order != "Package Name"):
            alertMsg = (
                "Note: In order to search for a package, you must first sort the database by package name for a faster search time...",
                "Otherwise, you can still search for a package without sorting the database by the package name but with the cost of a longer searching time"
            )
            sortInput = functions.get_input(prompt="Do you want to sort the database by package name? (Y/N): ", prints=alertMsg, command=("y", "n"))
            if (sortInput == "y"): 
                reverseOrder = functions.get_input(prompt="Do you want to sort the database in descending order? (Y/N): ", command=("y", "n"))
                if (reverseOrder == "y"):
                    self.heap_sort(1)
                else:
                    self.heap_sort()

                return self.binary_search(packageName.title())
            else:
                return self.linear_search(packageName.title(), "package")

    def search_for_customer(self, customerName):
        """
        Do a linear search on the database for the customer name
        """
        return self.linear_search(customerName.title(), "customer")
    
    def search_for_range_of_cost(self, low, high):
        """
        Do a search on the database for the range of cost specified by the user.
        
        Requires 2 arguments:
        - low (int)
        - high (int)
        """
        if (self.__sort_order != "Package Cost Per Pax"):
            alertMsg = (
                "Note: In order to search for a range of cost, you must first sort the database by package cost per pax for a faster search time...",
                "Otherwise, you can still search for a range of cost without sorting the database by the package cost per pax but with the cost of a longer searching time"
            )
            sortInput = functions.get_input(prompt="Do you want to sort the database by package cost per pax? (Y/N): ", prints=alertMsg, command=("y", "n"))
            if (sortInput == "y"):
                reverseOrder = functions.get_input(prompt="Do you want to sort the database in descending order? (Y/N): ", command=("y", "n"))
                if (reverseOrder == "y"):
                    self.__db = self.merge_sort(self.__db, 1)
                    self.__descending_order = 1
                else:
                    self.__db = self.merge_sort(self.__db)
                    self.__descending_order = 0

                self.__sort_order = "Cost Per Pax"
                indexOne, indexTwo = self.binary_search(low, high)
                self.print_from_index(indexOne, indexTwo)
            else:
                self.print_from_array(self.linear_search_range_of_cost(low, high))

    def lowerIndex(self, i, lowerRange):
        """
        Search for any records within the lowerRange of the cost specified by the user starting from the index found from the search
        
        Best time complexity: O(n)
        Worst time complexity: O(n)
        Average time complexity: O(n)
        
        Space complexity: O(1)
        """
        while (i > 0 and self.__db[i - 1].get_package_cost_per_pax() >= lowerRange):
            i -= 1
        return i

    def upperIndex(self, i, upperRange):
        """
        Search for any records within the upperRange of the cost specified by the user starting from the index found from the search
        
        Best time complexity: O(n)
        Worst time complexity: O(n)
        Average time complexity: O(n)
        
        Space complexity: O(1)
        """
        while (i < len(self.__db) - 1 and self.__db[i + 1].get_package_cost_per_pax() <= upperRange):
            i += 1
        return i

    def empty(self):
        """
        Check if the database is empty and will return True if it is empty
        """
        return True if not self.__db else False

    def linear_search_range_of_cost(self, low, high):
        """
        Do a linear search on the database for the range of cost specified by the user.
        
        Requires 2 arguments:
        - low (int)
        - high (int)
        
        Best time complexity: O(1)
        Worst time complexity: O(n)
        Average time complexity: O(n)
        
        Space complexity: O(1)
        """
        arr = []
        for record in self.__db:
            if (record.get_package_cost_per_pax() >= low and record.get_package_cost_per_pax() <= high):
                arr.append(record)
        return arr

    def linear_search(self, target, typeOfSearch):
        """
        Do a linear search on the database for the customer name
        
        Requires 2 arguments:
        - target (string)
        - typeOfSearch (string)
        
        Best time complexity: O(1)
        Worst time complexity: O(n)
        Average time complexity: O(n)
        
        Space complexity: O(1)
        """
        for record in self.__db:
            if (typeOfSearch == "customer" and record.get_customer_name() == target):
                return record
            elif (typeOfSearch == "package" and record.get_package_name() == target):
                return record
        return -1

    def binary_search(self, packageName):
        """
        Do a binary search on the database for the package name
        
        Requires 1 argument:
        - packageName (string)
        
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
        
        Optional argument:
        - descendingFlag (bool)
        
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

        self.__sort_order = "Customer Name"

    def selection_sort(self, descendingFlag = False):
        """
        Do a selection sort by package name
        
        Optional argument:
        - descendingFlag (bool)
        
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

        self.__sort_order = "Package Name"

    def insertion_sort(self, descendingFlag = False):
        """
        Do a insertion sort by package cost
        
        Optional argument:
        - descendingFlag (bool)
        
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

        self.__sort_order = "Package Cost"

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
        
        Optional argument:
        - descendingFlag (bool)
        
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
        
        self.__sort_order = "Package Name"

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
        
        Requires 1 argument:
        - arr (list)
        
        Best time complexity: O(n log(n))
        Worst time complexity: O(n log(n))
        Average time complexity: O(n log(n))
        
        Space complexity: O(n)
        """
        arrLen = len(arr)
        if (arrLen <= 1): 
            return arr # return if the array has only one element

        mid = arrLen // 2
        leftHalf = self.merge_sort(arr[:mid])
        rightHalf = self.merge_sort(arr[mid:])
        
        newArr = self.merge(leftHalf, rightHalf, descendingFlag)
        return newArr

    def counting_sort(self, place):
        """
        Counting sort for radix sort
        
        Requires 1 argument:
        - place (int)
        
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
            index = self.__db[i].get_pax_num() // place
            countArr[index % 10] += 1

        # Calculate cumulative count
        for i in range(1, 10):
            countArr[i] += countArr[i - 1]

        # Place the elements in sorted order
        i = n - 1
        while i >= 0:
            index = self.__db[i].get_pax_num() // place
            outputArr[countArr[index % 10] - 1] = self.__db[i]
            countArr[index % 10] -= 1
            i -= 1

        for i in range(0, n):
            self.__db[i] = outputArr[i]

    def radix_sort(self, descendingFlag = False):
        """
        Do a radix sort on the database by number of pax

        Optional argument:
        - descendingFlag (bool)
        
        Best time complexity: O(nk)
        Worst time complexity: O(nk)
        Average time complexity: O(nk)
        
        Space complexity: O(n+k)
        Where n is the number of keys and k is the range of keys
        """
        # Find the maximum number to know number of digits
        maxCost = max(self.__db, key=lambda x: x.get_pax_num()).get_pax_num()

        # Do counting sort for every digit. Note that instead of passing digit number, place is passed. 
        # place is 10^i where i is current digit number
        place = 1
        while (maxCost // place > 0):
            self.counting_sort(place)
            place *= 10
            
        if (descendingFlag):
            self.__db = self.__db[::-1]

        self.__sort_order = "Number of Pax"

    def print_from_array(self, recordArr):
        header = f"| {'Customer Name'.ljust(self.__table_len[0])} | {'Package Name'.ljust(self.__table_len[1])} | {'Cost Per Pax'.ljust(self.__table_len[2])} | {'Number of Pax'.ljust(self.__table_len[3])} |"

        print("-" * len(header))
        print(header)
        print("-" * len(header))

        for record in recordArr:
            print(f"| {record.get_customer_name().ljust(self.__table_len[0])}", end=" | ")
            print(f"{record.get_package_name().ljust(self.__table_len[1])}", end=" | ")
            print(f"${round(record.get_package_cost_per_pax(), 2):.2f}".ljust(self.__table_len[2]), end=" | ")
            print(f"{str(record.get_pax_num()).ljust(self.__table_len[3])}  |")

        print("-" * len(header))

    def print_from_index(self, startIndex, endIndex):
        header = f"| {'Customer Name'.ljust(self.__table_len[0])} | {'Package Name'.ljust(self.__table_len[1])} | {'Cost Per Pax'.ljust(self.__table_len[2])} | {'Number of Pax'.ljust(self.__table_len[3])} |"

        print("-" * len(header))
        print(header)
        print("-" * len(header))

        if (not self.__descending_order):
            for i in range(startIndex, endIndex + 1):
                print(f"| {self.__db[i].get_customer_name().ljust(self.__table_len[0])}", end=" | ")
                print(f"{self.__db[i].get_package_name().ljust(self.__table_len[1])}", end=" | ")
                print(f"${round(self.__db[i].get_package_cost_per_pax(), 2):.2f}".ljust(self.__table_len[2]), end=" | ")
                print(f"{str(self.__db[i].get_pax_num()).ljust(self.__table_len[3])}  |")
        else:
            for i in range(endIndex, startIndex - 1, -1):
                print(f"| {self.__db[i].get_customer_name().ljust(self.__table_len[0])}", end=" | ")
                print(f"{self.__db[i].get_package_name().ljust(self.__table_len[1])}", end=" | ")
                print(f"${round(self.__db[i].get_package_cost_per_pax(), 2):.2f}".ljust(self.__table_len[2]), end=" | ")
                print(f"{str(self.__db[i].get_pax_num()).ljust(self.__table_len[3])}  |")
        print("-" * len(header))

    def __str__(self):
        header = f"| {'Customer Name'.ljust(self.__table_len[0])} | {'Package Name'.ljust(self.__table_len[1])} | {'Cost Per Pax'.ljust(self.__table_len[2])} | {'Number of Pax'.ljust(self.__table_len[3])} |"

        print("-" * len(header))
        print(header)
        print("-" * len(header))

        counter = 0
        rowsToPrint = 10
        while (counter < len(self.__db)):
            
            for i in range(counter, counter + rowsToPrint):
                record = self.__db[i]
                print(f"| {record.get_customer_name().ljust(self.__table_len[0])}", end=" | ")
                print(f"{record.get_package_name().ljust(self.__table_len[1])}", end=" | ")
                print(f"${round(record.get_package_cost_per_pax(), 2):.2f}".ljust(self.__table_len[2]), end=" | ")
                print(f"{str(record.get_pax_num()).ljust(self.__table_len[3])}  |")

                counter += 1
                if (counter >= len(self.__db)):
                    break

            print("-" * len(header))
            
            if (counter < len(self.__db)):
                continuePrompt = functions.get_input(prompt="Press enter to continue or type 'q' to exit: ", command=("", "q"))
                
                if (continuePrompt == "q"): break
                else:
                    for i in range(rowsToPrint + 2):
                        print("\033[1A\x1b[2K", end="") # move up cursor and delete whole line
                        # this may not work in some versions of Windows but running it in powershell will likely works fine
            else:
                print("End of database...")
        return ""

h = HotelDatabase()
from random import randint
for i in range(205):
    h.add_record(f"Package {i}", f"Customer {i}", randint(1, 5), randint(60, 10000))

h.search_for_range_of_cost(0, 10000)