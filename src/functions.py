# import third-party libraries
from colorama import Fore as F
from colorama import Style as S
import pickle

# import standard libraries
import re, pathlib, logging
from datetime import datetime
from time import sleep
from random import randint, uniform, choice

# Welcome header message
HEADER = "Welcome to Waffle Hotel's Booking Records"

# regex for handling user inputs
RANGE_INPUT_REGEX = re.compile(r"^\d+(-)\d+|\d+$")

# to get the path of the directory that the python is being executed from
FILE_PATH = pathlib.Path(__file__).parent.resolve()

# for persistent storage of the records
PICKLE_FILE_PATH = FILE_PATH.joinpath("hotel_records.pickle")

# a tuple of strings that indicates True used in this project
USED_TRUE_CONDITIONS = ("y", "Y") 

# presets used in preinitialising the database with records
# by randomly selecting one element from each presets
PACKAGE_NAME_PRESETS = ["Budget Package", "Standard Package", "Premium Package", "Deluxe Package", "Luxury Package", "Ultimate Package"]
CUSTOMER_NAME_PRESETS = ["John Smith", "Jane Doe", "Jack Black", "Jill Jackson", "Juanita Jones", "Eden Lai", "Calvin Goh", "Mr Waffles"]

def S_reset(nl=0):
    """
    Function to reset colorama foreground, background colors and styles.
    
    Param:
    - nl (bool): If True, will print a new line after resetting colorama. Defaults to False.
    """
    if (nl): end = "\n"
    else: end = ""
    print(f"{S.RESET_ALL}", end=end)

def check_if_db_file_exists():
    """
    Check if the db pickle file exists
    """
    return PICKLE_FILE_PATH.is_file()

def preintialise_data():
    """
    Randomly picks a package name and customer name from the list of packages and customers predefined in this function and returns them in a tuple.
    """
    return choice(PACKAGE_NAME_PRESETS), choice(CUSTOMER_NAME_PRESETS)

def read_db_file():
    """
    Function to load the database file
    """
    from hotel_record import HotelDatabase

    db = HotelDatabase()
    if (check_if_db_file_exists()):
        with open(PICKLE_FILE_PATH, "rb") as f:
            db = pickle.load(f)
    else:
        # pre-initialize the database with 10 records to satisfy basic function b
        for _ in range(10):
            randPackage, randCust = preintialise_data()
            db.add_record(randPackage, randCust, randint(1,9), uniform(50,10000))

    return db

def save_db_file(db):
    """
    Function to save the database file for future runs
    """
    with open(PICKLE_FILE_PATH, "wb") as f:
        pickle.dump(db, f)
    print(f"{F.LIGHTGREEN_EX}Database file saved successfully!")
    S_reset()

def print_main_menu(numOfRecords):
    """
    Print the menu for user to choose their next action
    """
    
    print()
    print("*" * len(HEADER))
    print(f"{F.LIGHTYELLOW_EX}{HEADER}")
    print(f"{'System':^{len(HEADER)}}")
    S_reset()
    print("*" * len(HEADER))
    print()
    print("-" * 13, "Menu Options", "-" * 13)
    print()
    print(f"> Number of records: {numOfRecords}")
    print()
    print("1. Search records options")
    print("2. Add a new record")
    print("3. Edit records options")
    print("4. Sort records options")
    print("5. Delete records options")
    print("X. Exit application and save database")
    print()
    print("-" * 40)

def print_sub_menu(typeOfMenu):
    """
    Print the sub-menu based on the main menu option chosen by the user
    
    Requires one argument:
    - typeOfMenu (int): The main menu option that the user chose
    """
    if (typeOfMenu == 1):
        print()
        print("-" * 8, "Search Options", "-" * 8)
        print()
        print("1. Display all records")
        print("2. List records by cost (linear search/binary search + radix sort)")
        print("3. List records by customer name (binary search tree)")
        print("F. Back to main menu")
        print()
        print("-" * 33)
    elif (typeOfMenu == 3):
        print()
        print("-" * 13, "Edit Options", "-" * 13)
        print()
        print("1. Edit record by customer name (linear search)")
        print("2. Edit record by package name (linear search/binary search + heap sort)")
        print("F. Back to main menu")
        print()
        print("-" * 40)
    elif (typeOfMenu == 4):
        print()
        print("-" * 15, "Sort Options", "-" * 15)
        print()
        print("1. Sort records by customer name (bubble sort/tree sort)")
        print("2. Sort records by package name (selection sort)")
        print("3. Sort records by package cost (insertion sort)")
        print("4. Sort records by package's number of pax (shellsort)")
        print("F. Back to main menu")
        print()
        print("-" * 44)
    elif (typeOfMenu == 5):
        print()
        print("-" * 13, "Delete Options", "-" * 13)
        print()
        print("1. Delete record by customer name (linear search)")
        print("2. Delete record by package name (linear search/binary search + heap sort)")
        print("F. Back to main menu")
        print()
        print("-" * 42)
    elif (typeOfMenu == 6):
        print()
        print("-" * 10, "Easter Egg Menu Options", "-" * 10)
        print()
        print("1. Sort records by customer name (stalin sort)")
        print("2. Sort records by package name (bogo sort)")
        print("3. Sort records by package name (bozo sort)")
        print("4. Sort records by package cost (slow sort)")
        print("5. Sort records by package's number of pax (sleep sort)")
        print("Q. Back to sort menu")
        print()
        print("-" * 45)
    else:
        raise ValueError(f"Unknown type of sub-menu argument, {typeOfMenu}...")

def get_input(prints=None, prompt=None, command=None, warning=None):
    """
    Returns user's input based on the defined command paramater without 
    letting the user enter anything else besides the defined command parameter.
    
    Args:
    - prompt: The prompt to be displayed to the user.
    - prints: The message to be printed to the user.
    - command: The input to be accepted by the program.
    - warning: Used for displaying a custom error message.
    
    Defaults:
    - command: None but must be defined at all time as it will raise an Exception if not defined
    - prompt: "", an input without any prompt
    - prints: None, will not print out any messages
    - warning: None, will not display any error messages
    """
    if (not prompt): 
        prompt = ""

    if (not command): 
        raise ValueError("command keyword argument must be defined in the function, get_input")

    if (prints):
        print()
        if (isinstance(prints, tuple)):
            for line in prints:
                print(line)
        else: 
            print(prints)
        S_reset(nl=True)

    while (1):
        userInput = input(prompt).lower().strip()
        if (isinstance(command, tuple) and userInput in command): 
            return userInput
        elif (userInput == command):
            return userInput
        else: 
            if (warning): 
                print(f"{F.LIGHTRED_EX}Error: {warning}")
            else:
                if (not isinstance(command, tuple)):
                    print(f"{F.LIGHTRED_EX}Input Error: Please enter {command}.")
                elif (len(command) == 2):
                    print(f"{F.LIGHTRED_EX}Input Error: Please enter {command[0]} or {command[1]}.")
                else:
                    print(f"{F.LIGHTRED_EX}Input Error: Please enter {', '.join(command[:-1])}, or {command[-1]}.")

            S_reset(nl=True)

def log_error():
    """
    Logs an error message to the error log file
    """
    logFolderPath = FILE_PATH.joinpath("logs")
    logFolderPath.mkdir(exist_ok=True, parents=True)
    
    fileName = "".join(["error-details-", datetime.now().strftime("%d-%m-%Y"), ".log"])
    logFilePath = logFolderPath.joinpath(fileName)

    if (logFilePath.is_file()):
        with open(logFilePath, "a") as f:
            f.write("\n\n")
    else:
        with open(logFilePath, "w") as f:
            f.write("Waffle Hotel's Booking Records System Error Log\n\n")

    logging.basicConfig(filename=logFilePath, filemode="a", format="%(asctime)s - %(message)s")
    logging.error("Error Details: ", exc_info=True)

def countdown():
    """
    Prints a countdown message to the user before closing the application
    """
    print("Please press ENTER to exit...")
    input()
    for i in range(3, -1, -1):
        print(f"\rAutomatically shutting down in {i} seconds...", end="")
        if (i != 0): 
            sleep(1)

def shutdown(nl=0, program="Main"):
    """
    Print some messages before shutting down the program

    Args:
    - nl (int/bool, optional): Whether to print a newline before the shutdown messages. Defaults to 0/False.
    - program (str, optional): Print the corresponding program shutdown messages. Defaults to "Main".
    """
    if (nl): print()
    if (program.title() == "Main"): 
        print(f"\n{F.LIGHTYELLOW_EX}Thank you for using Waffle Hotel's Booking Records System!")
    else:
        print(f"\n{F.LIGHTRED_EX}Exiting program...")
    S_reset()
    countdown()

def get_range(userInput):
    """
    Used for retreiving a range from the user's input.
    
    Returns an integer or a list of integers
    
    Note: It uses the regex, "\d+(-)\d+|\d+" to check for input validity such as "1-2", or "1" which are valid.
    
    Requires one argument to be defined:
    - The user's URL input (string or list)
    """
    userInput = userInput.replace(" ", "")
    if re.fullmatch(RANGE_INPUT_REGEX, userInput):
        if ("-" not in userInput):
            return int(userInput)
        userInput = userInput.split("-")
        rangeList = [int(i) for i in userInput]
        
        # Check if the list in ascending order to make sure the range is valid
        if (rangeList[0] > rangeList[1]):
            # If not, swap the values
            rangeList = [rangeList[1], rangeList[0]]
        return rangeList
    else:
        return "error"

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

def convert_var_to_bool(var):
    """
    Convert a variable to a boolean
    
    Requires 1 argument:
    - var (str/int/float/bool): The variable to be converted
    """
    if (isinstance(var, bool)):
        return var
    elif (isinstance(var, int)):
        return bool(var)
    elif (isinstance(var, str) and var in USED_TRUE_CONDITIONS):
        return True
    else:
        False