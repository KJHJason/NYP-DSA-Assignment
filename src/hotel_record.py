# import third party libraries
from colorama import Fore as F

# import standard library
import math

# import local python files
from functions import get_input, S_reset, format_price, print_record_data
from tree_code import BinarySearchTree

class RecordData:
    def __init__(self, packageName, customerName, paxNum, packageCostPerPax):
        self.__packageName = packageName.title()
        self.__customerName = customerName.title()
        self.__paxNum = int(paxNum)
        self.__packageCostPerPax = round(float(packageCostPerPax), 2)

    def set_package_name(self, packageName):
        self.__packageName = packageName.title()
    def update_package_name(self):
        while (1):
            print()
            print(f"Current package name: {self.__packageName}")
            newPackageName = input("Enter a new package name (x to cancel): ").strip().lower()
            if (newPackageName == ""):
                print(f"{F.LIGHTRED_EX}Package name cannot be empty!")
                S_reset()
            elif (newPackageName == "x"):
                return
            else:
                confirmInput = get_input(prompt=f"Are you sure you want to change the package name to \"{newPackageName}\"? (Y/N): ", command=("y", "n"))
                if (confirmInput == "y"):
                    self.__packageName = newPackageName.title()
                    return
    def get_package_name(self):
        return self.__packageName

    def set_customer_name(self, customerName):
        self.__customerName = customerName.title()
    def update_customer_name(self):
        while (1):
            print()
            print(f"Current customer name: {self.__customerName}")
            newCustomerName = input("Enter a new customer name (x to cancel): ").strip().lower()
            if (newCustomerName == ""):
                print(f"{F.LIGHTRED_EX}Customer name cannot be empty!")
                S_reset()
            elif (newCustomerName == "x"):
                return
            else:
                confirmInput = get_input(prompt=f"Are you sure you want to change the customer name to \"{newCustomerName}\"? (Y/N): ", command=("y", "n"))
                if (confirmInput == "y"):
                    self.__customerName = newCustomerName.title()
                    return
    def get_customer_name(self):
        return self.__customerName

    def set_pax_num(self, paxNum):
        self.__paxNum = int(paxNum)
    def update_pax_num(self):
        while (1):
            print()
            print(f"Current number of pax: {self.__paxNum}")
            newPaxNum = input("Enter a new number of pax (x to cancel): ").strip().lower()
            if (newPaxNum == ""):
                print(f"{F.LIGHTRED_EX}Number of pax cannot be empty!")
                S_reset()
            elif (newPaxNum == "x"):
                return
            else:
                try:
                    newPaxNum = int(newPaxNum)
                    confirmInput = get_input(prompt=f"Are you sure you want to change the number of pax to \"{newPaxNum}\"? (Y/N): ", command=("y", "n"))
                    if (confirmInput == "y"):
                        self.__paxNum = newPaxNum
                        return
                except ValueError:
                    print(f"{F.LIGHTRED_EX}Number of pax must be an number!")
                    S_reset()
    def get_pax_num(self):
        return self.__paxNum

    def set_package_cost_per_pax(self, packageCostPerPax):
        self.__packageCostPerPax = round(float(packageCostPerPax), 2)
    def update_package_cost_per_pax(self):
        while (1):
            print()
            print(f"Current package cost per pax: {format_price(self.__packageCostPerPax)}")
            newPackageCostPerPax = input("Enter a new package cost per pax (x to cancel): $").strip().lower()
            if (newPackageCostPerPax == ""):
                print(f"{F.LIGHTRED_EX}Package cost per pax cannot be empty!")
                S_reset()
            elif (newPackageCostPerPax == "x"):
                return
            else:
                try:
                    newPackageCostPerPax = round(float(newPackageCostPerPax), 2)
                    confirmInput = get_input(prompt=f"Are you sure you want to change the package cost per pax to \"{format_price(newPackageCostPerPax)}\"? (Y/N): ", command=("y", "n"))
                    if (confirmInput == "y"):
                        self.__packageCostPerPax = newPackageCostPerPax
                        return
                except ValueError:
                    print(f"{F.LIGHTRED_EX}Package cost per pax must be a valid price!")
                    S_reset()
    def get_package_cost_per_pax(self):
        return self.__packageCostPerPax

    def __str__(self):
        return print_record_data(self.__packageName, self.__customerName, self.__paxNum, self.__packageCostPerPax)

class HotelDatabase:
    def __init__(self):
        """
        Constructor for the Hotel Database which will create an empty array and set the descending order flag to False
        """
        self.__db = []
        self.__bst_root = BinarySearchTree() # create a binary search tree based on customer names as the keys
        self.__descending_order = False
        self.__sort_order = "Not Sorted"
        self.__table_headers = ["Customer Name", "Package Name", "Cost per Pax", "Number of Pax"]
        self.__table_len = [len(self.__table_headers[0]), len(self.__table_headers[1]), len(self.__table_headers[2]), len(self.__table_headers[3])]

    def delete_record(self, record):
        """
        Deletes a record from the database
        
        Args:
        record: The record to be deleted
        """
        self.__db.remove(record)
        print(f"{F.LIGHTGREEN_EX}Record deleted!")
        S_reset()

    def add_record(self, packageName, customerName, paxNum, packageCostPerPax):
        """
        Add a record to the database
        
        Requires 4 arguments for the record:
        1. Package Name (string)
        2. Customer Name (string)
        3. Number of Pax (int)
        4. Package Cost per Pax (int)
        """
        if (len(customerName) > self.__table_len[0]):
            self.__table_len[0] = len(customerName)

        if (len(packageName) > self.__table_len[1]):
            self.__table_len[1] = len(packageName)

        formattedPackageCostPerPax = format_price(packageCostPerPax)
        if (len(formattedPackageCostPerPax) > self.__table_len[2]):
            self.__table_len[2] = len(formattedPackageCostPerPax)

        if (len(str(int(paxNum))) > self.__table_len[3]):
            self.__table_len[3] = len(str(int(paxNum)))

        self.__sort_order = "Not Sorted"
        recordData = RecordData(packageName, customerName, paxNum, packageCostPerPax)
        self.__db.append(recordData)
        self.__bst_root.insert(recordData)

    def edit_record(self, record):
        """
        Edit a record's data
        
        Requires 1 argument:
        - record (RecordData)
        """
        header = "Select the field you want to edit:"
        menu = f"""{'-' * len(header)}
{header}
1. Package Name
2. Customer Name
3. Number of Pax
4. Package Cost per Pax
5. Display Record Data
A. All Fields
X. Exit
{'-' * len(header)}"""
        while (1):
            whichToEdit = get_input(prompt="Which field do you want to edit?: ", command=("1", "2", "3", "4", "5", "a", "x"), prints=menu)
            if (whichToEdit == "1"):
                record.update_package_name()
            elif (whichToEdit == "2"):
                record.update_customer_name()
            elif (whichToEdit == "3"):
                record.update_pax_num()
            elif (whichToEdit == "4"):
                record.update_package_cost_per_pax()
            elif (whichToEdit == "5"):
                print(record, end="")
            elif (whichToEdit == "a"):
                record.update_package_name()
                print()
                record.update_customer_name()
                print()
                record.update_pax_num()
                print()
                record.update_package_cost_per_pax()
            elif (whichToEdit == "x"):
                break
            else:
                print(f"{F.LIGHTRED_EX}Invalid input...")
                S_reset()

    def sort_by_pax_num(self, reverse=False):
        """
        Do a 3 way quicksort on the database by number of pax
        
        Optional parameter:
        - reverse (bool)
        """
        if (len(self.__db) > 1):
            if (isinstance(reverse, str)):
                if (reverse == "y"): 
                    reverse = 1
                else:
                    reverse = 0
            self.__descending_order = reverse
            self.three_way_quicksort(0, len(self.__db) - 1, reverse=reverse)
            self.__sort_order = "Number of Pax"
            print(f"{F.LIGHTGREEN_EX}The database has been sorted by the package's number of pax!")
        elif (len(self.__db) == 1):
            print(f"{F.LIGHTRED_EX}Warning: There is no need to sort the database as there is only one record!")
        else:
            print(f"{F.LIGHTRED_EX}Warning: There are no records to sort!")
        S_reset()

    def sort_by_customer_name(self, reverse=False):
        """
        Do a bubble sort on the database by customer name to satisfy the basic function c.2. criteria
        
        Optional parameter:
        - reverse (bool)
        """
        if (len(self.__db) > 1):
            if (isinstance(reverse, str)):
                if (reverse == "y"): 
                    reverse = 1
                else:
                    reverse = 0
            self.bubble_sort(reverse=reverse)
            self.__sort_order = "Customer Name"
            print(f"{F.LIGHTGREEN_EX}The database has been sorted by customer name!")
        elif (len(self.__db) == 1):
            print(f"{F.LIGHTRED_EX}Warning: There is no need to sort the database as there is only one record!")
        else:
            print(f"{F.LIGHTRED_EX}Warning: There are no records to sort!")
        S_reset()

    def sort_by_package_name(self, reverse=False):
        """
        Do a selection sort on the database by package name to satisfy the basic function c.3. criteria
        
        Optional parameter:
        - reverse (bool)
        """
        if (len(self.__db) > 1):
            if (isinstance(reverse, str)):
                if (reverse == "y"): 
                    reverse = 1
                else:
                    reverse = 0
            self.selection_sort(reverse=reverse)
            self.__sort_order = "Package Name"
            print(f"{F.LIGHTGREEN_EX}The database has been sorted by package name!")
        elif (len(self.__db) == 1):
            print(f"{F.LIGHTRED_EX}Warning: There is no need to sort the database as there is only one record!")
        else:
            print(f"{F.LIGHTRED_EX}Warning: There are no records to sort!")
        S_reset()

    def sort_by_package_cost(self, reverse=False):
        """
        Do a insertion sort on the database by package cost to satisfy the basic function c.4. criteria
        
        Optional parameter:
        - reverse (bool)
        """
        if (len(self.__db) > 1):
            if (isinstance(reverse, str)):
                if (reverse == "y"): 
                    reverse = 1
                else:
                    reverse = 0
            self.insertion_sort(reverse=reverse)
            self.__sort_order = "Cost Per Pax"
            print(f"{F.LIGHTGREEN_EX}The database has been sorted by customer name!")
        elif (len(self.__db) == 1):
            print(f"{F.LIGHTRED_EX}Warning: There is no need to sort the database as there is only one record!")
        else:
            print(f"{F.LIGHTRED_EX}Warning: There are no records to sort!")
        S_reset()

    def search_for_customer(self, customerName, mode="Edit"):
        """
        Do a linear search on the database for the customer name to satisfy the basic function c.5. criteria
        
        Requires 1 argument:
        - customerName (string)
        - mode (string): "Edit" or "Display" or "Delete", defaults to "Edit"
        """
        mode = mode.title()
        customerName = customerName.title()

        if (mode == "Display"):
            dataList = self.__bst_root.search(customerName)
            if (dataList != -1):
                self.print_from_array(dataList.convert_to_array())
                return
            else:
                print(f"{F.LIGHTRED_EX}No records found with the customer name, {customerName}!")
                S_reset(nl=1)
                return -1

        data = self.linear_search(customerName, "customer")
        if (data == -1):
            print(f"{F.LIGHTRED_EX}Customer \"{customerName}\" not found!")
            S_reset()
            return

        print(data)
        editInput = get_input(prompt=f"Do you want to {mode.lower()} the record? (Y/N): ", command=("y", "n"))
        if (editInput == "y" and mode == "Edit"):
            self.edit_record(data)
        elif (editInput == "y" and mode == "Delete"):
            self.delete_record(data)
            self.__bst_root.delete(data, deleteAll=False)

    def search_for_package(self, packageName, mode="Edit"):
        """
        Do a binary search on the database for the package name to satisfy the basic function c.6. criteria
        
        Note: Depending on the user's preference, the package name can be searched using linear search algorithm if the user wish to perserve the order of the database.
        
        Requires 1 argument:
        - packageName (string)
        """
        packageName = packageName.title()
        if (self.__sort_order != "Package Name" and len(self.__db) > 1):
            alertMsg = (
                "Note: You can first sort the database by package name for a faster search time in future searches...",
                "Otherwise, you can still search for a package and maintain the original order of the database..."
            )
            sortInput = get_input(prompt="Do you want to sort the database by package name? (Y/N): ", prints=alertMsg, command=("y", "n"))
            if (sortInput == "y"): 
                reverseOrder = get_input(prompt="Do you want to sort the database in descending order? (Y/N): ", command=("y", "n"))
                if (reverseOrder == "y"):
                    self.heap_sort(reverse=1)
                else:
                    self.heap_sort()
                
                self.__sort_order = "Package Name"

                return self.search_for_package(packageName, mode=mode)
            else:
                record = self.linear_search(packageName, "package")
                if (record == -1):
                    print(f"{F.LIGHTRED_EX}Package \"{packageName}\" not found!")
                    S_reset()
                else:
                    print(record)
                    userInput = get_input(prompt=f"Do you want to {mode.lower()} the record? (Y/N): ", command=("y", "n"))
                    if (userInput == "y" and mode == "Edit"):
                        self.edit_record(record)
                    elif (userInput == "y" and mode == "Delete"):
                        self.delete_record(record)
        else:
            record = self.binary_search_for_package_name(packageName)
            if (record == -1):
                print(f"{F.LIGHTRED_EX}Package \"{packageName}\" not found!")
                S_reset()
            else:
                print(record)
                userInput = get_input(prompt=f"Do you want to {mode.lower()} the record? (Y/N): ", command=("y", "n"))
                if (userInput == "y" and mode == "Edit"):
                    self.edit_record(record)
                elif (userInput == "y" and mode == "Delete"):
                    self.delete_record(record)

    def search_for_range_of_cost(self, low, high):
        """
        Do a binary search or a linear search on the database for the range of cost specified by the user to satisfy the basic function c.7. criteria
        
        Requires 2 arguments:
        - low (int)
        - high (int)
        """
        if (self.__sort_order != "Cost Per Pax" and len(self.__db) > 1):
            alertMsg = (
                "Note: You can first sort the database by package cost per pax for a faster search time in future searches...",
                "Otherwise, you can still search for packages that fits within the specified range of cost and maintain the original order of the database..."
            )
            sortInput = get_input(prompt="Do you want to sort the database by package cost per pax? (Y/N): ", prints=alertMsg, command=("y", "n"))
            if (sortInput == "y"):
                reverseOrder = get_input(prompt="Do you want to sort the database in descending order? (Y/N): ", command=("y", "n"))
                if (reverseOrder == "y"):
                    self.radix_sort(reverse=1)
                    self.__descending_order = 1
                else:
                    self.radix_sort()
                    self.__descending_order = 0

                self.__sort_order = "Cost Per Pax"
                return self.search_for_range_of_cost(low, high)
            else:
                arr = self.linear_search_range_of_cost(low, high)
                if (arr):
                    self.print_from_array(arr)
                else:
                    print(f"{F.LIGHTRED_EX}No packages found with a cost between {low} and {high}!")
                    S_reset()
        else:
            indexOne, indexTwo = self.binary_search_for_range_of_cost(low, high)
            if (indexOne == -1 and indexTwo == -1):
                print(f"{F.LIGHTRED_EX}No packages found with a cost between {low} and {high}!")
                S_reset()
            else:
                self.print_from_index(indexOne, indexTwo)

    def lowerIndex(self, i, lowerRange):
        """
        Search for any records within the lowerRange of the cost specified by the user starting from the index found from the search
        
        Requires 2 arguments:
        - i (int) <-- refers to the index obtained from a search algorithm
        - lowerRange (int)
        
        Best time complexity: O(n)
        Worst time complexity: O(n)
        Average time complexity: O(n)
        
        Space complexity: O(1)
        """
        if (not self.__descending_order):
            while (i > 0 and self.__db[i - 1].get_package_cost_per_pax() >= lowerRange):
                i -= 1
        else:
            while (i < len(self.__db) - 1 and self.__db[i + 1].get_package_cost_per_pax() >= lowerRange):
                i += 1
        return i

    def upperIndex(self, i, upperRange):
        """
        Search for any records within the upperRange of the cost specified by the user starting from the index found from the search
        
        Requires 2 arguments:
        - i (int) <-- refers to the index obtained from a search algorithm
        - upperRange (int)
        
        Best time complexity: O(n)
        Worst time complexity: O(n)
        Average time complexity: O(n)
        
        Space complexity: O(1)
        """
        if (not self.__descending_order):
            while (i < len(self.__db) - 1 and self.__db[i + 1].get_package_cost_per_pax() <= upperRange):
                i += 1
        else:
            while (i > 0 and self.__db[i - 1].get_package_cost_per_pax() <= upperRange):
                i -= 1
        return i

    def binary_search_for_range_of_cost(self, lowRange, highRange):
        """
        Do a binary search on the database for the package name
        
        Requires 2 arguments:
        - lowRange (int/float)
        - highRange (int/float)
        
        Best time complexity: O(1)
        Worst time complexity: O(log(n))
        Average time complexity: O(log(n))
        
        Space complexity: O(1)
        """
        l = 0
        r = len(self.__db) - 1
        while (l <= r):
            mid = (l + r) // 2
            
            # return mid if the range is found in the subarray
            if (self.__db[mid].get_package_cost_per_pax() >= lowRange and self.__db[mid].get_package_cost_per_pax() <= highRange):
                if (self.__descending_order):
                    return self.upperIndex(mid, highRange), self.lowerIndex(mid, lowRange)
                else:
                    return self.lowerIndex(mid, lowRange), self.upperIndex(mid, highRange)

            if (not self.__descending_order):
                # if the lower range to find is greater than mid, search the right half
                if (self.__db[mid].get_package_cost_per_pax() < lowRange):
                    l = mid + 1
                # if the upper range to find is less than mid, search the left half
                else:
                    r = mid - 1
            else:
                # if the upper range to find is greater than mid, search the right half
                if (self.__db[mid].get_package_cost_per_pax() > highRange):
                    l = mid + 1
                # if the lower range to find is less than mid, search the left half
                else:
                    r = mid - 1

        return -1, -1 # return -1 if the package name is not found

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
        - typeOfSearch (string) <-- "customer" or "package"
        
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

    def binary_search_for_package_name(self, packageName):
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

    def bubble_sort(self, reverse=False):
        """
        Do a bubble sort on the database by customer name
        
        Optional argument:
        - reverse (bool)
        
        Best time complexity: O(n)
        Worst time complexity: O(n^2)
        Average time complexity: O(n^2)
        
        Space complexity: O(1)
        """
        self.__descending_order = reverse
        for i in range(len(self.__db) - 1): # -1 to stop at last element since the last element will be the highest element after an iteration from the nested for loop
            swapFlag = 0
            for j in range(len(self.__db) - i - 1): # -i to stop at last i element since they are already sorted and -1 to account for the indexing starting from 0
                if (reverse):
                    # swap the elements if the jth customer name is smaller than the next customer name
                    if (self.__db[j].get_customer_name() < self.__db[j + 1].get_customer_name()):
                        self.__db[j], self.__db[j + 1] = self.__db[j + 1], self.__db[j]
                        swapFlag = 1
                else:
                    # swap the elements if the jth customer name is greater than the next customer name
                    if (self.__db[j].get_customer_name() > self.__db[j + 1].get_customer_name()):
                        self.__db[j], self.__db[j + 1] = self.__db[j + 1], self.__db[j]
                        swapFlag = 1

            if (not swapFlag):
                break # break when the array is already sorted

    def selection_sort(self, reverse=False):
        """
        Do a selection sort by package name
        
        Optional argument:
        - reverse (bool)
        
        Best time complexity: O(n^2)
        Worst time complexity: O(n^2)
        Average time complexity: O(n^2)
        
        Space complexity: O(1)
        """
        self.__descending_order = reverse
        dbSize = len(self.__db)
        for i in range(dbSize):
            # initialise the element at ith index and assume that it is the smallest/biggest element based on the reverse
            index = i

            for j in range(i + 1, dbSize):
                if (reverse):
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

    def insertion_sort(self, reverse=False):
        """
        Do a insertion sort by package cost
        
        Optional argument:
        - reverse (bool)
        
        Best time complexity: O(n)
        Worst time complexity: O(n^2)
        Average time complexity: O(n^2)
        
        Space complexity: O(1)
        """
        self.__descending_order = reverse
        dbSize = len(self.__db)
        for i in range(1, dbSize):
            el = self.__db[i] # save the value to be positioned
            
            j = i - 1
            if (reverse):
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

    def heapify(self, n, i, reverse): 
        """
        To heapify subtree rooted at index i. 
        
        Requires 3 arguments:
        - n (int) <-- the size of the array
        - i (int) <-- the index of the root of the subtree
        - reverse (bool)
        """
        l = (2 * i) + 1
        r = (2 * i) + 2

        if (reverse):
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
                self.heapify(n, smallest, reverse)
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
                self.heapify(n, largest, reverse) 

    def heap_sort(self, reverse=False):
        """
        Do a heap sort on the database by package name
        
        Optional argument:
        - reverse (bool)
        
        Best time complexity: O(n log(n))
        Worst time complexity: O(n log(n))
        Average time complexity: O(n log(n))
        
        Space complexity: O(1)
        """
        self.__descending_order = reverse
        n = len(self.__db) 

        # Build a heap
        for i in range((n // 2) - 1, -1, -1): 
            self.heapify(n, i, reverse) 

        # extract elements individually starting from the end
        for i in range(n - 1, -1, -1): 
            self.__db[i], self.__db[0] = self.__db[0], self.__db[i] # swap the first element with the last node from the heap
            self.heapify(i, 0, reverse) # call heapify on the reduced list

    def partition(self, low, high, reverse):
        """
        Partition the array into three parts using the "Dutch National Flag Algorithm"

        In an ascending order,
        - arr[low...i] contains all the elements smaller than the pivot
        - arr[i+1...j-1] contains all the elements equal to the pivot
        - arr[j...high] contains all the elements larger than the pivot

        In a descending order,
        - arr[low...i] contains all the elements larger than the pivot
        - arr[i+1...j-1] contains all the elements equal to the pivot
        - arr[j...high] contains all the elements smaller than the pivot
        
        Args:
        - low (int): The lower index of the array
        - high (int): The higher index of the array
        - reverse (bool): Whether the array is sorted in ascending or descending order.
        """
        arr = self.__db

        # if looking at two or less elements
        if (high - low <= 1):
            # swap the elements if in wrong order
            if (not reverse):
                if (arr[high].get_pax_num() < arr[low].get_pax_num()):
                    arr[high], arr[low] = arr[low], arr[high]
            else:
                if (arr[high].get_pax_num() > arr[low].get_pax_num()):
                    arr[high], arr[low] = arr[low], arr[high]

            return low, high # i, j pointers for the next recursive call

        # initialise mid pointer and pivot
        mid = low
        pivot = arr[high].get_pax_num()
        while (mid <= high):
            # if the element is smaller than the pivot, swap it the elements
            if (arr[mid].get_pax_num() < pivot):
                if (not reverse):
                    # Ascending order: swap the elements with the high pointer such that the smaller element is on the left
                    arr[mid], arr[low] = arr[low], arr[mid]
                    mid += 1
                    low += 1
                else:
                    # Descending order: swap the elements with the low pointer such that the smaller element is on the right
                    arr[mid], arr[high] = arr[high], arr[mid]
                    high -= 1

            # if there are values that are the same as the pivot
            elif (arr[mid].get_pax_num() == pivot):
                # increment the mid pointer to move to the next element
                mid += 1 

            # if the element is greater than the pivot, swap it with the element at the high pointer
            elif (arr[mid].get_pax_num() > pivot):
                if (not reverse):
                    # Ascending order: swap the elements with the low pointer such that the larger element is on the right
                    arr[mid], arr[high] = arr[high], arr[mid]
                    high -= 1
                else:
                    # Descending order: swap the elements with the high pointer such that the larger element is on the left
                    arr[mid], arr[low] = arr[low], arr[mid]
                    mid += 1
                    low += 1

        return low - 1, mid # i, j pointers for the next recursive call

    def three_way_quicksort(self, low, high, reverse=False):
        """
        3-way quicksort algorithm for sorting the database by pax number in ascending or descending order

        Advantages of 3way quicksort over the traditional quicksort algorithm is that it is able to sort the array quicker if there are many duplicate values
        which is ideal for pax number as hotels usually have between 1 to 9 pax per room.
        
        Time Complexities:
        - Best case: O(n(log(n)))
        - Worst case: O(n^2)
        - Average case: O(n(log(n)))
        
        Space Complexity:
        - O(1) in this function
        
        Args:
        - low (int): The lower index of the array
        - high (int): The higher index of the array
        - reverse (bool): Whether the array is sorted in ascending or descending order. Default to False.
        """
        if (low >= high): 
            return

        # partition the array
        i, j = self.partition(low, high, reverse)

        # sort the left half recursively
        self.three_way_quicksort(low, i, reverse)
        
        # sort the right half recursively
        self.three_way_quicksort(j, high, reverse)

    def counting_sort_for_radix_sort(self, place, reverse):
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
        for i in range(n):
            index = int(self.__db[i].get_package_cost_per_pax() * 100) // place
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

        # Place the elements in sorted order
        i = n - 1
        while (i >= 0):
            index = int(self.__db[i].get_package_cost_per_pax() * 100) // place
            outputArr[countArr[index % 10] - 1] = self.__db[i]
            countArr[index % 10] -= 1
            i -= 1

        # Copy the sorted elements into original array
        for i in range(n):
            self.__db[i] = outputArr[i]

    def radix_sort(self, reverse=False):
        """
        Do a radix sort on the database by cost per pax

        Optional argument:
        - reverse (bool)
        
        Best time complexity: O(nk)
        Worst time complexity: O(nk)
        Average time complexity: O(nk)
        
        Space complexity: O(n+k)
        Where n is the number of keys and k is the range of keys
        
        Note that I multiplied the cost per pax by 100 as it is a float with a possible decimal place of up to 2
        """
        # Find the maximum number to know number of digits
        maxCost = int(max(self.__db, key=lambda x: x.get_package_cost_per_pax()).get_package_cost_per_pax() * 100)

        # Do counting sort for every digit. Note that instead of passing digit number, place is passed. 
        # place is 10^i where i is current digit number
        place = 1
        while (maxCost // place > 0):
            self.counting_sort_for_radix_sort(place, reverse=reverse)
            place *= 10

    def print_from_array(self, arr):
        """
        Print records from the given array (to satisfy the basic function c.1. criteria)
        Pagination is an added feature of my own ;)
        
        Requires 1 argument:
        - arr (list)
        """
        print()
        if (len(arr) > 0):
            print("Numbers of results found:", len(arr))
            header = f"| {'Customer Name'.ljust(self.__table_len[0])} | {'Package Name'.ljust(self.__table_len[1])} | {'Cost Per Pax'.ljust(self.__table_len[2])} | {'Number of Pax'.ljust(self.__table_len[3])} |"

            counter = 0
            rowsToPrint = 10
            currentPage = 1
            maxPages = math.ceil(len(arr) / rowsToPrint)

            lastPageRecordsToPrint = len(arr) % rowsToPrint
            if (lastPageRecordsToPrint == 0):
                lastPageRecordsToPrint = rowsToPrint

            while (1):
                print("-" * len(header))
                print(header)
                print("-" * len(header))

                if (currentPage > maxPages):
                    currentPage = 1
                    counter = 0
                elif (currentPage < 1):
                    currentPage = maxPages
                    counter = 0

                if (currentPage != maxPages):
                    for i in range(counter, counter + rowsToPrint):
                        record = arr[i]
                        print(f"| {record.get_customer_name().ljust(self.__table_len[0])}", end=" | ")
                        print(f"{record.get_package_name().ljust(self.__table_len[1])}", end=" | ")
                        print(format_price(record.get_package_cost_per_pax()).ljust(self.__table_len[2]), end=" | ")
                        print(f"{str(record.get_pax_num()).ljust(self.__table_len[3])} |")

                        counter += 1
                        if (counter >= len(arr)):
                            break
                else:
                    for i in range(-lastPageRecordsToPrint, 0, 1):
                        record = arr[i]
                        print(f"| {record.get_customer_name().ljust(self.__table_len[0])}", end=" | ")
                        print(f"{record.get_package_name().ljust(self.__table_len[1])}", end=" | ")
                        print(format_price(record.get_package_cost_per_pax()).ljust(self.__table_len[2]), end=" | ")
                        print(f"{str(record.get_pax_num()).ljust(self.__table_len[3])} |")
                    
                    counter = len(arr) - lastPageRecordsToPrint - rowsToPrint

                print("-" * len(header))
                
                pageStatus = f"Page {currentPage} of {maxPages}"
                print(f"{' ' * (len(header) - len(pageStatus))}{pageStatus}", end="\n\n")

                if (len(arr) > 10):
                    try:
                        continuePrompt = input("Press any keys to go to the next page or type \"b\" or \"q\" to go back or stop respectively: ").strip().lower()
                    except KeyboardInterrupt:
                        break
                    
                    if (continuePrompt == "q"): 
                        break
                    else:
                        if (continuePrompt == "b"):
                            if (currentPage != maxPages):
                                counter -= (rowsToPrint * 2)
                                currentPage -= 1
                            else:
                                currentPage -= 1
                        else:
                            currentPage += 1

                        for i in range(rowsToPrint + 8):
                            print("\033[1A\x1b[2K", end="") # move up a line and deletes the whole line
                else:
                    break
        else:
            print(f"{F.LIGHTRED_EX}Error: There is no records...")
            S_reset()

    def print_from_index(self, startIndex, endIndex):
        """
        Print the records from the database from the startIndex to the endIndex
        
        Requires 2 arguments:
        - startIndex (int)
        - endIndex (int)
        """
        self.print_from_array(self.__db[startIndex:endIndex + 1])
        print()

    def get_array(self):
        """
        Return the database array

        Returns:
        list: get the array of records
        """
        return self.__db

    def __str__(self):
        self.print_from_array(self.__db)
        return ""

    def __len__(self):
        return len(self.__db)

if (__name__ == "__main__"):
    # test codes
    from random import randint, uniform
    h = HotelDatabase()
    for i in range(1000):
        h.add_record(f"Customer {i}", f"Package {randint(1, 9999)}", randint(1, 9), uniform(50, 9999))
    h.search_for_package("Pack")
    print(h)