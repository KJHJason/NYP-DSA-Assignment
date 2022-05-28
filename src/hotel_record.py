# import third party libraries
import re
from colorama import Fore as F

# import standard library
from math import ceil

# import local python files
from functions import get_input, S_reset, format_price, print_record_data, convert_var_to_bool

# import data structures
from data_structures.AVLTree import AVLTree

# import sorting algorithms
from sorting_algorithms.noob_sorts import bogosort, stalinsort, slowsort, sleepsort
from sorting_algorithms.radix_sort import radix_sort
from sorting_algorithms.shellsort import shellsort
from sorting_algorithms.heap_sort import heap_sort
from sorting_algorithms.pancake_sort import pancake_sort
from sorting_algorithms.insertion_sort import insertion_sort
from sorting_algorithms.selection_sort import selection_sort
from sorting_algorithms.bubble_sort import bubble_sort

# import searching algorithms
from searching_algorithms.binary_search import binary_search_for_name, binary_search_for_range_of_cost
from searching_algorithms.linear_search import linear_search_for_name, linear_search_range_of_cost
from searching_algorithms.exponential_search import exponential_search_for_customer
from searching_algorithms.fibonacci_search import fibonacci_search_for_package_name

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
    "bozosort": PACKAGE_NAME,
    "stalinsort": CUST_NAME,
    "slowsort": COST_PER_PAX,
    "sleepsort": PAX_NUM
}

class RecordData:
    """
    Creates a RecordData object with methods to update each of its attributes.
    
    Used to hold each Staycation booking records information such as:
    - package name
    - customer name
    - number of pax
    - package cost per pax
    These attributes satisfy the basic function a
    
    Requires 4 arguments to initialise the object:
        - packageName: the name of the package
        - customerName: the name of the customer
        - paxNum: the number of pax in the package
        - packageCostPerPax: the package cost per pax of the package
    
    Note that paxNum and packageCostPerPax will be converted to integers and floats respectively.
    """
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

    def get_val(self, attribute=None):
        """
        Returns the value of the specified attribute.
        
        Requires one argument:
        - attribute(str): The attribute to get the value of.
            - "packageName"
            - "customerName"
            - "paxNum"
            - "packageCostPerPax"
        """
        if (attribute == "packageName"):
            return self.get_package_name()
        elif (attribute == "customerName"):
            return self.get_customer_name()
        elif (attribute == "paxNum"):
            return self.get_pax_num()
        elif (attribute == "packageCostPerPax"):
            return self.get_package_cost_per_pax()
        else:
            raise ValueError(f"Invalid attribute \"{attribute}\" in get_val in RecordData object!")

    def __repr__(self):
        return "(" + f"{self.__packageName}, " + f"{self.__customerName}, " + f"{self.__paxNum} pax, " + format_price(self.__packageCostPerPax) + ")"

    def __str__(self):
        return print_record_data(self.__packageName, self.__customerName, self.__paxNum, self.__packageCostPerPax)

class HotelDatabase:
    """
    Will create a HotelDatabase object responsible for storing and managing all hotel records.
    
    Upon initialisation, this object will create an empty array which would hold all hotel records
    of RecordData objects.
    """
    def __init__(self):
        # Array of RecordData objects
        self.__db = []

        # create an AVL tree based on customer names as the keys
        self.__bst_root = AVLTree() 

        # boolean to determine whether to sort the records in descending order
        self.__descending_order = False 

        # to determine the current sort order
        self.__sort_order = NOT_SORTED 

        # table headers
        self.__table_headers = [CUST_NAME, PACKAGE_NAME, COST_PER_PAX, PAX_NUM] 
        
        # table lengths for padding
        self.__table_len = [len(self.__table_headers[0]), len(self.__table_headers[1]), \
                            len(self.__table_headers[2]), len(self.__table_headers[3])] 

    def delete_record(self, record=None, index=None):
        """
        Deletes a record from the database
        
        Requires either one of the two arguments:
        record: The record to be deleted (defaults to None)
        index: The index of the record to be deleted (defaults to None)
        """
        if (index is None):
            self.__db.remove(record)
        else:
            self.__db.pop(index)
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

    def edit_all_details_of_record(self, record):
        """
        Edits all details of a record and updates the sorting order if necessary.
        
        Requires 1 argument:
        - record (RecordData)
        """
        res = record.update_package_name()
        print()
        if (res == -1):
            return
        elif (self.__sort_order == PACKAGE_NAME):
            self.__sort_order = NOT_SORTED

        res = record.update_customer_name()
        print()
        if (res == -1):
            return
        elif (self.__sort_order == CUST_NAME):
            self.__sort_order = NOT_SORTED

        res = record.update_pax_num()
        print()
        if (res == -1):
            return
        elif (self.__sort_order == PAX_NUM):
            self.__sort_order = NOT_SORTED

        res = record.update_package_cost_per_pax()
        if (res == -1):
            return
        elif (self.__sort_order == COST_PER_PAX):
            self.__sort_order = NOT_SORTED

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
                res = record.update_package_name()
                if (res != -1 and self.__sort_order == PACKAGE_NAME):
                    self.__sort_order = NOT_SORTED

            elif (whichToEdit == "2"):
                res = record.update_customer_name()
                if (res != -1 and self.__sort_order == CUST_NAME):
                    self.__sort_order = NOT_SORTED

            elif (whichToEdit == "3"):
                res = record.update_pax_num()
                if (res != -1 and self.__sort_order == PAX_NUM):
                    self.__sort_order = NOT_SORTED

            elif (whichToEdit == "4"):
                res = record.update_package_cost_per_pax()
                if (res != -1 and self.__sort_order == COST_PER_PAX):
                    self.__sort_order = NOT_SORTED

            elif (whichToEdit == "5"):
                print(record, end="")
            elif (whichToEdit == "a"):
                self.edit_all_details_of_record(record)
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
            shellsort(self.__db, reverse=reverse)
            self.__descending_order = reverse
            self.__sort_order = PAX_NUM
            print(f"{F.LIGHTGREEN_EX}The database has been sorted by the package's number of pax!")
        elif (len(self.__db) == 1):
            print(f"{F.LIGHTRED_EX}Notice: There is no need to sort the database as there is only one record!")
        else:
            print(f"{F.LIGHTRED_EX}Notice: There are no records to sort!")
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
                bubble_sort(self.__db, reverse=reverse)

            self.__descending_order = reverse
            self.__sort_order = CUST_NAME
            print(f"{F.LIGHTGREEN_EX}The database has been sorted by customer name!")
        elif (len(self.__db) == 1):
            print(f"{F.LIGHTRED_EX}Notice: There is no need to sort the database as there is only one record!")
        else:
            print(f"{F.LIGHTRED_EX}Notice: There are no records to sort!")
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
            selection_sort(self.__db, reverse=reverse)
            self.__descending_order = reverse
            self.__sort_order = PACKAGE_NAME
            print(f"{F.LIGHTGREEN_EX}The database has been sorted by package name!")
        elif (len(self.__db) == 1):
            print(f"{F.LIGHTRED_EX}Notice: There is no need to sort the database as there is only one record!")
        else:
            print(f"{F.LIGHTRED_EX}Notice: There are no records to sort!")
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
            insertion_sort(self.__db, reverse=reverse)
            self.__descending_order = reverse
            self.__sort_order = COST_PER_PAX
            print(f"{F.LIGHTGREEN_EX}The database has been sorted by package cost!")
        elif (len(self.__db) == 1):
            print(f"{F.LIGHTRED_EX}Notice: There is no need to sort the database as there is only one record!")
        else:
            print(f"{F.LIGHTRED_EX}Notice: There are no records to sort!")
        S_reset()

    def get_index_from_list(self, data=-1, dataOrigIndex=[], mode=None, typeOfOperations=None, target=None):
        """
        Function to get the index from a list of data.
        Used to when there is duplicate data in the search results.
        
        Requires 5 arguments:
        - data (list/int): if int, it must be -1 to indicate no results found
        - dataOrigIndex (list): the original index of the data in self.__db
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
            return -1, -1

        if (len(data) != len(dataOrigIndex)):
            raise ValueError("The length of data and dataOrigIndex arrays must be the same in get_index_from_list() function!")

        numIndexPrompt = ""
        if (len(data) == 1):
            return 0, dataOrigIndex[0]

        print(f"\n{F.LIGHTGREEN_EX}Multiple records found with the {mode} name, {target}!")
        print(f"{F.LIGHTGREEN_EX}Please select the record you wish to {typeOfOperations.lower()} after looking at the search results!\n")
        S_reset()

        self.print_from_array(data)
        numIndexPrompt = f"Which record would you like to {typeOfOperations.lower()}? (x to cancel): No."
        if (len(data) > 10):
            numIndexPrompt = f"Which record would you like to {typeOfOperations.lower()}? (x to cancel/v to view table): No."

        index = 0
        while (1):
            numIndexChoice = input(numIndexPrompt).strip()
            if (numIndexChoice.lower() == "x"):
                print(f"{F.LIGHTRED_EX}Cancelled {typeOfOperations.lower()} operation with {mode}, {target}!")
                S_reset(nl=True)
                return -1, -1
            elif (len(data) > 10 and numIndexChoice.lower() == "v"):
                return self.get_index_from_list(data=data, dataOrigIndex=dataOrigIndex, mode=mode, typeOfOperations=typeOfOperations, target=target)
            elif (numIndexChoice == ""):
                print(f"{F.LIGHTRED_EX}Please enter a number from the table!")
                S_reset(nl=True)
            elif (re.fullmatch(NUM_REGEX, numIndexChoice)):
                index = int(numIndexChoice) - 1
                if (index >= 0 and index < len(data)):
                    return index, dataOrigIndex[index]
                else:
                    print(f"{F.LIGHTRED_EX}Invalid input, please enter a number between 1 and {len(data)}!")
                    S_reset(nl=True)
            else:
                print(f"{F.LIGHTRED_EX}Invalid input, please enter a number from the table \"No.\" column!")
                S_reset(nl=True)

    def search_for_customer(self, customerName, mode="Edit"):
        """
        Do a linear search on the database for the customer name to satisfy the basic function c.5. criteria
        
        Requires 2 argument:
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

        if (self.__sort_order != CUST_NAME and len(self.__db) > 1):
            alertMsg = [
                f"{F.LIGHTYELLOW_EX}Note: You can first sort the database by customer name for a faster search time in future searches,",
                "Otherwise, you can still search for a customer and maintain the original order of the database..."
            ]
            if (mode == "Edit"):
                alertMsg.append("assuming that the customer name is unchanged when editing the record.")
                alertMsg[1], alertMsg[2] = alertMsg[2], alertMsg[1]

            alertMsg = tuple(alertMsg)

            sortInput = get_input(prompt="Do you want to sort the database by customer name? (Y/N): ", prints=alertMsg, command=("y", "n"))
            if (sortInput == "y"): 
                reverseOrder = get_input(prompt="Do you want to sort the database in descending order? (Y/N): ", command=("y", "n"))

                reverseOrder = convert_var_to_bool(reverseOrder)
                self.__db = self.__bst_root.tree_sort(reverse=reverseOrder)
                self.__descending_order = reverseOrder

                print(f"{F.LIGHTGREEN_EX}The database has been sorted by customer name!")
                S_reset(nl=True)
                self.__sort_order = CUST_NAME

                return self.search_for_customer(customerName, mode=mode)
            else:
                dataTuple = linear_search_for_name(self.__db, customerName, "customerName")
                data = []
                dataOrigIndex = []
                if (dataTuple != -1):
                    for matchedData in dataTuple:
                        data.append(matchedData[0])
                        dataOrigIndex.append(matchedData[1])
        else:
            lowIndex, highIndex = exponential_search_for_customer(self.__db, customerName, self.__descending_order)
            data = self.__db[lowIndex:highIndex + 1]
            dataOrigIndex = list(range(lowIndex, highIndex + 1))

        index, dbIndex = self.get_index_from_list(data=data, dataOrigIndex=dataOrigIndex, mode="customer", typeOfOperations=mode, target=customerName)
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
            self.delete_record(index=dbIndex)
            self.__bst_root.delete(data)

    def search_for_package(self, packageName, mode="Edit"):
        """
        Do a binary search on the database for the package name to satisfy the basic function c.6. criteria
        
        Note: Depending on the user's preference, the package name can be searched using linear search algorithm if the user wish to perserve the order of the database.
        
        Requires 2 arguments:
        - packageName (string)
        - mode (string): "Edit" or "Display" or "Delete", defaults to "Edit"
        """
        mode = mode.title()
        packageName = packageName.title()

        if (mode == "Display"):
            if (self.__sort_order != PACKAGE_NAME and len(self.__db) > 1):
                alertMsg = (
                    f"{F.LIGHTYELLOW_EX}Note: You can first sort the database by package name for a faster search time in future searches,",
                    "Otherwise, you can still search for a package and maintain the original order of the database..."
                )
                sortInp = get_input(prompt="Do you want to sort the database by package name? (Y/N): ", command=("y", "n"), prints=alertMsg)
                if (sortInp == "y"):
                    reverseOrder = get_input(prompt="Do you want to sort the database in descending order? (Y/N): ", command=("y", "n"))

                    reverseOrder = convert_var_to_bool(reverseOrder)
                    pancake_sort(self.__db, reverseOrder)
                    self.__descending_order = reverseOrder
                    self.__sort_order = PACKAGE_NAME

                    print(f"{F.LIGHTGREEN_EX}The database has been sorted by package name!")
                    S_reset(nl=True)
                    return self.search_for_package(packageName, mode=mode)
                else:
                    recordsTuple = linear_search_for_name(self.__db, packageName, "packageName")
                    if (recordsTuple != -1):
                        records = [record[0] for record in recordsTuple]
                        return self.print_from_array(records)
                    else:
                        print(f"{F.LIGHTRED_EX}No records found with the package name, {packageName}!")
                        S_reset(nl=True)
                        return -1
            else:
                lowIndex, highIndex = fibonacci_search_for_package_name(self.__db, packageName, descendingOrder=self.__descending_order)

                if (lowIndex == -1 and highIndex == -1):
                    print(f"{F.LIGHTRED_EX}No records found with the package name, {packageName}!")
                    S_reset(nl=True)
                    return -1

                return self.print_from_index(lowIndex, highIndex)
        
        if (self.__sort_order != PACKAGE_NAME and len(self.__db) > 1):
            alertMsg = [
                f"{F.LIGHTYELLOW_EX}Note: You can first sort the database by package name for a faster search time in future searches,",
                "Otherwise, you can still search for a package and maintain the original order of the database..."
            ]
            if (mode == "Edit"):
                alertMsg.append("assuming that the package name is unchanged when editing the record.")
                alertMsg[1], alertMsg[2] = alertMsg[2], alertMsg[1]

            alertMsg = tuple(alertMsg)

            sortInput = get_input(prompt="Do you want to sort the database by package name? (Y/N): ", prints=alertMsg, command=("y", "n"))
            if (sortInput == "y"): 
                reverseOrder = get_input(prompt="Do you want to sort the database in descending order? (Y/N): ", command=("y", "n"))

                reverseOrder = convert_var_to_bool(reverseOrder)
                heap_sort(self.__db, reverse=reverseOrder)
                self.__descending_order = reverseOrder

                print(f"{F.LIGHTGREEN_EX}The database has been sorted by package name!")
                S_reset(nl=True)
                self.__sort_order = PACKAGE_NAME

                return self.search_for_package(packageName, mode=mode)
            else:
                recordsTuple = linear_search_for_name(self.__db, packageName, "packageName")
                records = []
                recordsOrigIndex = []
                if (recordsTuple != -1):
                    for matchedData in recordsTuple:
                        records.append(matchedData[0])
                        recordsOrigIndex.append(matchedData[1])
        else:
            lowIndex, highIndex = binary_search_for_name(self.__db, packageName, self.__descending_order, "packageName")
            records = self.__db[lowIndex:highIndex + 1]
            recordsOrigIndex = list(range(lowIndex, highIndex + 1))

        index, dbIndex = self.get_index_from_list(data=records, dataOrigIndex=recordsOrigIndex, mode="package", typeOfOperations=mode, target=packageName)
        if (index == -1):
            return

        record = records[index]
        print(record)
        userInput = get_input(prompt=f"Do you want to {mode.lower()} this record? (Y/N): ", command=("y", "n"))
        if (userInput == "y" and mode == "Edit"):
            oldCustName = record.get_customer_name()
            self.edit_record(record)
            if (oldCustName != record.get_customer_name()):
                self.__bst_root.move_node(record)
        elif (userInput == "y" and mode == "Delete"):
            self.delete_record(index=dbIndex)
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
                radix_sort(self.__db, reverse=reverseOrder)
                self.__descending_order = reverseOrder

                print(f"{F.LIGHTGREEN_EX}The database has been sorted by package cost per pax!")
                S_reset(nl=True)
                self.__sort_order = COST_PER_PAX
                return self.search_for_range_of_cost(low, high)
            else:
                arr = linear_search_range_of_cost(self.__db, low, high)
                if (arr):
                    self.print_from_array(arr)
                else:
                    print(f"{F.LIGHTRED_EX}No packages found with a cost between {low} and {high}!")
                    S_reset()
        else:
            indexOne, indexTwo = binary_search_for_range_of_cost(self.__db, low, high, self.__descending_order)
            if (indexOne == -1 and indexTwo == -1):
                print(f"{F.LIGHTRED_EX}No packages found with a cost between {low} and {high}!")
                S_reset()
            else:
                self.print_from_index(indexOne, indexTwo)

    def print_from_array(self, arr):
        """
        Print records from the given array (to satisfy the basic function c.1. criteria)
        Pagination is an added feature.
        
        Requires one argument:
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

            header = f"| {noHeader:^{noLen}} | {'Customer Name':<{self.__table_len[0]}} | {'Package Name':<{self.__table_len[1]}} | {'Cost Per Pax':>{self.__table_len[2]}} | {'Number of Pax':>{self.__table_len[3]}} |"

            # default rows to print per page, change at own will
            rowsToPrint = 10
            
            # initialise some variables
            counter = 0 # used for the for loop range arguments
            currentPage = 1 # used to indicate the current page
            maxPages = ceil(len(arr) / rowsToPrint) # number of pages to print

            # calculate the amount of records to print for the last page
            lastPageRecordsToPrint = len(arr) % rowsToPrint
            if (lastPageRecordsToPrint == 0):
                # set the lastPageRecordsToPrint to the rowsToPrint as it means that
                # there is no remainder, i.e. the length of the array 
                # is 10, 20, 30, and so on...
                lastPageRecordsToPrint = rowsToPrint

            # for the no. header numbers for the last page as the last page is using negative indexing
            noLastPageArr = [i + 1 for i in range(len(arr) - lastPageRecordsToPrint, len(arr))]

            while (1):
                print("Number of records:", len(arr))
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
                        print(f"| {i+1:^{noLen}}", end=" | ")
                        print(f"{record.get_customer_name():<{self.__table_len[0]}}", end=" | ")
                        print(f"{record.get_package_name():<{self.__table_len[1]}}", end=" | ")
                        print(f"{format_price(record.get_package_cost_per_pax()):>{self.__table_len[2]}}", end=" | ")
                        print(f"{str(record.get_pax_num()):>{self.__table_len[3]}} |")

                        counter += 1
                        if (counter >= len(arr)):
                            break
                # for the last page which will use negative indexing
                else:
                    for i in range(-lastPageRecordsToPrint, 0, 1):
                        record = arr[i]
                        print(f"| {noLastPageArr[i]:^{noLen}}", end=" | ")
                        print(f"{record.get_customer_name():<{self.__table_len[0]}}", end=" | ")
                        print(f"{record.get_package_name():<{self.__table_len[1]}}", end=" | ")
                        print(f"{format_price(record.get_package_cost_per_pax()):>{self.__table_len[2]}}", end=" | ")
                        print(f"{str(record.get_pax_num()):>{self.__table_len[3]}} |")

                    # calculate counter for the other pages, which will use positive indexing
                    counter = len(arr) - lastPageRecordsToPrint - rowsToPrint

                print("-" * len(header))

                print(f"Page {currentPage} of {maxPages}".rjust(len(header)), end="\n\n")

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
                            # go back a page
                            if (currentPage != maxPages):
                                # if the current page is not the last page, minus 1 from the current page
                                # and calculate the counter
                                counter -= (rowsToPrint * 2)
                                currentPage -= 1
                            else:
                                # if the current page is the last page, 
                                # minus the current page but do not calculate the counter as it is already calculated
                                # after the for loop for the last page.
                                currentPage -= 1
                        else:
                            # go to the next page
                            currentPage += 1

                        for _ in range(rowsToPrint + 8):
                            print("\033[1A\x1b[2K", end="") # move up a line and deletes the whole line
                else:
                    return
        else:
            print(f"{F.LIGHTRED_EX}Notice: There are no records to display...")
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
    
    def easter_egg_sorts(self, typeOfSort=None):
        """
        Method to sort the database using different non-sensical sorts such as bogosort
        
        Requires 1 argument:
        - typeOfSort (str) -> "bogosort", "bozosort", "stalinsort", "slowsort", "sleepsort"
        """
        if (not NOOB_SORTS_INFO_DICT.get(typeOfSort)):
            raise ValueError(f"Error: {typeOfSort} is not a valid sort type in easter_egg_sorts()")

        if (NOOB_SORTS_INFO_DICT[typeOfSort] == self.__sort_order and self.__descending_order == False):
            print(f"{F.LIGHTRED_EX}Error: The database is already sorted by {NOOB_SORTS_INFO_DICT[typeOfSort].lower()}...")
            S_reset()
            return

        if (typeOfSort == "bogosort" or typeOfSort == "bozosort"):
            # sorts by package name
            sortByBozosort = True if (typeOfSort == "bozosort") else False

            print("\nSorting...", end="")
            self.__db, iterNums = bogosort(self.__db, variant=sortByBozosort)
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