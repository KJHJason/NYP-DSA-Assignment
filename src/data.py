# import third party libraries
from colorama import Fore as F
from colorama import Style as S

# import standard library
import math

# import local python files
from functions import get_input, S_reset

def format_price(price):
    """
    Format the price to 2 decimal places and return a string
    
    Requires 1 argument:
    - price (int/float)
    """
    return f"${round(float(price), 2):.2f}"

def print_record_data(packageNameInput, customerNameInput, paxNumInput, packageCostPerPaxInput):
    """
    Function to print the record data in a readable format.
    
    Requires 4 arguments:
    - packageNameInput (str): The package name
    - customerNameInput (str): The customer name
    - paxNumInput (int): The number of pax
    - packageCostPerPaxInput (int/float): The package cost per pax
    """
    header = "Record Data Displayed Below:"
    maxLen = len(header)

    packageName = f"Package Name: {packageNameInput}"
    if (len(packageName) > maxLen):
        maxLen = len(packageName)

    customerName = f"Customer Name: {customerNameInput}"
    if (len(customerName) > maxLen):
        maxLen = len(customerName)

    paxNum = f"Number of Pax: {paxNumInput}"
    if (len(paxNum) > maxLen):
        maxLen = len(paxNum)

    packageCostPerPax = f"Package Cost Per Pax: {format_price(packageCostPerPaxInput)}"
    if (len(packageCostPerPax) > maxLen):
        maxLen = len(packageCostPerPax)

    print()
    print("-" * maxLen)
    print(header)
    print()
    print(packageName)
    print(customerName)
    print(paxNum)
    print(packageCostPerPax)
    print("-" * maxLen)
    return ""

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
        self.__descending_order = False
        self.__sort_order = "Not Sorted"
        self.__table_headers = ["Customer Name", "Package Name", "Cost per Pax", "Number of Pax"]
        self.__table_len = [len(self.__table_headers[0]), len(self.__table_headers[1]), len(self.__table_headers[2]), len(self.__table_headers[3])]

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
        self.__db.append(RecordData(packageName, customerName, paxNum, packageCostPerPax))

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
        Do a merge sort on the database by number of pax
        
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
            self.__db = self.merge_sort(self.__db, reverse=reverse)
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
            print(f"{F.LIGHTGREEN_EX}The database has been sorted by customer name!")
        elif (len(self.__db) == 1):
            print(f"{F.LIGHTRED_EX}Warning: There is no need to sort the database as there is only one record!")
        else:
            print(f"{F.LIGHTRED_EX}Warning: There are no records to sort!")
        S_reset()

    def search_for_customer(self, customerName):
        """
        Do a linear search on the database for the customer name to satisfy the basic function c.5. criteria
        
        Requires 1 argument:
        - customerName (string)
        """
        data = self.linear_search(customerName.title(), "customer")
        if (data == -1):
            print(f"{F.LIGHTRED_EX}Customer \"{customerName}\" not found!")
            S_reset()
            return
        print(data)
        editInput = get_input(prompt="Do you want to edit the record? (Y/N): ", command=("y", "n"))
        if (editInput == "y"):
            self.edit_record(data)

    def search_for_package(self, packageName):
        """
        Do a binary search or a linear search on the database for the package name to satisfy the basic function c.6. criteria
        
        Requires 1 argument:
        - packageName (string)
        """
        if (self.__sort_order != "Package Name" and len(self.__db) > 1):
            alertMsg = (
                "Note: In order to search for a package, you must first sort the database by package name for a faster search time...",
                "Otherwise, you can still search for a package without sorting the database by the package name but with the cost of a longer searching time"
            )
            sortInput = get_input(prompt="Do you want to sort the database by package name? (Y/N): ", prints=alertMsg, command=("y", "n"))
            if (sortInput == "y"): 
                reverseOrder = get_input(prompt="Do you want to sort the database in descending order? (Y/N): ", command=("y", "n"))
                if (reverseOrder == "y"):
                    self.heap_sort(reverse=1)
                else:
                    self.heap_sort()

                return self.search_for_package(packageName)
            else:
                record = self.linear_search(packageName.title(), "package")
                if (not record):
                    print(f"{F.LIGHTRED_EX}Package \"{packageName}\" not found!")
                    S_reset()
                else:
                    print(record)
                    editInput = get_input(prompt="Do you want to edit the record? (Y/N): ", command=("y", "n"))
                    if (editInput == "y"):
                        self.edit_record(record)
        else:
            record = self.binary_search_for_package_name(packageName.title())
            if (record == -1):
                print(f"{F.LIGHTRED_EX}Package \"{packageName}\" not found!")
                S_reset()
            else:
                print(record)
                editInput = get_input(prompt="Do you want to edit the record? (Y/N): ", command=("y", "n"))
                if (editInput == "y"):
                    self.edit_record(record)
    
    def search_for_range_of_cost(self, low, high):
        """
        Do a binary search or a linear search on the database for the range of cost specified by the user to satisfy the basic function c.7. criteria
        
        Requires 2 arguments:
        - low (int)
        - high (int)
        """
        if (self.__sort_order != "Cost Per Pax" and len(self.__db) > 1):
            alertMsg = (
                "Note: In order to search for a range of cost, you must first sort the database by package cost per pax for a faster search time...",
                "Otherwise, you can still search for a range of cost without sorting the database by the package cost per pax but with the cost of a longer searching time."
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
        flag = 0
        for i in range(len(self.__db) - 1): # -1 to stop at last element since the last element will be the highest element after an iteration from the nested for loop
            for j in range(len(self.__db) - i - 1): # -i to stop at last i element since they are already sorted and -1 to account for the indexing starting from 0
                if (reverse):
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

        self.__sort_order = "Package Name"

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

        self.__sort_order = "Cost Per Pax"

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
        
        self.__sort_order = "Package Name"

    def merge(self, leftArr, rightArr, reverse):
        """
        Merge two sub-arrays
        """
        if (reverse):
            leftArr = leftArr[::-1]
            rightArr = rightArr[::-1]

        newArr = []
        i = j = 0
        leftArrSize = len(leftArr)
        rightArrSize = len(rightArr)
        while (i < leftArrSize and j < rightArrSize):
            if (reverse):
                if (leftArr[i].get_pax_num() > rightArr[j].get_pax_num()):
                    newArr.append(leftArr[i])
                    i += 1
                else:
                    newArr.append(rightArr[j])
                    j += 1
            else:
                if (leftArr[i].get_pax_num() < rightArr[j].get_pax_num()):
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

    def merge_sort(self, arr, reverse=False):
        """
        Do a merge sort on the database by number of pax
        
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
        
        newArr = self.merge(leftHalf, rightHalf, reverse)
        return newArr

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
        while i >= 0:
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

        self.__sort_order = "Cost Per Pax"

    def print_from_array(self, arr):
        """
        Print records from the given array (to satisfy the basic function c.1. criteria)
        Pagination is an added feature of my own ;)
        
        Requires 1 argument:
        - arr (list)
        """
        print()
        print("Length of arr:", len(arr))
        if (len(arr) > 0):
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
            print(f"{F.LIGHTRED_EX}No records found")
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