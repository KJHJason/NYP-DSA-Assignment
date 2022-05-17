# import third party libraries
import re
from colorama import Fore as F

# import standard library
from math import ceil

# import local python files
from functions import get_input, S_reset, format_price, print_record_data, convert_var_to_bool
from tree_code import AVLTree
from noob_sorts import bogosort, stalinsort, slowsort, sleepsort

# regex for handling user inputs
NUM_REGEX = re.compile(r"^\d+$")
COST_REGEX = re.compile(r"^\d+(\.\d+)?$")

# header text for displaying records in a table and 
# to indicate how the array is sorted by
NOT_SORTED = "Not Sorted"
CUST_NAME = "Customer Name"
PACKAGE_NAME  = "Package Name"
PAX_NUM = "Number of Pax"
COST_PER_PAX = "Cost Per Pax"

# info on what the various slow sorting algorithms sorts by
NOOB_SORTS_INFO_DICT = {
    "bogosort": PACKAGE_NAME,
    "stalinsort": CUST_NAME,
    "slowsort": COST_PER_PAX,
    "sleepsort": PAX_NUM
}

class RecordData:
    def __init__(self, packageName, customerName, paxNum, packageCostPerPax):
        self.__packageName = packageName.title()
        self.__customerName = customerName.title()
        self.__paxNum = int(paxNum)
        self.__packageCostPerPax = round(float(packageCostPerPax), 2)

    def set_package_name(self, packageName):
        self.__packageName = packageName.title()
    def get_package_name(self):
        return self.__packageName
    def update_package_name(self):
        while (1):
            print()
            print(f"Current package name: {self.__packageName}")
            newPackageName = input("Enter a new package name (x to cancel): ").strip().lower()
            if (newPackageName.title() == self.__packageName):
                print(f"{F.LIGHTRED_EX}Package name cannot be the same as the current name!")
                S_reset()
            elif (newPackageName == ""):
                print(f"{F.LIGHTRED_EX}Package name cannot be empty!")
                S_reset()
            elif (newPackageName == "x"):
                return -1
            else:
                confirmInput = get_input(prompt=f"Are you sure you want to change the package name to \"{newPackageName.title()}\"? (Y/N): ", command=("y", "n"))
                if (confirmInput == "y"):
                    self.__packageName = newPackageName.title()
                    print(f"{F.LIGHTGREEN_EX}Package name updated!")
                    S_reset()
                    return

    def set_customer_name(self, customerName):
        self.__customerName = customerName.title()
    def get_customer_name(self):
        return self.__customerName
    def update_customer_name(self):
        while (1):
            print()
            print(f"Current customer name: {self.__customerName}")
            newCustomerName = input("Enter a new customer name (x to cancel): ").strip().lower()
            if (newCustomerName.title() == self.__customerName):
                print(f"{F.LIGHTRED_EX}Customer name cannot be the same as the current name!")
                S_reset()
            elif (newCustomerName == ""):
                print(f"{F.LIGHTRED_EX}Customer name cannot be empty!")
                S_reset()
            elif (newCustomerName == "x"):
                return -1
            else:
                confirmInput = get_input(prompt=f"Are you sure you want to change the customer name to \"{newCustomerName.title()}\"? (Y/N): ", command=("y", "n"))
                if (confirmInput == "y"):
                    self.__customerName = newCustomerName.title()
                    print(f"{F.LIGHTGREEN_EX}Customer name updated!")
                    S_reset()
                    return

    def set_pax_num(self, paxNum):
        self.__paxNum = int(paxNum)
    def get_pax_num(self):
        return self.__paxNum
    def update_pax_num(self):
        while (1):
            print()
            print(f"Current number of pax: {self.__paxNum}")
            newPaxNum = input("Enter a new number of pax (x to cancel): ").strip().lower()
            if (newPaxNum == ""):
                print(f"{F.LIGHTRED_EX}Number of pax cannot be empty!")
                S_reset()
            elif (newPaxNum == "x"):
                return -1
            elif (not re.fullmatch(NUM_REGEX, newPaxNum) or int(newPaxNum) < 1):
                print(f"{F.LIGHTRED_EX}Invalid input, please enter a valid pax number of pax more than 0...")
                S_reset()
            elif (int(newPaxNum) != self.__paxNum):
                newPaxNum = int(newPaxNum)
                confirmInput = get_input(prompt=f"Are you sure you want to change the number of pax to \"{newPaxNum}\"? (Y/N): ", command=("y", "n"))
                if (confirmInput == "y"):
                    self.__paxNum = newPaxNum
                    print(f"{F.LIGHTGREEN_EX}Number of pax updated!")
                    S_reset()
                    return
            else:
                print(f"{F.LIGHTRED_EX}Number of pax cannot be the same as the current number of pax!")
                S_reset()

    def set_package_cost_per_pax(self, packageCostPerPax):
        self.__packageCostPerPax = round(float(packageCostPerPax), 2)
    def get_package_cost_per_pax(self):
        return self.__packageCostPerPax
    def update_package_cost_per_pax(self):
        while (1):
            print()
            print(f"Current package cost per pax: {format_price(self.__packageCostPerPax)}")
            newPackageCostPerPax = input("Enter a new package cost per pax (x to cancel): $").strip().lower()
            if (newPackageCostPerPax == ""):
                print(f"{F.LIGHTRED_EX}Package cost per pax cannot be empty!")
                S_reset()
            elif (newPackageCostPerPax == "x"):
                return -1
            elif (not re.fullmatch(COST_REGEX, newPackageCostPerPax)):
                print(f"{F.LIGHTRED_EX}Package cost per pax must be a valid price!")
                S_reset()
            elif (round(float(newPackageCostPerPax), 2) != self.__packageCostPerPax):
                newPackageCostPerPax = round(float(newPackageCostPerPax), 2)
                confirmInput = get_input(prompt=f"Are you sure you want to change the package cost per pax to \"{format_price(newPackageCostPerPax)}\"? (Y/N): ", command=("y", "n"))
                if (confirmInput == "y"):
                    self.__packageCostPerPax = newPackageCostPerPax
                    print(f"{F.LIGHTGREEN_EX}Package cost per pax updated!")
                    S_reset()
                    return
            else:
                print(f"{F.LIGHTRED_EX}Package cost per pax cannot be the same as the current package cost per pax!")
                S_reset()

    def __repr__(self):
        return "(" + f"{self.__packageName}, " + f"{self.__customerName}, " + f"{self.__paxNum} pax, " + format_price(self.__packageCostPerPax) + ")"

    def __str__(self):
        return print_record_data(self.__packageName, self.__customerName, self.__paxNum, self.__packageCostPerPax)

class HotelDatabase:
    def __init__(self):
        """
        Constructor for the Hotel Database which will create an empty array and set the descending order flag to False
        """
        self.__db = []
        self.__bst_root = AVLTree() # create an AVL tree based on customer names as the keys
        self.__descending_order = False
        self.__sort_order = NOT_SORTED
        self.__table_headers = [CUST_NAME, PACKAGE_NAME, COST_PER_PAX, PAX_NUM]
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
        3. Number of Pax (int/string) -> will be converted to int if it's a string
        4. Package Cost per Pax (float/string) -> will be converted to float if it's a string
        """
        if (len(customerName) > self.__table_len[0]):
            self.__table_len[0] = len(customerName)

        if (len(packageName) > self.__table_len[1]):
            self.__table_len[1] = len(packageName)

        formattedPackageCostPerPax = format_price(packageCostPerPax)
        if (len(formattedPackageCostPerPax) > self.__table_len[2]):
            self.__table_len[2] = len(formattedPackageCostPerPax)

        if (len(str(paxNum)) > self.__table_len[3]):
            self.__table_len[3] = len(str(paxNum))

        self.__sort_order = NOT_SORTED
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
                res = record.update_package_name()
                print()
                if (res == -1):
                    return

                res = record.update_customer_name()
                print()
                if (res == -1):
                    return

                res = record.update_pax_num()
                print()
                if (res == -1):
                    return

                res = record.update_package_cost_per_pax()
                if (res == -1):
                    return
            elif (whichToEdit == "x"):
                return
            else:
                print(f"{F.LIGHTRED_EX}Invalid input...")
                S_reset()

    def sort_by_pax_num(self, reverse=False):
        """
        Do a 3 way quicksort on the database by number of pax
        
        Optional parameter:
        - reverse (bool)
        """
        reverse = convert_var_to_bool(reverse)

        if (self.__sort_order == PAX_NUM and self.__descending_order == reverse):
            print(f"{F.LIGHTRED_EX}Notice: The database is already sorted by the package's number of pax!")
            S_reset()
            return

        if (len(self.__db) > 1):
            self.shellsort(reverse=reverse)
            self.__descending_order = reverse
            self.__sort_order = PAX_NUM
            print(f"{F.LIGHTGREEN_EX}The database has been sorted by the package's number of pax!")
        elif (len(self.__db) == 1):
            print(f"{F.LIGHTRED_EX}Warning: There is no need to sort the database as there is only one record!")
        else:
            print(f"{F.LIGHTRED_EX}Warning: There are no records to sort!")
        S_reset()

    def sort_by_customer_name(self, reverse=False, typeOfSort="tree"):
        """
        Do a bubble sort on the database by customer name to satisfy the basic function c.2. criteria
        
        Optional parameter:
        - reverse (bool)
        """
        reverse = convert_var_to_bool(reverse)

        if (self.__sort_order == CUST_NAME and self.__descending_order == reverse):
            print(f"{F.LIGHTRED_EX}Notice: The database is already sorted by the customer's name!")
            S_reset()
            return

        if (len(self.__db) > 1):
            if (typeOfSort == "tree"):
                self.__db = self.__bst_root.tree_sort(reverse=reverse)
            else:
                self.bubble_sort(reverse=reverse)

            self.__descending_order = reverse
            self.__sort_order = CUST_NAME
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
        reverse = convert_var_to_bool(reverse)

        if (self.__sort_order == PACKAGE_NAME and self.__descending_order == reverse):
            print(f"{F.LIGHTRED_EX}Notice: The database is already sorted by the package's name!")
            S_reset()
            return

        if (len(self.__db) > 1):
            self.selection_sort(reverse=reverse)
            self.__descending_order = reverse
            self.__sort_order = PACKAGE_NAME
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
        reverse = convert_var_to_bool(reverse)

        if (self.__sort_order == COST_PER_PAX and self.__descending_order == reverse):
            print(f"{F.LIGHTRED_EX}Notice: The database is already sorted by the package's cost!")
            S_reset()
            return

        if (len(self.__db) > 1):
            self.insertion_sort(reverse=reverse)
            self.__descending_order = reverse
            self.__sort_order = COST_PER_PAX
            print(f"{F.LIGHTGREEN_EX}The database has been sorted by package cost!")
        elif (len(self.__db) == 1):
            print(f"{F.LIGHTRED_EX}Warning: There is no need to sort the database as there is only one record!")
        else:
            print(f"{F.LIGHTRED_EX}Warning: There are no records to sort!")
        S_reset()

    def get_index_from_list(self, data=-1, mode=None, typeOfOperations=None, target=None):
        """
        Function to get the index from a list of data.
        Used to when there is duplicate data in the search results.
        
        Requires 4 arguments:
        - data (list/int): if int, it must be -1 to indicate no results found
        - mode (str): mode is defined as what type of data, e.g. "customer" and "package".
        - typeOfOperations (str): operations such as "edit" and "delete"
        - target (str): the target data to be passed into such as the customer/package name
        """
        if (not target or typeOfOperations.lower() not in ("edit", "delete") or mode.lower() not in ("customer", "package")):
            raise ValueError(f"Invalid arguments, {mode} or {typeOfOperations} or {target}, in get_index_from_list()")

        if (data == -1 or not data):
            # if data is equal to -1 or is an empty list
            print(f"{F.LIGHTRED_EX}{mode.title()} \"{target}\" not found!")
            S_reset()
            return -1

        numIndexPrompt = ""
        if (len(data) > 1):
            print(f"\n{F.LIGHTGREEN_EX}Multiple records found with the {mode} name, {target}!")
            print(f"{F.LIGHTGREEN_EX}Please select the record you wish to {typeOfOperations.lower()} after looking at the search results!\n")
            S_reset()
            self.print_from_array(data)
            numIndexPrompt = f"Which record would you like to {typeOfOperations.lower()}? (x to cancel): No."
            if (len(data) > 10):
                numIndexPrompt = f"Which record would you like to {typeOfOperations.lower()}? (x to cancel/v to view table): No."
        else:
            return 0

        index = 0
        while (1):
            numIndexChoice = input(numIndexPrompt).strip()
            if (numIndexChoice.lower() == "x"):
                print(f"{F.LIGHTRED_EX}Cancelled {typeOfOperations.lower()} operation with {mode}, {target}!")
                S_reset(nl=True)
                return -1
            elif (len(data) > 10 and numIndexChoice.lower() == "v"):
                return self.get_index_from_list(data=data, mode=mode, typeOfOperations=typeOfOperations, target=target)
            elif (numIndexChoice == ""):
                print(f"{F.LIGHTRED_EX}Please enter a number from the table!")
                S_reset(nl=True)
            elif (re.fullmatch(NUM_REGEX, numIndexChoice)):
                index = int(numIndexChoice) - 1
                if (index >= 0 and index < len(data)):
                    return index
                else:
                    print(f"{F.LIGHTRED_EX}Invalid input, please enter a number between 1 and {len(data)}!")
                    S_reset(nl=True)
            else:
                print(f"{F.LIGHTRED_EX}Invalid input, please enter a number from the table \"No.\" column!")
                S_reset(nl=True)

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
                S_reset(nl=True)
                return -1

        data = self.linear_search(customerName, "customer")
        index = self.get_index_from_list(data=data, mode="customer", typeOfOperations=mode, target=customerName)
        if (index == -1):
            return

        data = data[index]
        print(data)
        inp = get_input(prompt=f"Do you want to {mode.lower()} this record? (Y/N): ", command=("y", "n"))
        if (inp == "y" and mode == "Edit"):
            oldCustName = data.get_customer_name()
            self.edit_record(data)
            if (oldCustName != data.get_customer_name()):
                self.__bst_root.move_node(data)
        elif (inp == "y" and mode == "Delete"):
            self.delete_record(data)
            self.__bst_root.delete(data)

    def search_for_package(self, packageName, mode="Edit"):
        """
        Do a binary search on the database for the package name to satisfy the basic function c.6. criteria
        
        Note: Depending on the user's preference, the package name can be searched using linear search algorithm if the user wish to perserve the order of the database.
        
        Requires 1 argument:
        - packageName (string)
        """
        mode = mode.title()
        packageName = packageName.title()
        if (self.__sort_order != PACKAGE_NAME and len(self.__db) > 1):
            alertMsg = (
                f"{F.LIGHTYELLOW_EX}Note: You can first sort the database by package name for a faster search time in future searches...",
                "Otherwise, you can still search for a package and maintain the original order of the database..."
            )
            sortInput = get_input(prompt="Do you want to sort the database by package name? (Y/N): ", prints=alertMsg, command=("y", "n"))
            if (sortInput == "y"): 
                reverseOrder = get_input(prompt="Do you want to sort the database in descending order? (Y/N): ", command=("y", "n"))

                reverseOrder = convert_var_to_bool(reverseOrder)
                self.heap_sort(reverse=reverseOrder)
                self.__descending_order = reverseOrder


                print(f"{F.LIGHTGREEN_EX}The database has been sorted by package name!")
                S_reset(nl=True)
                self.__sort_order = PACKAGE_NAME

                return self.search_for_package(packageName, mode=mode)
            else:
                records = self.linear_search(packageName, "package")
                index = self.get_index_from_list(data=records, mode="package", typeOfOperations=mode, target=packageName)
                if (index == -1):
                    return

                record = records[index]
                print(record)
                userInput = get_input(prompt=f"Do you want to {mode.lower()} this record? (Y/N): ", command=("y", "n"))
                if (userInput == "y" and mode == "Edit"):
                    self.edit_record(record)
                elif (userInput == "y" and mode == "Delete"):
                    self.delete_record(record)
        else:
            lowIndex, highIndex = self.binary_search_for_package_name(packageName)
            records = self.__db[lowIndex:highIndex + 1]
            index = self.get_index_from_list(data=records, mode="package", typeOfOperations=mode, target=packageName)
            if (index == -1):
                return

            record = records[index]
            print(record)
            userInput = get_input(prompt=f"Do you want to {mode.lower()} this record? (Y/N): ", command=("y", "n"))
            if (userInput == "y" and mode == "Edit"):
                self.edit_record(record)
            elif (userInput == "y" and mode == "Delete"):
                self.delete_record(record)
                self.__bst_root.delete(record)

    def search_for_range_of_cost(self, low, high):
        """
        Do a binary search or a linear search on the database for the range of cost specified by the user to satisfy the basic function c.7. criteria
        
        Requires 2 arguments:
        - low (int)
        - high (int)
        """
        if (self.__sort_order != COST_PER_PAX and len(self.__db) > 1):
            alertMsg = (
                f"{F.LIGHTYELLOW_EX}Note: You can first sort the database by package cost per pax for a faster search time in future searches...",
                "Otherwise, you can still search for packages that fits within the specified range of cost and maintain the original order of the database..."
            )
            sortInput = get_input(prompt="Do you want to sort the database by package cost per pax? (Y/N): ", prints=alertMsg, command=("y", "n"))
            if (sortInput == "y"):
                reverseOrder = get_input(prompt="Do you want to sort the database in descending order? (Y/N): ", command=("y", "n"))

                reverseOrder = convert_var_to_bool(reverseOrder)
                self.radix_sort(reverse=reverseOrder)
                self.__descending_order = reverseOrder

                print(f"{F.LIGHTGREEN_EX}The database has been sorted by package cost per pax!")
                S_reset(nl=True)
                self.__sort_order = COST_PER_PAX
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

    def costLowerIndex(self, i, lowerRange):
        """
        Search for any records within the lowerRange of the cost specified by the user starting from the index found from a search algorithm.
        Limitations: Array must sorted by package cost per pax
        
        Requires 2 arguments:
        - i (int) <-- refers to the index obtained from a search algorithm
        - lowerRange (int)
        
        Best time complexity: O(n)
        Worst time complexity: O(n)
        Average time complexity: O(n)
        """
        if (not self.__descending_order):
            while (i > 0 and self.__db[i - 1].get_package_cost_per_pax() >= lowerRange):
                i -= 1
        else:
            while (i < len(self.__db) - 1 and self.__db[i + 1].get_package_cost_per_pax() >= lowerRange):
                i += 1
        return i

    def costUpperIndex(self, i, upperRange):
        """
        Search for any records within the upperRange of the cost specified by the user starting from the index found from a search algorithm.
        Limitations: Array must sorted by package cost per pax
        
        Requires 2 arguments:
        - i (int) <-- refers to the index obtained from a search algorithm
        - upperRange (int)
        
        Best time complexity: O(n)
        Worst time complexity: O(n)
        Average time complexity: O(n)
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
        """
        l = 0
        r = len(self.__db) - 1
        while (l <= r):
            mid = (l + r) // 2
            
            # return mid if the range is found in the subarray
            if (self.__db[mid].get_package_cost_per_pax() >= lowRange and self.__db[mid].get_package_cost_per_pax() <= highRange):
                if (self.__descending_order):
                    return self.costUpperIndex(mid, highRange), self.costLowerIndex(mid, lowRange)
                else:
                    return self.costLowerIndex(mid, lowRange), self.costUpperIndex(mid, highRange)

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
        """
        arr = []
        for record in self.__db:
            if (record.get_package_cost_per_pax() >= low and record.get_package_cost_per_pax() <= high):
                arr.append(record)
        return arr

    def get_val(self, record, typeOfVal):
        """
        Get the respective attribute from the RecordData object based on the typeOfVal given.
        
        Used in the linear search function below.
        
        Requires 2 arguments:
        - record (RecordData)
        - typeOfVal (str): "customer" or "package"
        """
        return record.get_customer_name() if (typeOfVal == "customer") \
                                          else record.get_package_name()

    def linear_search(self, target, typeOfSearch):
        """
        Do a linear search on the database for the customer name
        
        Requires 2 arguments:
        - target (string)
        - typeOfSearch (string) <-- "customer" or "package"
        
        Best time complexity: O(n)
        Worst time complexity: O(n)
        Average time complexity: O(n)
        """
        if (typeOfSearch not in ("customer", "package")):
            raise ValueError(f"Invalid search type, {typeOfSearch}, Must be either \"customer\" or \"package\"!")

        arr = []
        for record in self.__db:
            if (self.get_val(record, typeOfSearch) == target):
                arr.append(record)
        return -1 if (len(arr) == 0) else arr

    def findAllNameOccurrences(self, i, name):
        """
        Search for all occurrences of the target name specified by the user starting from the index found from a search algorithm.
        Limitations: Array must sorted by target name type
        
        Requires 2 arguments:
        - i (int) <-- refers to the index obtained from a search algorithm
        - name (string) <-- package name
        
        Best time complexity: O(n)
        Worst time complexity: O(n)
        Average time complexity: O(n)
        """
        iCopy = i
        # search the right
        while (i < len(self.__db) - 1 and self.__db[i + 1].get_package_name() == name):
            i += 1

        # search the left
        while (iCopy > 0 and self.__db[iCopy - 1].get_package_name() == name):
            iCopy -= 1

        return iCopy, i

    def binary_search_for_package_name(self, packageName):
        """
        Do a binary search on the database for the package name
        
        Requires 1 argument:
        - packageName (string)
        
        Best time complexity: O(1)
        Worst time complexity: O(log(n))
        Average time complexity: O(log(n))
        """
        l = 0
        r = len(self.__db) - 1
        while (l <= r):
            mid = (l + r) // 2
            
            # return mid if the package name is found in the subarray
            if (self.__db[mid].get_package_name() == packageName):
                # will return the index of the first and last occurrence of the package name in a tuple
                return self.findAllNameOccurrences(mid, packageName) 

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

        return -1, -1 # return -1 if the package name is not found

    def bubble_sort(self, reverse=False):
        """
        Do a bubble sort on the database by customer name
        
        Optional argument:
        - reverse (bool)
        
        Best time complexity: O(n)
        Worst time complexity: O(n^2)
        Average time complexity: O(n^2)
        """
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
        """
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
        """
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
        """
        n = len(self.__db) 

        # Build a min or max heap depending on the reverse condition
        # if in ascending order, then build a max heap
        # if in descending order, then build a min heap
        for i in range((n // 2) - 1, -1, -1): 
            self.heapify(n, i, reverse) 

        # extract elements individually starting from the end
        for i in range(n - 1, -1, -1): 
            self.__db[i], self.__db[0] = self.__db[0], self.__db[i] # swap the first element with the last node from the heap
            self.heapify(i, 0, reverse) # call heapify on the reduced list

    def shellsort(self, reverse=False):
        """
        Shellsort algorithm works like the insertion sort algorithm but
        shellsort will sort the elements that are far apart from each other,
        and progressively reduces the interval gap between the elements to be compared.
        
        Sorts by pax number
        
        Best Time Complexity: O(n log n)
        Average Time Complexity: O(n log n)
        Worst Time Complexity: O(n^2)
        """
        # initialise the gap by halving the array size first
        arr = self.__db
        gap = len(arr) // 2

        while (gap > 0):
            # loop through the elements in the array in intervals of the gap
            for i in range(gap, len(arr)):
                temp = arr[i] # store the current element as temp
                j = i # initialise j to be the value of i

                # rearrange the elements at n/2, n/4, n/8, ... intervals

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
        Pagination is an added feature.
        
        Requires 1 argument:
        - arr (list)
        """
        print()
        if (len(arr) > 0):
            # calculate the number of padding to add for the number header
            noHeader = "No."
            noHeaderLen = len(str(len(arr)))
            if (noHeaderLen > len(noHeader)):
                noLen = noHeaderLen
            else:
                noLen = len(noHeader)

            print("Numbers of results found:", len(arr))
            header = f"| {noHeader.ljust(noLen)} | {'Customer Name'.ljust(self.__table_len[0])} | {'Package Name'.ljust(self.__table_len[1])} | {'Cost Per Pax'.ljust(self.__table_len[2])} | {'Number of Pax'.ljust(self.__table_len[3])} |"

            # default rows to print per page, change at own will
            rowsToPrint = 10
            
            # initialise some variables
            counter = 0
            currentPage = 1
            maxPages = ceil(len(arr) / rowsToPrint)

            lastPageRecordsToPrint = len(arr) % rowsToPrint
            if (lastPageRecordsToPrint == 0):
                lastPageRecordsToPrint = rowsToPrint

            # for the no. header numbers for the last page as the last page is using negative indexing
            noLastPageArr = [str(i + 1) for i in range(len(arr) - lastPageRecordsToPrint, len(arr))]

            while (1):
                print("-" * len(header))
                print(header)
                print("-" * len(header))

                # reset the counter and current page if the current page exceeds the max pages
                if (currentPage > maxPages):
                    currentPage = 1
                    counter = 0
                # if the current page is 0, print the last page
                elif (currentPage < 1):
                    currentPage = maxPages
                    counter = 0

                # for the front few pages
                if (currentPage != maxPages):
                    for i in range(counter, counter + rowsToPrint):
                        record = arr[i]
                        print(f"| {str(i + 1).ljust(noLen)}", end=" | ")
                        print(f"{record.get_customer_name().ljust(self.__table_len[0])}", end=" | ")
                        print(f"{record.get_package_name().ljust(self.__table_len[1])}", end=" | ")
                        print(format_price(record.get_package_cost_per_pax()).ljust(self.__table_len[2]), end=" | ")
                        print(f"{str(record.get_pax_num()).ljust(self.__table_len[3])} |")

                        counter += 1
                        if (counter >= len(arr)):
                            break
                # for the last page which will use negative indexing
                else:
                    for i in range(-lastPageRecordsToPrint, 0, 1):
                        record = arr[i]
                        print(f"| {noLastPageArr[i].ljust(noLen)}", end=" | ")
                        print(f"{record.get_customer_name().ljust(self.__table_len[0])}", end=" | ")
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
                    except (KeyboardInterrupt):
                        # ctrl + c to quit
                        return

                    # quit by entering q
                    if (continuePrompt == "q"): 
                        return
                    else:
                        # continue and calculate the counter and current page
                        if (continuePrompt == "b"):
                            if (currentPage != maxPages):
                                counter -= (rowsToPrint * 2)
                                currentPage -= 1
                            else:
                                currentPage -= 1
                        else:
                            currentPage += 1

                        for _ in range(rowsToPrint + 8):
                            print("\033[1A\x1b[2K", end="") # move up a line and deletes the whole line
                else:
                    return
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
    
    def easter_egg_sorts(self, typeOfSort="bogosort"):
        """
        Method to sort the database using different non-sensical sorts such as bogosort
        
        Requires 1 argument:
        - typeOfSort (str) -> "bogosort", "stalinsort", "slowsort", "sleepsort"
        """
        if (not NOOB_SORTS_INFO_DICT.get(typeOfSort)):
            raise ValueError(f"Error: {typeOfSort} is not a valid sort type in easter_egg_sorts()")

        if (NOOB_SORTS_INFO_DICT[typeOfSort] == self.__sort_order and self.__descending_order == False):
            print(f"{F.LIGHTRED_EX}Error: The database is already sorted by {NOOB_SORTS_INFO_DICT[typeOfSort].lower()}...")
            S_reset()
            return

        if (typeOfSort == "bogosort"):
            # sorts by package name
            print("\nSorting...", end="")
            self.__db, iterNums = bogosort(self.__db)
            print(f"\r{F.LIGHTGREEN_EX}The database has been sorted after {iterNums} iterations by package name!")
            S_reset(nl=True)
        elif (typeOfSort == "stalinsort"):
            # sorts by customer name
            self.__db = stalinsort(self.__db)
            print(f"{F.LIGHTGREEN_EX}The database has been sorted by customer name!")
            S_reset()
        elif (typeOfSort == "slowsort"):
            # sorts by package cost per pax
            slowsort(self.__db, 0, len(self.__db) - 1)
            print(f"{F.LIGHTGREEN_EX}The database has been sorted by package cost!")
            S_reset()
        elif (typeOfSort == "sleepsort"):
            # sorts by pax number
            self.__db = sleepsort(self.__db)
            print(f"{F.LIGHTGREEN_EX}The database has been sorted by the package's number of pax!")
            S_reset()

        self.__descending_order = False
        self.__sort_order = NOOB_SORTS_INFO_DICT[typeOfSort]

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

# test codes
if (__name__ == "__main__"):
    from random import randint, uniform
    h = HotelDatabase()
    for i in range(1000):
        h.add_record(f"Customer {i}", f"Package {randint(1, 9999)}", randint(1, 9), uniform(50, 9999))
        
    # add main test code below
    print(h)